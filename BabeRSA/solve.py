#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes as lb
from Crypto.Util.number import inverse
from Crypto.Util.number import GCD
from functools import reduce

modulus = 23179828669733827446628349471333288738084373436792992362734031873059287122808115763019210238930484207237950330265853033858636038557596862607202767020990826415650292823519778448829493189207280947702739046496232409292264980716239614242043639522047546828425698077513842504450817609995651373609586653934704030312593725975452304953191546414952667461477240987620867494770187874976920840440771143576440900251452176814787763110053534551038710239372648564421863861102338066424826036088971633049161401520274005882358361577885362043543967316621782313497782452369189128686543412436206597154588646741556028654872322517769688473421
key1 = 14630353321071091676401516769328327836777128628492970474117131668117043646595737054920172730263168709401774098417947666521943696762936416365010587155032484901915646860302663842268144811510513033378329172928185402526759755167653674689972686182118520513564690968828252241088119259884891102074491750852401078633629432725515432110322978029581458575636267872797375740245807376189740405988949851035026395032180255754674195299024679765052467889470390342577543072260102869819446037358460949801157657731476956407504555345509331581215657775553184097839004615829835343123174852930599291393285649447609898933393362904662517753319
exp1 = 5469342234088524207782091028137909547874959970036956407852044176141704866411338476316240300140875668233899334390219777989868327579997439398171768007463620

cipher1 = 19270992740151708293848699994770846543365208387312216287360064969323918442508630810076464038894409637595437041475636872589239658903300322147271621867772318656160365823830850574711575185158017179713187030999287002873007981477274241988350419767784868854083995264066198914538463564937035003494282107689943532832418093638809282013893246267457033311573025634700654750085043430456115187231026443817580876103984242830494236022041651097696291702834899635462277396373582376765259784043124399847174059652581243889967409652229198426095566672618038844457624492617487176362804798498642353424272861112854007232025669116571120636919
cipher2 = 18757179287228727801566739871336086101086517493342748952835627696635321425840378044298412731234569391503914640195842971706099975879928282437263148785005944194910761869094204755605810409265242397640446534212789240561253387756018826164552254409960890044705076018951063643069823430525326807587111204002527843667919572610926053566499315554090619601323460199016259583403394707127295207357640490233373565893314423238460988814335144131990224518886990286404436027496568899889977857785587200007312546513181794126734044118996675536656478081304673378124955732978191160936244513631961604253332761892272301094814912303418433213842

def decrypt(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod



def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

p = GCD(key1-1, modulus)
q = modulus // p
assert p*q == modulus

print(f"Cheesy: {lb(cipher1*inverse(pow(key1,exp1,modulus), modulus) % modulus).decode()}")
print(lb(decrypt([p, q], [cipher1, cipher2])).decode())

#HZiXCTF{F3rm4t_LiTT!3_7heoRem_f0r_3verY_B483R54}