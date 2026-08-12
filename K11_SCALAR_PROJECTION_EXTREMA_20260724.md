# Scalar-projection extrema and next compact cuts for `k=11,n=465`

## Status

The corrected Type-I/Type-II boundary--rank scalar projection is **integer
feasible**.  This remains true after adding the histogram-surplus rows from
`K11_HISTOGRAM_SURPLUS_CELL_CUTS_20260724.md` and all of the new scalar rows
proved below.  The computation therefore gives no scalar refutation of
length 465.

The useful outcome is a new set of sound compact refinements:

```text
lower-target rank-four rows,
candidate-count gap rows,
factor-five contaminated-triple rows,
joint candidate/triple rows,
endpoint/overlap-aware capped-capacity rows,
exact total short-cell OR-rank rows.
```

The first four use only the already exposed boundary and rank-histogram
quantities.  The endpoint/overlap and exact-OR-rank rows require local
physical-cell wires, but are still small relative to the full formula.

This note is not a SAT result for the complete OR formula.  Pointwise
coordinate banks, actual interval values, pin loads, endpoint alignments,
and the rank-seven shadow module are not variables of the scalar projection.

## 1. Audited scalar model

The audit uses the exact monotone rank-five and rank-six boundary vectors

```text
0<=h1<=...<=h6<=462,
0<=g1<=...<=g6<=462.
```

For each of the three corrected maximal rank-five chains A/B/C it uses the
exact formulas for `(y0,y1,y2)`, and it uses the exact rank-six formulas for
`(x0,x1,x2,x3)`.  Type I fixes `x0=1`; Type II fixes `x0=0`.

The following existing scalar rows are present:

```text
2*x0+x1 <= 138,
x1+2*x2+3*x3 >= 1008,
x3 >= 93+2*x0,

y0+x0 <= 135,
y2 >= y0+87+4*x0,
x0+x1 <= y0+3,
y2 <= x3+3,
y2 >= x1+82+14*x0,
x0+x1+y0+y1 <= 380-13*x0,
(x1+2*x2+3*x3)-(y1+2*y2) >= 455.
```

The entry-rank histogram satisfies

```text
n1+n2+n3+n4+n5+n6=465,
n1>=11,
n6=1 and n5<=133 in Type I,
n6=0 and n5<=134 in Type II,
n5=y0+delta,
```

where `(delta,s)` is `(0,1)` in Type I and one of

```text
(0,1), (1,1), (0,2)
```

in Type II.  Type I also has `n1+2*n2>=110`.

For every `s=1,...,10`, the exact nested rank-count row

```text
sum_r C(11-r,s-r)*nr >= RHS_s
```

is included, with

```text
RHS=(11,110,660,2640,7392,14322,14850,12540,7095,2794).
```

Finally, the audit contains `S>=649` in Type I and duplicate Type II, all
applicable old core-incidence rows, and the histogram-surplus rows

```text
F=sum_(r=1)^4 (nr-C(11,r))_+,
E=sum_(r=1)^4 r*(nr-C(11,r))_+.
```

The script also imposes the new scalar theorems of Sections 3--6 below.

The optional source modules whose variables are set-valued or positionwise
are deliberately outside this scalar model.  Thus “scalar feasible” means
exactly feasible in the displayed boundary/rank projection, not feasible in
the production CNF.

## 2. Remote exact optimization result

All CP-SAT optimization was run on RunPod Rose.  No optimization was run on
the user's workstation.

The final audit script is

```text
scratch/optimize_k11_scalar_projection.py
SHA-256 315b6e54d6d590457b5ab97526db613224ebb5ee289705b8b9231bfb95c72607
```

The frozen remote baseline source inspected for the scalar inventory was

```text
/root/k11_onion_20260723/k11_forest_sat_newcuts.cpp
SHA-256 2ab8ce03f844884c1dc6c5b4f742fe6e447680589172610fcd9649906ebdc26c
```

Every combination of

```text
branch in {Type I, Type II (0,1), Type II (1,1), Type II (0,2)}
chain  in {A,B,C}
```

is integer feasible after all scalar refinements in this note.

Here are Type-A feasible profiles from the final model.  They are arithmetic
profiles, not OR words.

