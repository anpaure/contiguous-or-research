# Gate C fragment quota compiler and the reopened logarithmic scale

**Status (2026-08-22).**  Everything through the scale audit in Section 6 is
proved below.  In particular, the phase-refined fragment multihypergraph has
exact degree

\[
                 D_L=L\widehat D,
\]

the uniform fractional weighting has the ideal marginal at every controlled
rank, its maximum normalized pair codegree is at most `4/b^2`, and any
quota-balanced integral selection compiles to a word of length

\[
                 W+O(L)+O(Wg/L)+o(W).
\]

Taking

\[
  L=\left\lceil {c b\log b\over\log\log b}\right\rceil,
  \qquad 0<c<2,
  \qquad x={1\over\log b},
\]

makes both serialization and the edge-size-weighted pair parameter `o(1)`,
while the expected independently surviving labelled support is

\[
 W\widehat D x^L
   =\exp\bigl((2-c+o(1))b\log b\bigr).
\]

Thus the first-moment extinction obstruction from the previously considered
scale does not apply here.  This is not a matching theorem.  The still-open
step is a **dependent integral near-matching/quota rounding** which selects
the fragments while keeping aggregate nearby-rank overflow `o(W)`.  A large
expected residual support and a small pair parameter do not prove that step.

## 1. Words, parameters, and the atom chronology

Let `Omega` be a set of size `2b`, where

\[
                    b=2h+1\ge5,
 \qquad \mathcal V={\Omega\choose b},
 \qquad W=|\mathcal V|={2b\choose b}.                 \tag{1.1}
\]

A word is a finite sequence of subsets of `Omega`.  It realizes a nonempty
target if that target is the union of a nonempty consecutive interval of
letters.  In the constructions below most letters are singletons, so an
injective block of `s` consecutive emitted symbols realizes their `s`-set.

Choose a split

\[
                    \Omega=A\mathbin{\dot\cup}B,
                    \qquad |A|=|B|=b,                 \tag{1.2}
\]

and directed cyclic orders `alpha` on `A` and `beta` on `B`, each taken
modulo rotation.  Repeat the length-`b` type word

\[
                     B,A,B,A,\ldots,B,A,B.             \tag{1.3}
\]

At successive events of one type, emit successive symbols in the
corresponding cyclic order.  A pair of stream roots belongs to
`Z_b^2`.  Advancing by one whole type period changes that pair by

\[
                         (h,h+1)=(h,-h)\pmod b.         \tag{1.4}
\]

This vector has order `b`.  We retain as a label one of the `b` cosets in

\[
                 Q=\mathbb Z_b^2/\langle(h,h+1)\rangle. \tag{1.5}
\]

A **phase-refined labelled atom** is a label
`(A,alpha,beta,rho)` with `rho in Q`, together with the resulting cyclic
emission word

\[
                         w=(w_t)_{t\in\mathbb Z_{b^2}}. \tag{1.6}
\]

Changing the representative of `rho` only rotates this cyclic word by a
whole type period.  Since all cyclic starts will be retained, no count below
depends on that choice.

More explicitly, every coset has a unique representative of the form
\((\rho,0)\): the second coordinate of \((h,h+1)\) is invertible modulo
\(b\). Thus the quotient in (1.5) has exactly the \(b\) representatives
used in the finite verifier. Relabelling \(\Omega\) transports the split,
both cyclic orders, and this root-pair quotient, so it permutes the full
labelled family.

For `t in Z_(b^2)`, put

\[
                         C_t=\{w_t,\ldots,w_{t+b-1}\}. \tag{1.7}
\]

Indices in cyclic displays are taken modulo `b^2`.

### Lemma 1.1 (chronology and injectivity)

For every phase-refined atom:

1. the `b^2` sets `C_t` are distinct members of `mathcal V`;
2. the forward gap between consecutive emissions of any fixed coordinate is
   at least `2b-2`.

Consequently every emission block of length at most `2b-2` is injective.

#### Proof

Every length-`b` type window contains `h` events of type `A` and `h+1`
events of type `B`.  Its two parts are cyclic intervals of those respective
lengths.  If `(i_t,j_t)` are their two interval starts, then
`i_t+j_t=t+constant mod b`; advancing by one type period sends

