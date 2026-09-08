# Gate C: exact pairing--defect incidence and near-optimal random menus

**Status (2026-08-22).**  Every enumerative and probabilistic assertion
below is proved.  For the incidence relation

\[
 \{\text{perfect pairings }\mathcal P\}
\longleftrightarrow
 \left\{C\in{\Omega\choose b}:C\text{ is defect one for }\mathcal P\right\},
                                                               \tag{0.1}
\]

we compute the exact vertex degree and every pair codegree.  After
identifying `C` with its complement, the largest normalized codegree is

\[
                         {5(b-2)\over b^2}\sim {5\over b}.        \tag{0.2}
\]

A random menu of

\[
          \left(a_b+o(1)\right){4\over\sqrt\pi}
          {2^b\over b^{5/2}},\qquad a_b\longrightarrow\infty,    \tag{0.3}
\]

pairings covers all but `o(W)` middle targets.  This is optimal up to the
arbitrarily slow factor `a_b`, by the fixed-pairing atlas cap.

The menu is not yet a coherent-tour matching.  We isolate the exact first
refinement constraint: targets assigned to one pairing must be balanced
over all ordered `(empty,double)` fibers.  A fixed cyclic order supplies an
explicit middle-target-disjoint tour bank covering `Omega(1/b)` of its
pairing stratum, but coupling such banks across the menu without middle
collisions remains open.

Throughout, `b>=3` is odd, `|Omega|=2b`,

\[
 W={2b\choose b},\qquad q=b(b-1),\qquad
 \mathfrak P={ (2b)!\over2^b b!}=(2b-1)!!.             \tag{0.4}
\]

## 1. One-target degree

Fix `C in binom(Omega,b)`.  A perfect pairing `P` makes `C` defect one
exactly when it has one edge internal to `C`, one edge internal to
`C^c`, and all other edges cross the cut.  Therefore its degree is

\[
 \boxed{D_1={b\choose2}^2(b-2)!
             ={b!\,b(b-1)\over4}.}                    \tag{1.1}
\]

Indeed choose the two internal edges, then biject the remaining `b-2`
vertices on the two shores.  Every pairing has

\[
                         S_1=q2^{b-2}                  \tag{1.2}
\]

defect-one targets: choose its ordered empty and doubled pairs and one
member of every other pair.  Double counting gives the useful density

\[
 \boxed{p:={D_1\over\mathfrak P}={S_1\over W}
       ={q2^{b-2}\over {2b\choose b}}.}                \tag{1.3}
\]

## 2. Complete pair-codegree formula

Let `C,D in binom(Omega,b)` and put

\[
 d=|C\setminus D|,qquad a=b-d.                         \tag{2.1}
\]

Thus the four Venn cells

\[
 A=C\cap D,\quad B=C\setminus D,\quad
 G=D\setminus C,\quad E=\Omega\setminus(C\cup D)       \tag{2.2}
\]

have sizes `a,d,d,a`.

### Theorem 2.1 (exact codegrees)

The number `Lambda_d` of perfect pairings for which both `C` and `D` are
defect one is

\[
 \boxed{
 \Lambda_d=a!d!\left[
       ad(ad-1)+{a(a-1)+d(d-1)\over4}
                         \right].}                     \tag{2.3}
\]

The formula includes `Lambda_0=Lambda_b=D_1`.  For `1<=d<=b-1`,

\[
 \boxed{{\Lambda_d\over D_1}
  ={4ad(ad-1)+a(a-1)+d(d-1)
    \over b(b-1){b\choose d}}.}                       \tag{2.4}
\]

#### Proof

An edge of a simultaneous defect-one pairing which is not of type `AE` or
`BG` is part of a small defect core.  The core must contribute exactly one
edge internal to each shore of each of the cuts `(C,C^c)` and `(D,D^c)`.
After the core is removed, every remaining edge is forced to have type
`AE` or `BG`.