| branch | `y=(y0,y1,y2)` | `x=(x0,x1,x2,x3)` | `(n1,n2,n3,n4); n5` | `(S,F,E)` |
|---|---|---|---|---|
| Type I | `(0,366,96)` | `(1,0,366,95)` | `(11,50,73,330);0` | `(1650,0,0)` |
| II `(0,1)` | `(134,107,221)` | `(0,0,244,218)` | `(11,55,0,265);134` | `(1181,0,0)` |
| II `(1,1)` | `(0,366,96)` | `(0,3,366,93)` | `(11,0,165,288);1` | `(1658,0,0)` |
| II `(0,2)` | `(0,367,95)` | `(0,3,366,93)` | `(11,0,165,289);0` | `(1662,0,0)` |

### 2.1 Exact margin minima

All entries in the next table are certified CP-SAT optima with every other
scalar row enabled.  `H2t` is the factor-five contaminated-triple row,
`H2g` the candidate-gap row, `H2c` their sound joint refinement, and `L4`
the lower-target rank-four row.

| branch | `min H0` | `min H1` | `min H2` | `min H2t` | `min H2g` | `min H2c` | `min L4` |
|---|---:|---:|---:|---:|---:|---:|---:|
| Type I | 0 | 0 | 9 | 8 | 0 | 0 | 0 |
| II `(0,1)` | n/a | n/a | 0 | 0 | 0 | 0 | 1 |
| II `(1,1)` | 0 | 0 | 9 | 8 | 0 | 0 | 0 |
| II `(0,2)` | 0 | 0 | 9 | 9 | 0 | 0 | 0 |

Thus none of the new rows is by itself an infeasibility certificate.  The
candidate and joint rows can still be tight in every branch.  The positive
minimum one for the non-tight `L4` margin is an integer consequence of the
whole audited scalar system; no independent combinatorial `+1` theorem is
claimed here.

Representative extremizers include:

```text
Type-I H0=0:
  y=(0,366,96), n=(11,50,73,330), n5=0, S=1650, F=E=0.

Type-I H1=0:
  y=(54,0,408), n=(266,55,1,88), n5=54,
  S=731, F=E=255.

Type-I minimum old H2 margin 9:
  y=(8,0,454), n=(354,0,1,101), n5=8,
  S=761, F=E=343.

Type-II (0,1) simultaneous H2=H2g=H2c=0:
  y=(86,0,376), n=(203,60,116,0), n5=86,
  S=671, F=197, E=202.
```

## 3. Lower-target rank-four rows

In a short-core branch every lower target has a singleton/pair witness.  The
useful singleton rank capacity is at most `S-E`.  After the `y1` selected
rank-five pair cells are removed, at most `1+y2` pair cells remain available
for lower targets.  Each such lower cell has OR-rank at most four.  Since the
561 lower targets require total rank 1936,

```text
1936 <= S-E+4*(1+y2).
```

Therefore, in Type I and the two tight Type-II cases,

```text
boxed: S-E+4*y2 >= 1932.                            (L4-short)
```

In the non-tight Type-II one-core case, all lower and selected nonliteral
rank-five witnesses have length at most three.  There are `2N-3` internal
pair/triple cells, and the `q=N-3` selected rank-five targets use `q` of
them.  At most `N` non-singleton cells remain for lower targets.  Hence

```text
1936 <= S-E+4*N,
N=465-n5,
```

or

```text
boxed: S-E-4*n5 >= 76.                              (L4-01)
```

## 4. Candidate-count gap and the `J=E-F` simplification

Let a candidate family contain all potentially useful singleton cells and
all internal pair/triple cells.  If it contains `G` more cells than the
number of required lower/rank-five targets, then at least `G` nonempty cells
are unused.  Subtracting one rank unit for each unused cell sharpens the
three-cell capacity row.

The raw guaranteed gaps are

| branch | gap |
|---|---:|
| Type I | `366-2*z-F` |
| II `(0,1)` | `369-2*n5-F` |
| II `(1,1)` | `368-2*n5-F` |
| II `(0,2)` | at least `366-2*n5-F` |

For the two-component branch the actual gap is
`366-2*n5-F+t1`, where `t1` indicates that one low component has length one.
The old H2 row must be retained when the displayed lower bound can be
negative.

In the non-tight branch, candidate-count feasibility itself gives the new
row

```text
boxed: F+2*n5 <= 369.                               (C0-01)
```

Put

