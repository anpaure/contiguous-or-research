# The exact PBBS component sector containing every positive run of length three

Date: 2026-09-08.
Status: proved from the canonical PBBS root formula and the established exact gap-five classification. Independent bounded verification against the original cyclic-parenthesis map was executed only on h100.

## 1. Result

Let n=2r+1, r>=3. Let f be the canonical PBBS permutation on rank-r subsets of the n-cycle, and consider the upper-middle owner factor with owners X=A^c and successor induced by f^2.

The union of components containing a positive coordinate run of length three consists of exactly

    r-2 components, each of length 3(2r+1).

Thus its exact owner mass is

    3(2r+1)(r-2).

Every other canonical owner component has all positive coordinate runs of length at least four. The full factor has no positive runs of lengths one or two.

At r=8 (k=17), the bad sector is exactly six cycles of length 51, containing 306 owners. They account for all 119 positive runs of length three. The remaining 24,004 owners lie in components with minimum positive residence at least four.

This is a statement about intact canonical components. Cutting and joining them can create new short runs or lose upper witnesses. The theorem does not claim a source of length B(17) or a safe fusion.

## 2. Imported finite PBBS facts

The established exact run-spectrum theorem is

    MATH_THEOREM_PBBS_EXACT_RUN_SPECTRUM_FLAT_ANTECEDENT_NOGO_AND_FULL_UPPER_DECK_20260813.md.

It supplies the following precise facts.

- An omitted-label gap g=2s+1 gives a positive run of length s+1 in the upper-middle f^2 owner factor, and every proper positive run arises uniquely this way.
- No gap one or gap three occurs.
- The normalized roots starting a consecutive gap five are exactly

      D=(10)^a 1(10)^b 0,
      a>=0, b>=1, a+b=r-1.

  There are r-1 such roots and n physical rotations each, giving n(r-1) positive runs of length three.

The normalized one-step map at the first up-step attaining maximum height is also established: if D=P1Q, then

    phi(D)=complement(Q) 0 complement(P).

For a physical root u, the new root is u+|P|+1 modulo n. Here a rooted state means a zero at u followed cyclically by the Dyck word D. These facts also follow directly by complementing all matched positions and keeping the unique unmatched zero absent.

## 3. Complete defect-one class and its explicit dynamics

A Dyck word of semilength r with r-1 peaks has exactly one ascent of length two, exactly one descent of length two, and all other ascents and descents of length one. Since it remains nonnegative, the double ascent occurs no later than the double descent. Consequently it has the unique form

    D(a,b,c)=(10)^a 1(10)^b 0(10)^c,
    a,c>=0, b>=1, a+b+c=r-1.

Equivalently, writing x=a, y=b-1, z=c,

    x,y,z>=0, x+y+z=r-2,
    D(x,y,z)=(10)^x 1(10)^(y+1) 0(10)^z.

There are binom(r,2) such roots.

The first up-step reaching height two is the second up-step of the nontrivial excursion, at physical offset 2x+2 from root u. In the root formula,

    P=(10)^x 1,
    Q=0(10)^y 0(10)^z.

Substitution and elementary concatenation give

    phi(D(x,y,z))=D(y,z,x).

Thus the complete physical map on this class is

    f:(x,y,z,u) -> (y,z,x,u+2(x+1)) mod n.              (1)

This proves invariance of this class directly; no general soliton-invariance theorem is needed.

After three steps the triple returns and the root has advanced by

    2(x+y+z+3)=2(r+1)=n+1,

hence by one modulo n.

A triple not fixed by cyclic rotation therefore gives one f-cycle of length 3n: no one- or two-step multiple can return its triple, while f^3 rotates its root by one. Since 3n is odd, f^2 has exactly the same component.

The only possible fixed triple has x=y=z. Its coordinates are all positive except when r=2, outside the present theorem. Such an interior triple therefore cannot contain a gap-five start and plays no role below.

## 4. Which components actually contain the short run?

By the exact gap-five classification, a gap-five starting root in this class has z=0. Under (1), its component contains such a root if and only if at least one of x,y,z is zero.

Conversely every positive run of length three comes from a gap-five start. Its root lies in this invariant class, so its whole owner component is among precisely these boundary-triple components. This proves both containment directions; other soliton classes cannot hide an additional bad component.

For N=r-2>=1, the number of nonnegative ordered triples summing to N with at least one coordinate zero is 3N. One proof counts the triples with exactly one zero (3(N-1), interpreted as zero at N=1) and the three triples with two zeros. None is fixed by cyclic rotation, so division by three gives N=r-2 quotient components.

Each lifts to one f^2 cycle of length 3n by Section 3. Their total mass is 3n(r-2). All runs outside these components have length at least four because lengths one and two are absent globally and all length-three runs have just been classified. This proves the theorem.

For r=8 one may use the following six cyclic-triple representatives:

    (0,0,6), (0,1,5), (0,2,4),
    (0,3,3), (0,4,2), (0,5,1).

There is one physical 51-cycle per representative. Exactly one quotient class has two zero coordinates; it contains two gap-five root phases. The other five have one. Hence these components contain

    17*(2+5)=119

positive runs of length three, agreeing with the independent n(r-1) census.

## 5. Verification record

One bounded original-map check was executed by ssh h100 on 2026-09-08. It did not search for a construction or run a solver.

For each r=3,...,10, the script enumerated the finitely many explicit triples and their n roots. It independently found each state's unique root by testing cyclic Dyck rotations, evaluated

    f(A)=A^c minus {the unique unmatched zero},

and compared that actual mask with (1). It then decomposed the boundary sector under two actual f evaluations per step, and counted literal positive coordinate runs in the complemented owner cycles.

Recorded output:

| r | all defect-one owners | bad components | length of each | bad-sector owners | positive runs of length 3 |
|---:|---:|---:|---:|---:|---:|
| 3 | 21 | 1 | 21 | 21 | 14 |
| 4 | 54 | 2 | 27 | 54 | 27 |
| 5 | 110 | 3 | 33 | 99 | 44 |
| 6 | 195 | 4 | 39 | 156 | 65 |
| 7 | 315 | 5 | 45 | 225 | 90 |
| 8 | 476 | 6 | 51 | 306 | 119 |
| 9 | 684 | 7 | 57 | 399 | 152 |
| 10 | 945 | 8 | 63 | 504 | 189 |

Terminal result:

    PASS: original cyclic-parenthesis f map agrees with rotating defect-one
    coordinates; exact bad-component and run counts r=3..10.

The general proof is Sections 2-4. The finite check is supporting verification, not a substitute for its all-r argument.

## 6. Consequence for a variable-depth construction

For k=17, it is unnecessary to place all height-at-most-two states into a shallow sector just to accommodate the canonical positive-three runs. Only the six components above need that treatment. Their unmodified internal runs are compatible with depth two. Every other intact component is compatible with depth three.

This reduces the intact-component sorting bill from the entire 2^7*17=2176-owner height-at-most-two sector to 306 owners. It does not yet show that a prefix of 306 owners is enough after fusion: the seams must retain valid runs, and all cyclic upper witnesses destroyed by cuts must be transported or recreated. Any arithmetic slack remaining after the variable schedule is capacity for a construction, not permission to discard these obligations.