\[
                         (i,j)\longmapsto(i+h,j-h).      \tag{1.8}
\]

Because `gcd(h,b)=1`, the `b` advances at a fixed time residue visit all
`b` pairs on the corresponding diagonal, and the `b` time residues give all
of `Z_b^2`.  Intersecting `C_t` with `A` and `B` recovers its two intervals,
so the `b^2` central sets are distinct.

Successive `A`-event gaps in (1.3) are `2,...,2,3`, and successive
`B`-event gaps are `2,...,2,1`.  A coordinate recurs after exactly `b`
events of its own type.  Among `b` consecutive `B`-event gaps there are at
most two gaps of size one, so their sum is at least `2b-2`; the `A` sum is
larger.  The last assertion follows because two positions in a block of
length at most `2b-2` are separated by at most `2b-3`.  \(\square\)

There are

\[
 \widehat N
   =bW((b-1)!)^2                                      \tag{1.9}
\]

phase-refined labelled atoms: choose `A`, the two directed cyclic orders,
and `rho`.  The labelled family is invariant under every permutation of
`Omega`.  Since each atom contains `b^2` distinct middle targets, its common
middle-target degree is

\[
 \boxed{\widehat D={\widehat N b^2\over W}
                    =b(b!)^2.}                         \tag{1.10}
\]

## 2. Full-atom pair profile

For two middle targets `S,T`, their Johnson distance is

\[
                         d(S,T)=|S-T|=|T-S|.            \tag{2.1}
\]

### Lemma 2.1 (exact normalized full-atom codegrees)

If `1<=d<b`, the number `widehat lambda_d` of phase-refined labelled atoms
containing a fixed pair at Johnson distance `d` satisfies

\[
 {\widehat\lambda_d\over\widehat D}
   ={4\min(d,b-d)\over {b\choose d}^2},
 \qquad \widehat\lambda_b=0.                           \tag{2.2}
\]

Its maximum over distinct pairs is exactly

\[
                         {4\over b^2},                  \tag{2.3}
\]

attained at `d=1` and `d=b-1`.

#### Proof

Fix one length-`h` cyclic interval in a `b=2h+1` cycle.  Among the `b`
intervals of that length, one is at Johnson distance zero and exactly two
are at each distance `1,...,h`.  The same is true for length `h+1` by
complementation.  Distances add across the disjoint shores.  Convolving the
two lists shows that, relative to one cell of an atom, the number of its
other cells at distance `d` is

\[
 n_d=4\min(d,b-d)\quad(1\le d<b),
 \qquad n_b=0.                                         \tag{2.4}
\]

There are `N_d=binom(b,d)^2` middle targets at distance `d` from a fixed
one.  Its stabilizer in the full symmetric group is transitive on them.
Double-counting `(atom,T)` with the atom containing the fixed target gives
`widehat D n_d=N_d widehat lambda_d`, proving (2.2).

For `u=min(d,b-d)=1`, (2.2) equals `4/b^2`.  If `2<=u<=h`, unimodality gives

\[
 {b\choose u}\ge {b\choose2}={b(b-1)\over2},
 \qquad {b\choose u}^2\ge ub^2,                        \tag{2.5}
\]

where the second inequality uses `u<=h=(b-1)/2`.  Hence (2.2) is at most
`4/b^2`.  \(\square\)

## 3. The labelled fragment multihypergraph

Fix

\[
                         1\le L\le {b^2\over2}.         \tag{3.1}
\]

For every phase-refined atom `C=(C_t)` and every labelled cyclic start
`a in Z_(b^2)`, define the central fragment edge

\[
             F(C,a)=\{C_a,C_{a+1},\ldots,C_{a+L-1}\}.  \tag{3.2}
\]

The labels `(C,a)` are retained even if two fragment sets coincide.  Let
`mathcal G_(b,L)` denote this labelled `L`-uniform multihypergraph on
`mathcal V`.

### Theorem 3.1 (exact degree and pair-codegree bound)

The number of labelled fragment edges is