The following are all possible typed cores.  The last column is their
number after the remaining `AE` and `BG` vertices are bijected, divided by
`a!d!`.

\[
\begin{array}{c|c}
\text{core types}&\text{normalized contribution}\\ \hline
AA,EE&a(a-1)/4\\
BB,GG&d(d-1)/4\\
GG,AB,BE&a d(d-1)/2\\
BB,AG,GE&a d(d-1)/2\\
EE,AB,AG&d a(a-1)/2\\
AA,BE,GE&d a(a-1)/2\\
AB,AG,BE,GE&a(a-1)d(d-1).
\end{array}                                             \tag{2.5}
\]

To see both completeness and the counts, label the four required internal
incidences by `C,C^c,D,D^c`.  The double-incidence edge types are

\[
 AA:(C,D),\ EE:(C^c,D^c),\ BB:(C,D^c),\ GG:(C^c,D),    \tag{2.6}
\]

and the single-incidence types are `AB:C`, `AG:D`, `BE:D^c`, and
`GE:C^c`.  Partitioning the four labels into allowed edge types, while
requiring equal numbers of removed `A,E` endpoints and of removed `B,G`
endpoints, gives exactly the seven rows of (2.5).

For example, the `GG,AB,BE` row has

\[
 {d\choose2}\,a d(d-1)a\,(a-1)!(d-2)!
 =a!d!\,{a d(d-1)\over2}                              \tag{2.7}
\]

realizations.  The other rows follow by the displayed symmetries; the
four-single-edge row is obtained by choosing distinct endpoints and gives
`a!d!a(a-1)d(d-1)`.  Summing (2.5) gives

\[
 {a(a-1)+d(d-1)\over4}
 +ad(d-1)+da(a-1)+a(a-1)d(d-1)
 = {a(a-1)+d(d-1)\over4}+ad(ad-1),                    \tag{2.8}
\]

which proves (2.3).  Divide by (1.1) and use
`a!d!/b!=1/binom(b,d)` to get (2.4).  The endpoint cases are also immediate
directly: `D=C` or `D=C^c` imposes the same cut condition. \(\square\)

Complementary targets have identical pairing neighborhoods, which explains
`Lambda_b=D_1`.  Quotient the middle layer by `C~C^c`; its positive
distances are represented by `1<=d<=(b-1)/2`.

### Corollary 2.2 (maximum quotient codegree)

For `b>=7`, the maximum normalized codegree between distinct complement
classes is

\[
 \boxed{\max_{1\le d\le(b-1)/2}{\Lambda_d\over D_1}
       ={5(b-2)\over b^2},}                            \tag{2.9}
\]

attained at `d=1`.  For `b=3` the value is `5/9`; for `b=5` it is `16/25`
at `d=2`.

#### Proof

Substitution of `d=1` in (2.4) gives `5(b-2)/b^2`.  For `d=2`, comparison
with this value reduces to

\[
             5b^3-54b^2+179b-186\ge0,                 \tag{2.10}
\]

which holds at `b=7` and increases thereafter.  For `d>=3`, the numerator
of (2.4) is at most `b^4/4+b^2`, while
`binom(b,d)>=binom(b,3)`.  The desired comparison follows from

\[
 {b^4\over4}+b^2\le {5\over6}(b-1)^2(b-2)^2,           \tag{2.11}
\]

valid for every `b>=7`.  The two small cases follow by direct substitution
in (2.4). \(\square\)

## 3. A near-optimal random pairing menu

### Theorem 3.1 (near-cover by pairings)

For every integer `0<=R<=mathfrak P`, there is a set of `R` distinct
perfect pairings whose defect-one strata leave at most

\[
                         W e^{-pR}                     \tag{3.1}
\]

middle targets uncovered.

#### Proof

Choose the `R` pairings uniformly without replacement.  A fixed target has
exactly `D_1` compatible pairings, so its probability of being uncovered is

