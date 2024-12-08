from true_math import divide as tr_div
from fake_math import divide as fk_div

res1 = fk_div(120, 3)
res2 = fk_div(11, 0)

res3 = tr_div(484, 11)
res4 = tr_div(565, 0)

print(res1, res2, res3, res4)