\[
                         W\widehat D,                   \tag{3.3}
\]

and every middle target has exact degree

\[
 \boxed{D_L=L\widehat D.}                              \tag{3.4}
\]

If `Delta_2` is the maximum labelled codegree of two distinct middle
targets, then

\[
 \boxed{{\Delta_2\over D_L}
    \le {L-1\over L}{4\over b^2}
    \le {4\over b^2},
 \qquad {L\Delta_2\over D_L}\le {4L\over b^2}.}       \tag{3.5}
\]

#### Proof

There are `widehat N b^2=W widehat D` atom-start labels, proving (3.3).
In each phase-refined atom through a fixed middle target, exactly `L` cyclic
starts place it in (3.2).  Equation (1.10) gives (3.4).

Let \(N=b^2\), and suppose the two targets occur at positions whose forward
cyclic difference is \(q\in\{1,\ldots,N-1\}\). The exact number of
length-\(L\) cyclic fragments containing both is

\[
             (L-q)_+ + (L-(N-q))_+.                  \tag{3.6}
\]

For \(L\le N/2\), at most one summand is positive, and (3.6) is at most
\(L-1\). Thus a full atom containing two distinct targets contributes at
most \(L-1\) fragment starts containing both. For a pair at Johnson
distance \(d\),

\[
 \deg_{\mathcal G}(S,T)
                    \le(L-1)\widehat\lambda_d.          \tag{3.7}
\]

Divide by `D_L=L widehat D` and apply (2.3).  \(\square\)

The restriction \(L\le b^2/2\) is the range used later and makes the
single-summand cyclic-wrap argument literal. Formula (3.6) also shows
directly that the \(L-1\) bound remains true for every \(L<b^2\).

## 4. Exact fractional marginals at all controlled ranks

Fix an integer

\[
                         b<g\le2b-2.                    \tag{4.1}
\]

The linearization of a fragment label `(C,a)` is the singleton block

\[
 \mathsf B(C,a)=
  (\{w_a\},\{w_{a+1}\},\ldots,\{w_{a+L+g-2}\}),       \tag{4.2}
\]

of length `L+g-1`.  For every `1<=s<=g`, retain the `L` **designated
rank-`s` occurrence tokens**

\[
 T_s(C,a,j)=\{w_{a+j},\ldots,w_{a+j+s-1}\},
 \qquad 0\le j<L.                                      \tag{4.3}
\]

They are genuine `s`-sets by Lemma 1.1.  Extra windows of (4.2) are harmless
and are not included in the quota ledger.

### Theorem 4.1 (full-rank fractional fragment atlas)

Give every labelled fragment weight `1/D_L`.  Then:

1. every middle target has fragment-edge load one;
2. the total fragment weight is `W/L`;
3. for every `1<=s<=g` and every `s`-set `T`, its weighted designated-token
   load is exactly

\[
                         \boxed{{W\over {2b\choose s}}}. \tag{4.4}
\]

#### Proof

The first assertion is (3.4), and (3.3)--(3.4) give total weight `W/L`.
Every fragment supplies exactly `L` designated tokens at rank `s`.  Their
total weighted mass is therefore

\[
              {W\widehat D\,L\over L\widehat D}=W.     \tag{4.5}
\]

The labelled atom, phase, and start family is invariant under every
permutation of `Omega`, and the symmetric group is transitive on the
`binom(2b,s)` targets of rank `s`.  All loads are therefore equal, and
(4.5) gives (4.4).  \(\square\)

This is an exact simultaneous fractional statement.  It does not say that
one integral fragment selection realizes those marginals.

## 5. A self-contained fragment quota compiler

Let

\[
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil,
 \qquad g=b+H+2,
 \qquad \mathcal B=\{b-H,\ldots,b+H\}.                 \tag{5.1}
\]

For all sufficiently large `b`, (4.1) holds.  Assume also `g<=L<=b^2/2`
and put

\[
             t=\left\lceil{W\over L}\right\rceil,
 \qquad M=Lt,
 \qquad W\le M<W+L.                                   \tag{5.2}
\]