```text
J=E-F=sum_(r=1)^4 (r-1)*(nr-C(11,r))_+.
```

The candidate-gap rows simplify to

```text
Type I:       6*S-J+7*z  >= 4620,
II (0,1):     6*S-J+7*n5 >= 4623,
II (1,1):     6*S-J+7*n5 >= 4627,
II (0,2):     6*S-J+7*n5 >= 4625.                  (C1)
```

For II `(0,2)`, `(C1)` is conjoined with the existing H2 baseline; this
implements the required `max(gap,0)`.

Both `F` and `J` have the exact 16-subset representation

```text
sum_r a_r*(nr-cr)_+
 = max_(R subset {1,2,3,4}) sum_(r in R) a_r*(nr-cr)
```

for `a_r=1` and `a_r=r-1`.  Thus no saturating subtractor is needed.

## 5. Factor-five contaminated-triple correction

Mark every internal pair cell selected as the witness of a rank-five target.
Every containing triple has OR-rank at least five.  It cannot witness a
lower target.  If its OR-rank is exactly five, its OR equals the contained
pair's rank-five target, so it cannot be the selected witness of any other
rank-five target.  It is therefore unused in the chosen distinct witness
family.

For a path component, let `k` edges be marked.  The number of incident
triple windows is at least `k`, unless every edge of that component is
marked, in which case it is `k-1`.  In Type I and both one-component
Type-II branches the selected-pair count is strictly smaller than the number
of component edges, so

```text
u>=y1.
```

In Type-II `(0,2)`, at most one component can have every edge marked (both
cannot be saturated because `y1<=q=N-3<N-2`).  Hence

```text
u>=max(y1-1,0).
```

Each contaminated triple has capped OR-rank exactly five.  This proves

```text
Type I:       6*S-E+5*z  >= 4254+5*y1,
II (0,1):     6*S-E+5*n5 >= 4254+5*y1,
II (1,1):     6*S-E+5*n5 >= 4259+5*y1,
II (0,2):     6*S-E+5*n5 >= 4259+5*max(y1-1,0).    (T)
```

The Type-II implementation needs no max wire.  Impose universally

```text
6*S-E+5*n5 >= 4254+5*y1,
```

add the `+5` version under the duplicate flag, and retain the existing 4259
baseline under the two-component flag.  Their conjunction is exactly `(T)`.

## 6. Correct interaction of candidate gaps and contaminated triples

The two corrections must not be naively added: contaminated triples are
already among the unused candidate cells.  If there are at least `G` unused
candidates and at least `u` contaminated triples, the rigorously removable
capped rank is

```text
5*u+max(G-u,0),
```

not `G+5*u`.

Using the branch lower bounds on `G,u` gives these compact joint rows:

```text
Type I:       6*S-J+7*z -4*y1  >= 4620,
II (0,1):     6*S-J+7*n5-4*y1 >= 4623,
II (1,1):     6*S-J+7*n5-4*y1 >= 4627,
II (0,2):     6*S-J+7*n5-4*y1 >= 4621.             (CT)
```

In II `(0,1)`, the separate contamination row is retained because `G` need
not dominate `y1`.  In II `(0,2)`, retain the old H2, candidate-gap, and
contamination rows as well; together with `(CT)` they implement the required
piecewise maxima at `y1=0`.  In Type I and duplicate Type II the H0 row gives
`G>=y1`, so `(CT)` already dominates the separate scalar projections.

These rows use only existing `S,J,n5,z,y1` arithmetic and 16 subset
comparisons.

## 7. Endpoint/overlap-aware capped-capacity refinement

The scalar rows replace every cell OR-rank by an entry-rank upper bound and
then use only a minimum boundary deficit.  The lost information can be
restored locally.

For all internal pair cells define

```text
B2 = 2*S - sum_pair sum_(i in pair) |Ai|,
L2 = sum_pair (sum_(i in pair)|Ai|-min(|OR(pair)|,5)).
```

A length-one component counts its sole endpoint twice in `B2`.  The exact
capped pair-cell capacity is `2*S-B2-L2`.  Therefore, precisely in the
short-core branches,

```text
boxed: 3*S-E-5*y1 >= 1936+B2+L2.                   (P-exact)
```

Similarly define over all internal pair and triple cells

