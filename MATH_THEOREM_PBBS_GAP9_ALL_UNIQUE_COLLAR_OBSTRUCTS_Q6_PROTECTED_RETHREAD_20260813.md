# A gap-nine PBBS collar has six forced immediate-upper witnesses: the old-flag-preserving `q>=6` rethread is impossible

**Date:** 2026-08-13  
**Status:** unconditional all-parameter obstruction on the literal
old-witness-preserving face; exact remote enumeration identifies a larger
six-slot family, but the one displayed collar already proves the theorem  
**Scope:** the standard GK/complement realization of the centered PBBS
owner factor, which is occurrence-isomorphic to the cyclic PBBS realization

## 1. Statement

Put

\[
 n=2m+1,\qquad m\ge 6,
\]

and let `F_m` be the complement-centered PBBS factor on the rank-`m+1`
owners.  Its edges are indexed by rank-`m` words `L`.  If `a(L)` is the
GK-up zero and `b(L)` is the complement-GK-up zero, the edge indexed by
`L` is

\[
 \{L+a(L),L+b(L)\},                              \tag{1.1}
\]

and its immediate-upper colour is

\[
 Q(L)=L+\{a(L),b(L)\}.                            \tag{1.2}
\]

Here and below words are written in coordinate order `0,1,...,2m`.

### Theorem 1.1 (all-unique gap-nine collar)

The factor `F_m` contains seven consecutive owners

\[
 V_{-1},V_0,V_1,V_2,V_3,V_4,V_5                 \tag{1.3}
\]

such that coordinate `0` is absent on `V_{-1},V_5` and present on exactly
the five intervening owners.  Every one of the six collar edges

\[
 E_j=V_{j-1}V_j\qquad(0\le j\le5)               \tag{1.4}
\]

has an immediate-upper colour `U_j` of global PBBS multiplicity one.

Consequently, if a rethread is obtained by cutting old PBBS edges into
pieces and is required to retain at least one **old** immediate-upper
witness of every target, then it cannot be `q`-safe for any

\[
 q\ge6.                                           \tag{1.5}
\]

This already refutes the capacitated collar-transversal condition `(4.5)`
in
`MATH_SYNTHESIS_SECOND_SHADOW_SUPPORT_CLOSED_AND_LONG_RESIDENCE_RETHREAD_GATE_20260813.md`
for every `m>=6` and `q>=6`.

For the OR-word target `q=d(2m+1)+1`, one has `q>=6` for every `m>=20`,
so the obstruction applies from ground size `41` onward.

## 2. The literal collar

Put

\[
 T=(10)^{m-4}.                                    \tag{2.1}
\]

The seven owners are

\[
\begin{array}{c|l}
-1&0111110\,T\,00\\
 0&1111100\,T\,00\\
 1&1111000\,T\,01\\
 2&1110000\,T\,11\\
 3&1100001\,T\,11\\
 4&1000011\,T\,11\\
 5&0000111\,T\,11.
\end{array}                                       \tag{2.2}
\]

Every word has weight `m+1`.  Their consecutive intersections `L_j` and
unions `U_j` are

\[
\begin{array}{c|l|l}
j&L_j&U_j\\ \hline
0&0111100\,T\,00&1111110\,T\,00\\
1&1111000\,T\,00&1111100\,T\,01\\
2&1110000\,T\,01&1111000\,T\,11\\
3&1100000\,T\,11&1110001\,T\,11\\
4&1000001\,T\,11&1100011\,T\,11\\
5&0000011\,T\,11&1000111\,T\,11.
\end{array}                                       \tag{2.3}
\]

Linear `01`/complement-`01` cancellation gives

\[
\begin{array}{c|c|c}
j&a(L_j)&b(L_j)\\ \hline
0&5&0\\
1&4&2m\\
2&3&2m-1\\
3&2&6\\
4&1&5\\
5&0&4.
\end{array}                                       \tag{2.4}
\]

Thus (1.1) gives exactly the consecutive edges in (2.2), and (1.2) gives
the six words in the last column of (2.3).  In particular (2.2) is not an
abstract Johnson path: it is a literal path in the actual centered PBBS
factor.

The first bits in (2.2) are

