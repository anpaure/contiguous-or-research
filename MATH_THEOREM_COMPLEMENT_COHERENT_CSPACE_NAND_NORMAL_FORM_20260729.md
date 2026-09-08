# Complement-coherent c-space is a cyclic NAND shift

Date: 2026-07-29

Status: exact normal-form theorem.  It identifies a sharply smaller
`k=15` carrier subclass.  It does not assert that the subclass contains a
decorated carrier.

## 1. Binary trace setup

Let `k=2m+1`, let

\[
 r=m+1,\qquad W=\binom{k}{r}=kC,qquad
 C=\operatorname{Cat}_m,
\]

and use the unit-voltage binary trace representation

\[
 T_i=\{x\in\mathbb Z_k:c_{i-xC}=1\},
 \qquad c\in\{0,1\}^{\mathbb Z_W}.                    \tag{1.1}
\]

Assume that the `T_i` form a Hamilton Johnson cycle and that their adjacent
intersections

\[
                         X_i=T_i\cap T_{i+1}           \tag{1.2}
\]

enumerate the rank-`m` layer.  Thus

\[
 T_0,X_0,T_1,X_1,\ldots,T_{W-1},X_{W-1}              \tag{1.3}
\]

is a Middle Levels Hamilton cycle.

Plain complement coherence is possible only when `W` is odd.  Write

\[
                         W=2s+1,qquad t=s+1.          \tag{1.4}
\]

Then `2t=1 mod W`.

## 2. Scalar complement law

### Theorem 2.1

The Middle Levels cycle (1.3) is complement coherent, with complementation
acting by its forced half-turn, if and only if

\[
 \boxed{1-c_p=c_{p+s}c_{p+s+1}}
 \qquad(p\in\mathbb Z_W).                              \tag{2.1}
\]

Equivalently,

\[
 \boxed{c_{q+t}=\operatorname{NAND}(c_q,c_{q+1})}
 \qquad(q\in\mathbb Z_W).                              \tag{2.2}
\]

#### Proof

Complement coherence of a Middle Levels Hamilton cycle cannot act as a
reflection: an edge-axis reflection would fix an incidence edge setwise and
would therefore require an edge `Y--complement(Y)`, which is impossible for
`m>0`.  Its action is the half-turn.  With the standard indexing this is

\[
                         \overline{T_i}=X_{i+s}.        \tag{2.3}
\]

At coordinate `x`, (1.1)--(1.2) turn (2.3) into

\[
 1-c_{i-xC}
   =c_{i+s-xC}c_{i+s+1-xC}.
\]

As `i-xC` ranges over every `p`, this is (2.1).  Conversely, (2.1) gives
(2.3) coordinatewise and hence makes complementation the half-turn of
(1.3).  Replacing `p` by `q+t` and using `-s=t mod W` gives (2.2).
\(\square\)

## 3. Local NAND word

Define the permuted trace

\[
                         d_j=c_{tj}.                   \tag{3.1}
\]

Because `2t=1 mod W`, equation (2.2) becomes

\[
 \boxed{d_{j+1}=\operatorname{NAND}(d_j,d_{j+2})}.     \tag{3.2}
\]

### Corollary 3.1

Equation (3.2) is equivalent to the two local forbidden patterns

\[
                            00,\qquad 111.              \tag{3.3}
\]

Thus every zero of `d` is isolated, and every cyclic one-run has length one
or two.

#### Proof

If the middle bit is zero, (3.2) says both neighbours are one.  If the
middle bit is one, its two neighbours are not both one.  This is exactly
(3.3), and the converse is the same argument reversed.  \(\square\)

The middle-rank class sums in (1.1) give

\[
 \sum c=(m+1)C,qquad \#\{c=0\}=mC.                   \tag{3.4}
\]

Permutation preserves these totals.  Every zero of `d` begins one one-run,
so `d` has `mC` one-runs.  If `a` of them have length two, then

\[
 mC+a=(m+1)C,
\]

and hence