Choose an integral list `mathscr F` of `t` labelled fragments; repetitions
are allowed.  For `s in mathcal B` and `T in binom(Omega,s)`, let `a_s(T)`
be the number of designated tokens (4.3) equal to `T` in the selected list.
Then

\[
                         \sum_Ta_s(T)=M.                \tag{5.3}
\]

Put `N_s=binom(2b,s)`.  Since `N_s<=W<=M`, choose balanced positive integer
quotas

\[
 q_s(T)\in\left\{\left\lfloor{M\over N_s}\right\rfloor,
                         \left\lceil{M\over N_s}\right\rceil\right\},
 \qquad \sum_Tq_s(T)=M,                                \tag{5.4}
\]

as follows. Write \(M=qN_s+r_s\) with \(0\le r_s<N_s\), assign quota
\(q+1\) to any \(r_s\) targets, and quota \(q\) to all others. Since
\(M\ge N_s\), one has \(q\ge1\).

Define the one-sided overflow

\[
                         V_s=\sum_T(a_s(T)-q_s(T))_+.    \tag{5.5}
\]

### Lemma 5.1 (overflow pays for holes)

If `h_s=|{T:a_s(T)=0}|`, then

\[
                         \boxed{h_s\le V_s}.            \tag{5.6}
\]

#### Proof

The load and quota vectors have the same total, so

\[
 \sum_T(a_s(T)-q_s(T))_+
   =\sum_T(q_s(T)-a_s(T))_+.                            \tag{5.7}
\]

Every quota is at least one, and every hole contributes at least one to the
right side.  \(\square\)

### Theorem 5.2 (fragment quota compiler)

For every selected list and quotas as above, there is a word realizing all
nonempty subsets of `Omega` whose length is at most

\[
\boxed{
 W+L+\left({W\over L}+1\right)(g-1)
 +\sum_{s\in\mathcal B}V_s
 +\sum_{\substack{1\le s\le2b\\|s-b|>H}}{2b\choose s}.
}                                                       \tag{5.8}
\]

Consequently, if

\[
 L=o(W),\qquad {g\over L}=o(1),qquad
                     \sum_{s\in\mathcal B}V_s=o(W),    \tag{5.9}
\]

then

\[
 \nu(2b)\le W+O(L)+O(Wg/L)+o(W)=(1+o(1))W.             \tag{5.10}
\]

Since every word realizing all middle targets has length at least `W`, this
implies `nu(2b)=(1+o(1))W`.

#### Proof

For every selected fragment concatenate its linear block (4.2).  Every
designated token is realized by an interval wholly inside its own block.
Concatenation cannot destroy such a witness; intervals crossing block cuts
can only create additional witnesses.  No connector and no separate
rank-by-rank cut charge is needed.

The concatenated length is

\[
\begin{aligned}
 t(L+g-1)
   &=M+t(g-1)\\
   &<W+L+\left({W\over L}+1\right)(g-1).                \tag{5.11}
\end{aligned}
\]

By Lemma 5.1, at most `sum_(s in mathcal B)V_s` band targets are missing.
Append each of them as one set-valued letter.  Append also every nonempty
target outside the band which is still missing.  A one-letter interval
realizes each appended target, proving (5.8).

For completeness, if `X` is `Bin(2b,1/2)`, then

\[
 \Pr(|X-b|\ge H)\le2e^{-H^2/b}.                        \tag{5.12}
\]

Indeed,
`E exp(lambda(X-b))=(cosh(lambda/2))^(2b)<=exp(b lambda^2/4)`;
optimize separately in the two tails.  Also
`W>=2^(2b)/(2b+1)`.  Hence the last sum in (5.8) is at most

\[
 2^{2b+1}e^{-H^2/b}
 \le {2(2b+1)\over(2b)^2}W=o(W).                       \tag{5.13}
\]

Equations (5.9), (5.11), and (5.13) prove the upper bound.

For the lower bound, fix an ending position of an arbitrary word.  The
unions of intervals ending there form a chain under inclusion as the start
moves left, so at most one distinct middle target can first be assigned to
that ending position.  Assign every realized middle target to one witnessing
ending position.  There are `W` targets, hence the word has at least `W`
positions.  \(\square\)

