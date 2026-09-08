# The F/Z plus six-N/Z ledger and the retained BQ fixed-axis bound

2026-09-08. Pure calculation by ternary_lift following root's FZ
proposal. Root supplied the aggregate substitution and six-one
geometry; ternary_lift independently checked them. The new fixed-axis
derivation below was independently read and checked by root, including
the NZ category counts, central-four equation, and all five infinity
cases: PASS. No computation occurred.

## 1. Correct aggregate and six-one geometry

Let F open four axes before closing any, with arbitrary closing order.
Its heights are1,2,3,4,3,2,1. Let Z=ABCABDCD, with heights
1,2,3,2,1,2,1. Then FZ has critical vector(0,5,6,1) and central
vector(0,2,3,2). Replacing TT+NN+5NZ by FZ+6NZ gives the entire
ten-bundle critical vector(26,75,18,1). With the original skeleton,
the central count vector is(8,41,31,4): one extra two-one G unit
and one extra four-one G unit. The excess costs are

    critical seven-one: 7/2;
    central two-one: 7;
    central four-one: 14;
    total: 49/2.

The two FZ six-one central cells are(F4,Z4) and(F5,Z3). Writing f
for F's first-closed axis, their unique(two,zero) pairs are
(Z-A,Z-D) and(f,Z-D). The skeleton leaves precisely the
infinity0/2 six-one G orbit and the infinity1 orbit of difference
plus/minus2. Hence infinity must be f or Z-A; when it is f require
Z-A minus Z-D = plus/minus2, and when it is Z-A require
f minus Z-D = plus/minus2. Both differences are in cyclic labels.

The seven-one critical cell(F4,Z3) has unique zero Z-D. Under
either admissible fixed-axis placement Z-D is cyclic, so this is
the already-covered nonfixed seven-one orbit, with infinity1.
Thus the total critical gap and endpoint sums are exactly21 and3.

## 2. The six NZ categories and FZ five-one contribution

Classify an NZ fixed-axis position by its five-one critical vector:

| Category | Axes | Vector by infinity0,1,2 |
| --- | --- | --- |
| Q | N-A or Z-D | (1,0,1) |
| R | N-B or N-D | (1,1,0) |
| S | N-C,Z-A,Z-B,Z-C | (0,2,0) |

Let ell be the opening position of f within F's initial four opens.
The six FZ five-one cells are original(3,4),(5,2) and complemented
(3,6),(4,5),(5,4),(6,3). Their vectors and the required numbers of
NZ positions in each category are:

| FZ infinity | FZ five-one vector | Numbers(Q,R,S) |
| --- | --- | --- |
| f opened at ell<=3 | (2,3,1) | (2,2,2) |
| f opened at ell=4 | (3,1,2) | (1,2,3) |
| Z-A | (3,2,1) | (2,1,3) |

Let d count N-D choices in R, a count Z-A choices in S, and c count
Z-C choices in S. Then the six NZ gap, endpoint, and central-four
infinity-one occurrence sums are respectively

    18-Q-d+c,
    Q+d+a,
    18-2Q-R-d-a.

Here Q,R also denote their category counts. These identities follow
from gaps2 on Q, gaps3/2 on N-B/N-D, gaps3 on N-C,Z-A,Z-B, and gap4
on Z-C. Endpoint indicators are1 exactly on Q,N-D,Z-A. The four-one
infinity-one counts are1 on Q,2/1 on N-B/N-D,3 on N-C,Z-B,Z-C, and
2 on Z-A.

## 3. The new extra four-one orbit still leaves at most one provider unit

Retain the literal zero-excess first BQ with gap2 and endpoint
indicator0. The other ten-flag provider is BQ or BR; write its gap
and endpoint indicator g,e. Write v,f for the six-flag provider's
gap and endpoint indicator, and s for whether infinity is one at
its unique four-one central cell. This includes the literal BU
and QV aggregate-preserving providers.

Let beta=1 when the unique extra four-one G orbit has infinity1,
and0 when it has infinity0/2. The residual four-one infinity1
demand is12 G orbits, so the completion must supply12+beta units.
The FZ three four-one cells are(F2,Z6),(F3,Z5),(F6,Z2). Their
infinity-one count alpha is2 for ell1/2,1 for ell3,0 for ell4,
and1 for infinity Z-A. Therefore

    d+a = s+kappa-beta,

where kappa=2 except that kappa=1 at ell3.

If w,h are FZ's gap and endpoint indicator, the required total
gap and endpoint sums21,3 give

    d-c = g+v+w-Q-1,
    d+a = 3-e-f-h-Q.

Combining the two expressions for d+a yields

    e+f+s = 3-h-Q-kappa+beta.

This gives the exhaustive fixed-axis consequence:

| FZ infinity | Consequence |
| --- | --- |
| f opened first | impossible: right side=-2+beta |
| f opened second | beta=1 and e=f=s=0 |
| f opened third | e+f+s=beta |
| f opened fourth | e+f+s=beta |
| Z-A | impossible: right side=-2+beta |

Thus FZ must first close infinity, which was opened second, third,
or fourth; in every surviving case

    e_other10 + e_six + s_six <= 1.

The extra four-one orbit is a real aggregate relaxation, but it does
not enlarge this particular provider-indicator bound. Consequently
the scoped second-BQ/BU and second-BQ/QV flag exclusions that use
only this bound and the unchanged one-one residual deck still apply.
This is not an obstruction to arbitrary other literal provider
profiles, fixed representatives, or a different repair budget.