```text
B3  = 5*S - sum_(pair/triple cell) sum_(i in cell)|Ai|,
L23 = sum_(pair/triple cell)
          (sum_(i in cell)|Ai|-min(|OR(cell)|,5)).
```

Then

```text
Type I:
  6*S-E+5*z >= 4246+B3+L23,

Type II:
  6*S-E+5*n5 >= 4246+B3+L23+5*delta.              (PT-exact)
```

Combining the contaminated triples with the same exact capacity gives

```text
Type I:
  6*S-E+5*z >= 4246+B3+L23+5*y1,

Type II:
  6*S-E+5*n5 >= 4246+B3+L23+5*delta+5*u,           (PTT)
```

where `u` has the branch lower bounds in Section 5.

These are capped-capacity relaxations: a cell with OR-rank above five is
unusable but `min(rank,5)` still credits it five.  Replacing the cap by
`rank*1[rank<=5]` is stronger.

No witness-choice loophole is present.  Chosen witnesses of distinct target
masks must occupy distinct physical cells.

## 8. Exact total short-cell OR-rank cut

Let `R3` be the exact sum of the actual OR-ranks of every internal low
singleton, pair, and triple cell.  This avoids the global `6*S` upper bound.

In Type I there are `3N-3` such cells and `561+q` required cells, so exactly

```text
366-2*z
```

cells are unused.  Their total rank is at least the unused count, plus:

* `J` extra units from forced unused surplus singleton cells;
* `4*y1` extra units from contaminated triples, whose rank is at least five.

The two classes are disjoint.  Comparing with required rank `4246-5*z`
gives

```text
boxed: R3+7*z-J-4*y1 >= 4612.                      (R3-I)
```

For Type II let `t1` be the number (zero or one) of length-one low
components.  The number of low cells is

```text
3*N-3*s+t1,
```

and the unused-cell count is

```text
372-2*n5-3*s+t1-delta.
```

In the two-component branch, a length-one component has no pair edge.  Thus
the possible one-unit saturation loss in the contaminated-triple count
disappears when `t1=1`.  Uniformly,

```text
u>=max(y1-1+t1,0)                    in the two-component branch.
```

The general exact row is

```text
R3+7*n5-J-4*u >= 4618+4*delta-3*s+t1.              (R3-II)
```

Thus:

```text
II (0,1): R3+7*n5-J-4*y1 >= 4615,
II (1,1): R3+7*n5-J-4*y1 >= 4619,
II (0,2): R3+7*n5-J-4*max(y1-1+t1,0) >= 4612+t1.
```

A convenient max-free Type-II projection is

```text
R3+7*n5+7*two >= 4615+J+4*y1+4*delta+5*t1.         (R3-II-linear)
```

For two components this is

```text
R3-J+7*n5-4*y1-5*t1 >= 4608.
```

Retaining the baseline unused-cell row handles the `y1=0,t1=0` corner in
which this max-free form intentionally gives away four units.

### 8.1 Compact physical encoding estimate

Reuse the exact `low[p]` flags.  For each adjacent pair and triple and each
of the eleven coordinates, define directly

```text
pair_contrib  <-> low[p]&low[p+1]&(A[p,b] or A[p+1,b]),
triple_contrib<-> low[p]&low[p+1]&low[p+2]
                  &(A[p,b] or A[p+1,b] or A[p+2,b]).
```

There are at most `11*(464+463)=10,197` contribution bits.  Direct
definitions need five clauses per pair bit and seven per triple bit, for
10,197 variables and 61,171 clauses.  An exact Wallace/ripple popcount needs
fewer than 20,424 variables and 142,968 clauses.  Reusing the existing
singleton-rank sum `S`, `J`, and boundary arithmetic gives the conservative
increment

```text
fewer than 33,000 variables and 225,000 clauses,
```

plus small comparison/guard glue.  This is near one percent of the current
roughly 20-million-clause formula and is a plausible next propagation
module.

## 9. Conclusion

The boundary--rank scalar projection is not the source of a length-465
contradiction: explicit integer profiles survive in every branch and every
A/B/C chain, even after the strongest compact scalar rows above.

The next useful information is physical and local.  The most economical
progression is:

1. add the factor-five and joint 16-subset scalar rows;
2. benchmark the exact `R3` module;
3. only if needed, expose the finer endpoint/overlap quantities `B2,L2,B3,L23`.

None of these results changes the proved value of `nu(11)` by itself.