\[
 \boxed{
 \#(11\text{-runs})=C,qquad
 \#(1\text{-runs})=(m-1)C.}                           \tag{3.5}
\]

For `k=15`, this is

\[
 W=6435,quad C=429,quad
 \#0=3003,quad \#(11\text{-runs})=429,quad
 \#(1\text{-runs})=2574.                              \tag{3.6}
\]

These counts are forced and should not be search objectives.

There is a second forced count in the **physical** `c` order.  Since
`c_p=d_(2p)`, a cyclic transition `c_p=1,c_(p+1)=0` is a step-two pattern

\[
                         d_i\,*\,d_{i+2}=1\,*\,0.
\]

The middle bit is necessarily one by (3.3), and the pattern is therefore
`110`.  Such a pattern occurs exactly once at the end of every length-two
one-run of `d`.  Consequently

\[
 \boxed{\#\text{ cyclic one-runs of }c=C}.             \tag{3.7}
\]

Thus the Catalan physical run count is already forced by the NAND law and
the middle class sums; lower-q1 exactness still has to make the associated
rank-`m` run labels distinct.

## 3.2 Gap-residue collapse of the eager equations

Let `Z` be the zero set of `d`, listed in its natural cyclic order.  By
(3.3), consecutive zeros have gaps two or three.  Call a zero **special**
when its outgoing gap is three.  The totals (3.4) give `mC` zeros, and if
`s` is the number of special zeros then

\[
 2mC+s=W=(2m+1)C,
\]

so `s=C`.

For `a in Z_C`, let `n_a` be the number of zeros congruent to `a mod C`, and
let `s_a` be the number of special zeros in that residue.  Every zero of
residue `b` has a unique predecessor: either a gap-two predecessor in
residue `b-2` or a gap-three predecessor in residue `b-3`.  Hence

\[
 \boxed{n_b=n_{b-2}-s_{b-2}+s_{b-3}.}                 \tag{3.8}
\]

### Theorem 3.2 (perfect long-gap residues)

Inside the complement-coherent NAND class, the middle class-sum equations
and all Johnson seam equations are equivalent to

\[
 \boxed{s_a=1\quad(a\in\mathbb Z_C).}                 \tag{3.9}
\]

In words: the starting residues of the `C` long gaps are every residue
modulo `C`, exactly once.

#### Proof

The class sums say exactly `n_a=m` for every residue: multiplying the
physical index by two only permutes the `k` sheet positions above a fixed
residue.  Equation (3.8) then gives `s_(b-2)=s_(b-3)` for all `b`, so all
`s_a` are equal.  Their total is `C`, proving (3.9).

Conversely, (3.9) turns (3.8) into `n_b=n_(b-2)`.  Since `C` is odd in the
complement-coherent case, step two is transitive on `Z_C`; all `n_b` are
equal, and their total `mC` makes each one `m`.  Thus all class sums hold.

Compare two consecutive quotient columns.  Of the `m` zero states above
the first residue, precisely `m-1` take a gap-two step and therefore persist
as the same absent coordinate in the next column.  The unique special state
leaves, and the unique special predecessor from the preceding residue
enters.  These two coordinates cannot coincide: coincidence would put two
zeros at consecutive `d` positions, contradicting (3.3).  Hence the absent
`m`-sets, and therefore their complementary rank-`m+1` owners, differ by
exactly one exchange.  Every Johnson seam equation follows.  \(\square\)

This replaces 429 rank equations and 429 XOR-two equations at `k=15` by
one combinatorial statement about a cyclic gap word of length 3003.  It does
**not** enforce distinct middle or q1 necklace columns, physical residence,
or any deeper shadow.

## 4. What the symmetry buys

Complement coherence gives, for every `q>=0`,

\[
 \overline{\bigcup_{j=0}^{q}T_{i+j}}
   =\bigcap_{j=0}^{q+1}T_{i+s+j}.                     \tag{4.1}
\]

Consequently upper depth `q` and lower depth `q+1` have identical load
functions under complementation.  At `k=15`, upper `q1` and lower `q2` are
one gate, and more generally the entire upper tower is one shifted copy of
the lower tower.

The unit-voltage representation supplies an additional advantage: every
coordinate trace is a translate of `c`, so all-coordinate depth-`d`
residence is exactly the single requirement that every cyclic one-run of
`c` have length at least `d+1`.  Notice that this is a run condition in the
physical `c` order; the short one-runs in the permuted `d` order of Section
3 are not residence defects.

## 5. Exact finite target at k=15

The complement-coherent strict-spiral lane asks for a binary trace `c`
satisfying simultaneously:

1. the 429 class sums equal eight;
2. every quotient seam has Johnson XOR weight two;
3. middle and adjacent-intersection necklace columns are bijective;
4. (2.1), equivalently the local `d` constraints (3.3);
5. every cyclic one-run of `c` has length at least four;
6. the protected lower flag rows cover every required target;
7. the exact one-core, weighted quotient Hall, physical matching, safe cut,
   and literal verifier all pass.

By (4.1), upper cuts need not be imposed separately from the corresponding
lower rows inside this subclass.  A sound UNSAT result concerns only the
intersection of strict unit-voltage equivariance and complement coherence;
it does not rule out a non-equivariant carrier, a complement-paired
multi-component factor, or the original formula.