\[
                         0,1,1,1,1,1,0.            \tag{2.5}
\]

Hence coordinate zero has a maximal positive owner run of length five.
Its complete run collar is precisely `E_0,...,E_5`.  In omitted-label
language this is a gap-nine return.

## 3. Each collar colour is globally unique

The PBBS angle-occurrence lemma gives a shorter and safer global check.
Put

\[
                         S_j=[n]\setminus U_j.      \tag{3.1}
\]

For `u notin S_j`, let `alpha_j(u)` be the forward survivor after adding
`u` to `S_j`, and let `beta_j(u)` be the reverse survivor.  Occurrences of
`U_j` are in bijection with fixed points of

\[
                         \beta_j\alpha_j.           \tag{3.2}
\]

Moreover every fixed point lies in the three-element reverse-survivor set
`U_-(S_j)`.

Contract the untouched `10` pairs in `T`.  Direct cancellation gives

\[
\begin{array}{c|c|c|c}
j&U_-(S_j)&\alpha_j(u)\ (u\in U_-(S_j))
            &\beta_j(\alpha_j(u))\\ \hline
0&\{3,4,5\}&0&5\\
1&\{2,3,4\}&2m&4\\
2&\{1,2,3\}&2m-1&3\\
3&\{0,1,2\}&6&2\\
4&\{0,1,2m\}&5&1\\
5&\{0,7,2m\}&4&0.
\end{array}                                       \tag{3.3}
\]

For example, in row zero the contracted word is a block of six zeros
followed by the three reverse survivors `3,4,5`; adding any one of those
three marks makes forward cancellation leave `0`, and adding `0` in the
reverse scan leaves `5`.  The other five rows are the same finite boundary
scan, shifted across the four leading ones; an intact `10` factor
contributes no survivor.  Thus (3.3) is independent of the number
`m-4` of contracted factors.

The last column is constant on `U_-(S_j)` and equals respectively

\[
                         5,4,3,2,1,0.              \tag{3.4}
\]

Exactly one member of each three-element set is fixed.  Therefore

\[
                         |\operatorname {Fix}(\beta_j\alpha_j)|=1
                         \qquad(0\le j\le5).       \tag{3.5}
\]

By the occurrence/fixed-point bijection,

\[
                         Q^{-1}(U_j)=\{L_j\}
                         \qquad(0\le j\le5),       \tag{3.6}
\]

which proves global multiplicity one, not merely distinctness inside the
displayed path.

## 4. The obstruction

Let `D` be the set of old PBBS edges cut by a piece-preserving rethread.
Retaining an old witness of every immediate-upper target requires

\[
 |D\cap Q^{-1}(U)|\le |Q^{-1}(U)|-1              \tag{4.1}
\]

for every `U`.  Equation (3.6) forces

\[
                         D\cap\{E_0,\ldots,E_5\}
                         =\varnothing.             \tag{4.2}
\]

On the other hand, if a positive run collar of length below `q` contains
no cut, that entire `0,1,...,1,0` pattern remains inside one unchanged
piece after the pieces are permuted.  For `q>=6`, (2.5) is such a run, so
every `q`-safe piece rethread must satisfy

\[
                         D\cap\{E_0,\ldots,E_5\}
                         \ne\varnothing.           \tag{4.3}
\]

Equations (4.2)--(4.3) contradict one another and prove Theorem 1.1.

For odd ground `k=2m+1`, the complete strict-lower count is

\[
 \Lambda=2^{2m}-1,
 \qquad W={2m+1\choose m}.
\]

The target slack `d` is the least integer satisfying

\[
 \Lambda\le dW+{d+1\choose2}.                     \tag{4.4}
\]

At `m=20`,

\[
 2^{40}-1-4{41\choose20}-10=22,995,878,885>0,     \tag{4.5}
\]

so `d>=5`.  The ratio `4^m/binom(2m+1,m)` is strictly increasing because

\[
 {4^{m+1}/\binom{2m+3}{m+1}
  \over
  4^m/\binom{2m+1}{m}}
 ={4m+8\over4m+6}>1.                              \tag{4.6}
\]