At rank `b`, (5.4) consists of quota one everywhere and quota two at fewer
than `L` targets.  Thus `V_b=o(W)` forces an almost-packing, but Theorem 5.2
does not require literal disjointness.  A natural stronger sufficient input
would be a matching of `floor(W/L)` fragments, followed by at most one extra
fragment, selected jointly so that the off-middle quota overflows remain
`o(W)`.  Proving such a dependent near-matching and simultaneous quota
rounding is exactly the open integral step.

## 6. The reopened scale

Fix a constant

\[
                         0<c<2                           \tag{6.1}
\]

and set

\[
 L=\left\lceil{c b\log b\over\log\log b}\right\rceil,
 \qquad x={1\over\log b}.                              \tag{6.2}
\]

All logarithms are natural.  Since `H=o(b)` and `g=b+H+2=(1+o(1))b`,

\[
 {g\over L}
   =\left({1\over c}+o(1)\right){\log\log b\over\log b}
   =o(1),                                               \tag{6.3}
\]

and `L<=b^2/2` for all sufficiently large `b`.  Theorem 3.1 gives

\[
 {L\Delta_2\over D_L}
 \le {4L\over b^2}
 = (4c+o(1)){\log b\over b\log\log b}=o(1).            \tag{6.4}
\]

In particular, the two deterministic overhead terms in (5.10) are `o(W)`.

Now retain every middle target independently with probability \(x\), and
let \(Z_x\) be the number of **labelled** fragment edges all of whose
\(L\) distinct middle targets survive. Coincident unlabelled fragment
sets, if any, are counted with their label multiplicity. Since every
fragment has exactly \(L\) distinct targets, (3.3) gives

\[
                         \mathbb E Z_x=W\widehat D x^L. \tag{6.5}
\]

Here the labelled supply also has the exact simplification

\[
                  W\widehat D
  ={2b\choose b}\,b(b!)^2=b(2b)!.                       \tag{6.6}
\]

Stirling's formula therefore gives

\[
 \log(W\widehat D)
 =\log{2b\choose b}+\log b+2\log(b!)
 =2b\log b+(2\log2-2)b+O(\log b).                      \tag{6.7}
\]

Also `L log log b=c b log b+O(log log b)`.  Therefore

\[
\boxed{
 \log\mathbb E Z_x=(2-c+o(1))b\log b,
 \qquad
 \mathbb E Z_x=\exp(\Omega(b\log b)).}                 \tag{6.8}
\]

This is the exact threshold visible to the first moment: `c<2` gives
exponentially large expected support, while `c>2` gives extinction at this
scale.  At the literal borderline `c=2`, (6.7) gives
`log E Z_x=(2 log 2-2)b+O(log b)`, so the expected support also tends to zero.

The point of (6.3)--(6.8) is limited but real.  Separate fragment
linearization replaces the older aggregate seam requirement `L>>bH` by the
much weaker serialization requirement `L>>g`.  At (6.2), the first-moment
support is still enormous at residual density `1/log b`.  Nevertheless,
an expectation tending to infinity does not imply that a dependent residual
contains a useful matching, and (6.4) alone is not a growing-uniformity
matching theorem.  Nothing here proves the stopped residual degree floor,
the integral near-matching, or the simultaneous quota overflow bound (5.9).

## 7. Exact logical boundary

The proved implication is

\[
\boxed{
 \begin{array}{c}
 \text{an integral list of }\lceil W/L\rceil\text{ fragments with}\\
 \sum_{s=b-H}^{b+H}V_s=o(W)
 \end{array}
 \Longrightarrow
 \nu(2b)=(1+o(1)){2b\choose b}.
}                                                       \tag{7.1}
\]

Unconditional inputs proved in this note are the literal atom chronology,
the exact phase-refined degree, the full pair profile, exact fragment
regularity, the pair-codegree bound, exact all-rank fractional marginals,
the quota-to-hole identity, the serialization bound, and the scale/support
audit.  The antecedent of (7.1) remains open.  It must be obtained by a
correlated construction; independent representatives, fractional symmetry,
and pair-codegree smallness do not perform the required rounding.
