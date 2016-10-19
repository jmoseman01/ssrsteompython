import ssrsteom
from decimal import Decimal
x=ssrsteom.ssrsteom([Decimal('68.035'), Decimal('94.000'), Decimal('126.625'), Decimal('166.720'), Decimal('215.095'), Decimal('272.560')],Decimal("1.9"),Decimal(".3"))
#x=ssrsteom.ssrsteom(ssrsteom.lambdax(lambda x:5*x**3+4*x**2+7*x+6,Decimal("1.9"),Decimal("3.4"),Decimal(".3")),Decimal("1.9"),Decimal(".3"))
x.solve()
#ssrsteom.ssrsteom([Decimal("9"),Decimal("42"),Decimal("119"),Decimal("258"),Decimal("477")],Decimal("1"),Decimal("1")).solve()
#ssrsteom.ssrsteom(map(lambda x: 3*x**3+2*x+5,[1,2,3,4,5])).solve()