Hence (4.5) persists for every `m>=20`, proving `q=d+1>=6` throughout
that range.

## 5. Larger exact pattern found by the audit

The durable verifier

```text
scratch/audit_pbbs_qsafe_cut_capacity_20260813.py
```

constructs the actual factor, extracts every short positive-run collar,
adds one SAT clause saying that every collar is cut, and adds one clause
saying that every immediate-upper fibre retains an old edge.  It was run
only on `h100` for the substantive instances.

For `q=6`, the number of collars all of whose edges have multiplicity-one
upper colours is

\[
\begin{array}{c|rrrrrrr}
m&4&5&6&7&8&9&10\\ \hline
\text{blocked collars}&9&66&273&840&2142&4788&9702.
\end{array}                                       \tag{5.1}
\]

These values are exactly

\[
                 (2m+1){m+1\choose5}.             \tag{5.2}
\]

After normalizing the middle centre of a blocked collar to `0D`, the
verified roots are exactly

\[
\begin{aligned}
D_{\boldsymbol a}={}&(10)^{a_0}1(10)^{a_1}111
 0(10)^{a_2}0(10)^{a_3}\\
 &\hspace{25mm}0(10)^{a_4}0(10)^{a_5},\\
 &a_0+\cdots+a_5=m-4.
\end{aligned}                                     \tag{5.3}
\]

There are `binom(m+1,5)` weak compositions, and every root has all
`2m+1` spatial phases.  Formula (5.3) explains (5.2) and contains the
proved display above at

\[
                 (a_0,a_1,\ldots,a_5)=(m-4,0,\ldots,0).
\]

The equality between *all* blocked collars and (5.3) is currently an
exact finite classification through `m=10`, not used as an all-parameter
premise.  Promoting it to an all-`m` theorem requires only a six-slot
leaf-contraction converse.  The explicit one-root family in Sections
2--4 already gives the unconditional obstruction.

The SAT status displays the sharp threshold in the tested range:

\[
\begin{array}{c|c|c}
q&4,5&6\text{ and above}\\ \hline
m=6,\ldots,9&\mathrm{SAT}&\mathrm{UNSAT}.
\end{array}                                       \tag{5.4}
\]

The `UNSAT` cases need no solver certificate: any one collar from
Theorem 1.1 is a unit-clause contradiction.

## 6. Relation to the peak-defect return conjecture

The formerly proposed pointwise inequality

\[
 g\ge 2igl(m-\operatorname{pk}(D)\bigr)+1
 \tag{6.1}
\]

is already false in the actual PBBS.  The all-parameter counterexample in
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, Theorem 18.1, is

\[
 D_{m,e}=(10)^{m-(2e-1)}(1100)^{e-2}111000,
 \qquad e\ge4,\quad m\ge2e-1.                 \tag{6.2}
\]

It has peak defect `e` but a consecutive return of gap seven, so its
right side in (6.1) is `2e+1>=9`.  Thus Narayana enumeration cannot be
invoked through that pointwise shortcut.  This counterexample is distinct
from the gap-nine unique-fibre obstruction above: (6.2) concerns aggregate
return packing, whereas Sections 2--4 concern protected upper-witness
capacity.

## 7. Exact scope and new route

The theorem proves a literal occurrence-column obstruction, not a no-go
for every global chronology.  It rules out any proof which simultaneously

1. cuts the old PBBS factor into unchanged pieces;
2. retains an old PBBS witness of every immediate-upper target; and
3. asks the output pieces to be `q`-safe for `q>=6`.

It does **not** rule out deleting one of `E_0,...,E_5` and creating a new
Johnson edge with the same colour `U_j`.  Therefore the replacement-enabled
PBBS theorem must contain a genuine rematerialization move.  More
precisely, every repaired chronology must rematerialize at least one of
the six colours in (2.3), and the full six-slot family (5.3) strongly
suggests that such replacements are needed in
`(2m+1) binom(m+1,5)` translated local collars.

Thus the old-flag-preserving route is closed.  The surviving positive
target is narrower and more concrete:

\[
 \boxed{
 \text{construct a phase-synchronous gap-nine replacement which creates}
 \text{ a fresh witness in each punctured unique upper fibre.}}
\]