\[
 { {\mathfrak P-D_1\choose R}\over{\mathfrak P\choose R}}
 \le(1-p)^R\le e^{-pR}.                                \tag{3.2}
\]

Summing over the `W` targets gives expected uncovered count at most (3.1),
so some menu attains that bound. \(\square\)

Let `a_b->infinity` slowly enough that `ceil(a_b/p)<=mathfrak P`, and take

\[
                         R=\left\lceil{a_b\over p}\right\rceil.  \tag{3.3}
\]

Then the leave is at most `We^(-a_b)=o(W)`, while Stirling gives

\[
 R=(a_b+o(1)){W\over q2^{b-2}}
   =(a_b+o(1)){4\over\sqrt\pi}{2^b\over b^{5/2}}.      \tag{3.4}
\]

The universal fixed-pairing atlas cap requires
`Omega(2^b/b^(5/2))` pairings in any near-full coherent-tour packing, so
(3.4) is sharp up to the arbitrarily slow factor `a_b` at the pairing-only
level.

## 4. Exact tour-refinement ledger

For a fixed pairing `P={P_0,...,P_(b-1)}` and ordered distinct indices
`(t,i)`, let

\[
 \mathcal F_{\mathcal P;t,i}
 =\{C:C\text{ omits }P_t,\text{ doubles }P_i,
                 \text{ and splits every other pair}\}.          \tag{4.1}
\]

Each fiber has size `2^(b-2)`, the `q` fibers partition the defect-one
stratum, and every coherent tour on `P` contains exactly one target from
every fiber.

### Proposition 4.1 (necessary fiber balance)

If a target set assigned to `P` is a disjoint union of `m` complete
coherent tours, then

\[
                |\mathcal A_{\mathcal P}\cap
                  \mathcal F_{\mathcal P;t,i}|=m       \tag{4.2}
\]

for every ordered `t!=i`.  This balance is necessary but is not asserted to
be sufficient: the `q` fiber choices in one tour are coupled by one cyclic
pair order and one initial transversal state.

There is nevertheless a uniform local bank of middle-target-disjoint tours.
Fix one cyclic order of `P`, and parameterize its tours by initial states
`x in F_2^b`.  Two such tours are internally middle-disjoint exactly when

\[
                              d_H(x,x')\ge3.            \tag{4.3}
\]

Indeed, in fiber `(t,i)` the split word is
`(x+f_(t,i))|_([b]\setminus{t,i})` for a fixed offset `f_(t,i)`.  Two
tours share that target precisely when `x+x'` is supported on `{t,i}` for
some distinct `t,i`, equivalently when their distance is at most two.

Put `r=ceil(log_2(b+1))`.  Choose `b` distinct nonzero columns in
`F_2^r` and let `X` be the kernel of the resulting parity-check matrix.
No nonzero word of weight one or two belongs to `X`; hence `X` has minimum
distance at least three and

\[
 |X|\ge2^{b-r}>{2^b\over2(b+1)}.                       \tag{4.4}
\]

Thus every pairing contains an explicit fixed-order
middle-target-disjoint bank of at least `2^(b-r)` coherent tours, covering
more than a `2/(b+1)` fraction of its defect-one stratum.

The live outer-layer theorem is now exact: starting from a near-covering
menu such as Theorem 3.1, select middle-target-disjoint tour banks (or
partial banks) inside its pairing strata so that their middle targets are
also disjoint **across different pairings** and cover `(1-o(1))W` targets.
Equations (4.1)--(4.4) show that the local volume exists once the menu is
enlarged by a polynomial factor; they do not perform the cross-pairing
middle rounding.  Even after that rounding, collisions among designated
rank-`b-1` or rank-`b+1` tokens and extension to one full SCD remain
additional Gate-C requirements.

The companion checker
`scratch/verify_gate_c_pairing_defect_incidence_and_menu_20260822.py`
enumerates every pairing through `b=7`, verifies (1.1)--(2.4), checks the
quotient maximum, and audits the fixed-order code criterion.
