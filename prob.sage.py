

# This file was *autogenerated* from the file prob.sage
from sage.all_cmdline import *   # import sage library

_sage_const_20 = Integer(20); _sage_const_16 = Integer(16); _sage_const_44 = Integer(44); _sage_const_1 = Integer(1); _sage_const_759211060281786031869071242155234136314844944 = Integer(759211060281786031869071242155234136314844944); _sage_const_1057401451679095062531151979389760885573147826 = Integer(1057401451679095062531151979389760885573147826); _sage_const_2 = Integer(2); _sage_const_142926404549455192668575513920450762633800129 = Integer(142926404549455192668575513920450762633800129); _sage_const_3 = Integer(3); _sage_const_773808304364278082418521288269860813684230337 = Integer(773808304364278082418521288269860813684230337); _sage_const_155419950529021753751813670756068418661489493 = Integer(155419950529021753751813670756068418661489493); _sage_const_4 = Integer(4); _sage_const_564605286683346876667536567601259285744471988 = Integer(564605286683346876667536567601259285744471988); _sage_const_5 = Integer(5); _sage_const_812270051867990261460153809983232723732262237 = Integer(812270051867990261460153809983232723732262237); _sage_const_410837747859871710141162996756729573836835781 = Integer(410837747859871710141162996756729573836835781); _sage_const_7 = Integer(7); _sage_const_576115660671090581945855297280052151651777662 = Integer(576115660671090581945855297280052151651777662)
from secret import FLAG

a = int(FLAG.hex()[:_sage_const_20 ],_sage_const_16 )
b = int(FLAG.hex()[_sage_const_20 :_sage_const_44 ],_sage_const_16 )
p = int(FLAG.hex()[_sage_const_44 :],_sage_const_16 )

ecc = EllipticCurve(GF(p), [a,b])

ecc.point((p-_sage_const_1 ,  _sage_const_759211060281786031869071242155234136314844944 ))
ecc.point((p+_sage_const_1 , _sage_const_1057401451679095062531151979389760885573147826 ))
ecc.point((p+_sage_const_2 ,  _sage_const_142926404549455192668575513920450762633800129 ))
ecc.point((p-_sage_const_3 ,  _sage_const_773808304364278082418521288269860813684230337 ))
ecc.point((p+_sage_const_3 ,  _sage_const_155419950529021753751813670756068418661489493 ))
ecc.point((p-_sage_const_4 ,  _sage_const_564605286683346876667536567601259285744471988 ))
ecc.point((p-_sage_const_5 ,  _sage_const_812270051867990261460153809983232723732262237 ))
ecc.point((p+_sage_const_5 ,  _sage_const_410837747859871710141162996756729573836835781 ))
ecc.point((p-_sage_const_7 ,  _sage_const_576115660671090581945855297280052151651777662 ))

assert FLAG == bytes.fromhex(hex(a)[_sage_const_2 :] + hex(b)[_sage_const_2 :] + hex(p)[_sage_const_2 :])
