# Gate C: exact microbank-orbit codegrees and the growing-rank boundary

**Status (2026-08-22).**  Every assertion through Section 10 is proved.
The result does not prove a near-factor.  It identifies exactly what the
middle and three-rank coordinate-orbit hypergraphs contribute and why their
pair-codegree profiles are not, by themselves, growing-uniformity matching
theorems.

Let `b` be sufficiently large and odd, let

\[
 n=2b,\qquad W={2b\choose b},\qquad q=b(b-1),
\]

and retain the coherent FIFO tours and tunable microbanks from
`MATH_THEOREM_GATE_C_TUNABLE_MICROBANK_AND_FACTOR_PACKET_20260822.md`.
The main new conclusions are these.

1. A tunable microbank may be chosen so that targets belonging to two
   different states have Johnson distance in a fixed linear band.
2. For the orbit hypergraph of that microbank, the degree and every
   Johnson-distance pair-codegree have exact double-counting formulas.
3. Its largest normalized pair-codegree is attained at Johnson distance
   one and is exactly

   \[
   \boxed{\delta_b={b^2-5\over2b^2(b-1)}
          ={1+o(1)\over2b}.}                         \tag{0.1}
   \]

4. One can choose the balanced one-factorization packet with the same
   separation property between distinct constituent banks.  Its orbit has
   the same exact maximum (0.1).
5. The edge sizes are `2^{o(b)}`, but their product with (0.1) tends to
   infinity.  Thus neither a fixed-uniformity nibble nor a theorem using
   only regularity and `Delta_2/d=o(1)` yields a near-factor.  The exact
   remaining middle-only assertion is a hereditary packet-availability or
   equivalent cluster-aware switching theorem.
6. Restoring the `b` omitted boundary starts completes every state tour to
   a band-clean cyclic word of length `b^2`.  This removes the raw
   `Theta(W)` serialization loss.  The remaining physical issues are a
   near-capacity matching of completed three-rank packets and aggregate
   coverage at the other band ranks.
7. The distinct all-band support of one completed tour is explicit, and a
   completed factor packet can be made internally disjoint throughout the
   band.  Every band rank has sufficient scalar capacity; what remains is
   correlated cross-packet coverage.

## 1. Orbit incidence is exactly the internal distance distribution

For `A,B in (Omega choose b)`, write

\[
 d_J(A,B)=|A\setminus B|=|B\setminus A|.
\]

For a fixed target set `E subseteq (Omega choose b)` of size `k`, put

\[
 N_j(E)=|\{(A,B)\in E^2:A\ne B,\ d_J(A,B)=j\}|,
 \qquad v_j={b\choose j}^2.                           \tag{1.1}
\]

Let `O(E)={pi E:pi in S_(2b)}` be the simple orbit, and let
`L=|O(E)|`.  Regard it as a `k`-uniform hypergraph on the `W` middle
targets.

### Proposition 1.1 (exact orbit degrees)

Every vertex has degree

\[
                         d={Lk\over W}.               \tag{1.2}
\]

If `A ne B` and `d_J(A,B)=j`, their codegree is

\[
                         d_2(j)={L N_j(E)\over Wv_j}, \tag{1.3}
\]

and hence

\[
 \boxed{{d_2(j)\over d}={N_j(E)\over k{b\choose j}^2}.} \tag{1.4}
\]

#### Proof

The coordinate group is transitive on middle targets and on ordered
pairs at each fixed Johnson distance.  Double count incidences of orbit
edges with one vertex to obtain (1.2), and incidences with an ordered
distance-`j` pair to obtain (1.3).  Passing from the permutation multiorbit
to the simple orbit divides both counts by the same setwise stabilizer of
`E`.  Division proves (1.4). \(\square\)

There is also a useful universal upper bound when `E` lies in one
defect-one stratum.  Put `a=b-j`.  Appendix I gives the common pairing
degree

\[
 \Lambda_j=a!j!\left[
 aj(aj-1)+{a(a-1)+j(j-1)\over4}\right]               \tag{1.5}
\]

and the one-target pairing degree

\[
                         D_1={b!b(b-1)\over4}.         \tag{1.6}
\]

For one fixed pairing `P`, its automorphism group is transitive on the
defect-one stratum.  Double counting `(P,A,B)` therefore shows that a
fixed defect-one `A` has exactly

\[
              v_j{\Lambda_j\over D_1}                 \tag{1.7}
\]

defect-one distance-`j` neighbors relative to `P`.  Consequently every
`E` in that stratum satisfies

\[
 {N_j(E)\over |E|v_j}\le {\Lambda_j\over D_1}
 ={4aj(aj-1)+a(a-1)+j(j-1)
   \over b(b-1){b\choose j}}.                         \tag{1.8}
\]

For `1<=j<=b-1`, the maximum of the right side is

\[
                         {5(b-2)\over b^2},            \tag{1.9}
\]

at `j=1,b-1`.  This recovers the `O(1/b)` outer codegree bound, but
Sections 2--4 determine the actual leading constant for a suitably chosen
microbank.

## 2. A separated balanced subcode

Fix a pairing and pair order.  Let `F` be the `q` middle flags.  For each
of the three targets attached to a flag `f`, extend its chronology vector
from the split pair coordinates to an arbitrary vector
`c_(r,f) in F_2^b`, where `r in {b-1,b,b+1}`, and put

\[
 \mathcal W=\{c_{r,f}+c_{r',g}:r,r'\in\{b-1,b,b+1\},\ f,g\in F\},
 \qquad |\mathcal W|\le9q^2.                         \tag{2.1}
\]

Let `C_+` be the collision-avoiding code of dimension `d=b-rho` and dual
distance greater than `H` used in the tunable-microbank theorem.  Fix

\[
                         \gamma={1\over20}.            \tag{2.2}
\]

For an integer `s`, define

\[
 \epsilon_b=(2^s-1)9q^2 2^\rho
 {2\sum_{i=0}^{\lfloor2\gamma b\rfloor}{b\choose i}\over2^b}. \tag{2.3}
\]

### Theorem 2.1 (balanced affine separation)

If

\[
 V_H2^{-s}+{2^s-1\over2^d}+\epsilon_b<1,
 \qquad V_H=\sum_{i=1}^H{b\choose i},                 \tag{2.4}
\]

then `C_+` contains an `s`-dimensional subcode `C_-` such that

\[
 C_-\cap\mathcal B=\varnothing,\qquad
 d(C_-^\perp)>H,                                      \tag{2.5}
\]

and, for every `0 ne h in C_-` and every `w in \mathcal W`,

\[
             2\gamma b\le \operatorname {wt}(h+w)
                       \le(1-2\gamma)b.               \tag{2.6}
\]

At the live value `H=ceil(sqrt(2b log(2b)))`, one may take

\[
                 s=\left\lceil\log_2(8V_H)\right\rceil=o(b). \tag{2.7}
\]

#### Proof

Choose independent uniform `X_1,...,X_s` from `C_+`.  The probability
that some nonzero word of weight at most `H` annihilates all generators is
at most `V_H2^{-s}`.  The probability that the generators are dependent
is at most `(2^s-1)/2^d`.

Fix a nonzero coefficient vector `u in F_2^s` and `w in \mathcal W`.
The sum `X_u=sum u_iX_i` is uniform on `C_+`.  Since
`|C_+|=2^(b-rho)`, the probability that `X_u+w` has weight below
`2 gamma b` or above `(1-2 gamma)b` is at most

\[
 2^\rho{2\sum_{i=0}^{\lfloor2\gamma b\rfloor}{b\choose i}\over2^b}.
\]

A union bound over `u ne 0` and `w` gives (2.3).  Under (2.4), some
sample avoids all three bad events.  Its span is the required `C_-`.
Containment in `C_+` gives collision avoidance.

For (2.7), `V_H2^{-s}<=1/8`, while `s=o(b)` by the standard entropy
bound on `V_H`.  The dependence term is `o(1)`.  Finally, with `h_2`
the binary entropy function,

\[
 \sum_{i\le2\gamma b}{b\choose i}
 \le(b+1)2^{h_2(2\gamma)b},\qquad h_2(1/10)<1,
\]

so (2.3) is `2^{-(1-h_2(1/10))b+o(b)}=o(1)`.  Thus (2.4) holds for
large `b`. \(\square\)

Every coset of `C_-` is still exactly `H`-wise uniform, and still lies
inside one collision-free parent coset.  Thus this strengthening loses
none of the conclusions of the tunable-microbank theorem.

### Corollary 2.2 (cross-state Johnson separation)

Let `E` be the middle support of a coset microbank from Theorem 2.1.  If
two targets of `E` arise from different states, then, for all large `b`,

\[
                         \gamma b\le d_J(A,B)
                                      \le(1-\gamma)b. \tag{2.8}
\]

#### Proof

Let the two flags be `f,g`, the state difference be `0 ne h in C_-`,
and let `R` be the union of their empty and doubled pair indices, so
`|R|<=4`.  On every pair outside `R`, both targets are split and their
chosen members disagree exactly where `h+c_(b,f)+c_(b,g)` is one.  If
`u` is the number of such disagreements, then

\[
 u\le d_J(A,B)\le u+4,
 \qquad |u-\operatorname {wt}(h+c_{b,f}+c_{b,g})|\le4. \tag{2.9}
\]

Equations (2.6) and (2.9), with the factor-two margin in (2.6), give
(2.8) for sufficiently large `b`. \(\square\)

## 3. Exact same-tour tails

Put `b=2r+1`.  Fix one state.  Swapping the two labels inside each pair
is an isometry, so assume the initial state is zero.  Index a middle flag
by its ordered empty and doubled pair `(e,d)`.  Use representatives
`0,...,b-1`, and let `(e,d)` also denote the open forward cyclic arc.
On every split pair `j`, the selected member has bit

\[
 \chi_{e,d}(j)
 =e+\mathbf1_{\{j<e\}}+\mathbf1_{\{j\in(e,d)\}}\pmod2. \tag{3.1}
\]

Indeed, before packet `e`, pair `j` has been flipped
`e-1_(j<e)` times; the packet then flips precisely the pairs in the open
forward arc before reaching `d`.

Formula (3.1) gives the following complete endpoint count.  The entries
are numbers of **unordered** flag pairs in one state.

\[
\begin{array}{c|c|c}
\text{signature relation}&d_J=1&d_J=b-1\\ \hline
\text{same empty pair}&b(b-2)&0\\
\text{same doubled pair}&b r(r-1)&0\\
\text{reversed empty/doubled pairs}&0&b\\
\text{exactly one cross identification}&0&b(b-1)\\
\text{all other relations}&0&0.
\end{array}                                             \tag{3.2}
\]

For completeness, here is the direct count behind the first two entries.
With one empty pair fixed, write the doubled positions as forward gaps
`1<=k<l<=b-1`.  Equation (3.1) gives distance `l-k`, so precisely the
`b-2` consecutive pairs have distance one.  With one doubled pair fixed,
write the two backward gaps as `k,l in {1,...,2r}`.  Equation (3.1) gives
distance one when `k` and `l` have the same parity, and distance `b-2`
otherwise.  The two parity classes have size `r`, giving
`2(r choose 2)=r(r-1)` pairs.

For distance `b-1`, reversed flags `(e,d),(d,e)` work exactly when the
forward gap from `e` to `d` is `2` or `b-2`.  The two orientations describe
the same `b` unordered pairs.  If there is exactly one cross identification,
orient the flags as `(e,d),(d,g)` and put `k=[d-e]_b`.  Direct substitution
in (3.1) says that the unique choice is

\[
 g=d+1\pmod b\quad(k\text{ odd}),\qquad
 g=d-1\pmod b\quad(k\text{ even}).                   \tag{3.2a}
\]

It never equals `e`; hence every one of the `b(b-1)` oriented choices
`(e,d)` gives one unordered pair with exactly one cross identification.
All remaining signature relations have distance at most `b-2`.  Finally,
two defect-one sets at distance one must either move the empty pair while
keeping the doubled pair, or move the doubled pair while keeping the empty
pair; hence the first two rows exhaust distance one.  This proves the
whole table.

In particular, the ordered counts in one state are

\[
 \boxed{N_1^{\rm tour}={b(b^2-5)\over2},\qquad
        N_{b-1}^{\rm tour}=2b^2.}                     \tag{3.3}
\]

There are no complementary same-state targets.  One can also see this
without the table: complementary signatures would have to be `(e,d)` and
`(d,e)`.  Summing their split-bit differences from (3.1) over
`j notin {e,d}` gives even parity, whereas complementarity would require
`b-2` disagreements, which is odd.

## 4. The exact maximum orbit codegree

Let `c=2^s` and let `E` be a separated microbank support.  Then

\[
                         k=|E|=qc.                    \tag{4.1}
\]

By Corollary 2.2, every pair at distance outside the central interval in
(2.8) belongs to one state.  Therefore (3.3) gives

\[
 {N_1(E)\over kv_1}
 ={c b(b^2-5)/2\over cb(b-1)b^2}
 =\boxed{{b^2-5\over2b^2(b-1)}},                     \tag{4.2}
\]

and

\[
                         {N_{b-1}(E)\over kv_{b-1}}
 ={2\over b(b-1)},\qquad N_b(E)=0.                   \tag{4.3}
\]

For every other tail distance `2<=j<=b-2`, a target has at most `q-1`
partners in its own state, whence

\[
 {N_j(E)\over kv_j}
 \le {q-1\over{b\choose j}^2}
 \le {q-1\over{b\choose2}^2}=O(b^{-2}).              \tag{4.4}
\]

For a central distance, the trivial bound `N_j(E)<=k(k-1)` and
`k=2^{o(b)}` give

\[
 {N_j(E)\over kv_j}
 \le {k\over{b\choose\lfloor\gamma b\rfloor}^2}
 =2^{-\Omega(b)}.                                     \tag{4.5}
\]

Equations (4.2)--(4.5) prove the following.

### Theorem 4.1 (exact microbank-orbit maximum)

For all sufficiently large odd `b`, the full coordinate orbit of a
separated balanced microbank is regular and has

\[
 \boxed{\max_{A\ne B}{d(A,B)\over d(A)}
       ={b^2-5\over2b^2(b-1)},}                       \tag{4.6}
\]

attained exactly at Johnson distance one at the level of distance
classes.  Its complementary codegree is zero.

## 5. A separated one-factorization packet

The one-factorization packet can be chosen with the same tail separation.
Choose the separated template of Section 2 on every factor and transport
the templates by independent uniform automorphisms of their factors, as
in the balanced-packet theorem.

For a fixed pairing, a fixed accessible middle target lies in its random
transported microbank with probability

\[
                         {c\over2^{b-2}}.              \tag{5.1}
\]

For a fixed middle target `A`, the number of middle targets `B` with
`d_J(A,B)<gamma b` or `d_J(A,B)>(1-gamma)b` is at most

\[
 T_\gamma=2\sum_{j=0}^{\lfloor\gamma b\rfloor}{b\choose j}^2
 \le 2(b+1)^2 2^{2h_2(\gamma)b}.                     \tag{5.2}
\]

Conditioning on the first bank, the expected number of tail pairs between
two different factor banks is therefore at most

\[
                         mT_\gamma {c\over2^{b-2}},
 \qquad m=qc.                                          \tag{5.3}
\]

There are fewer than `2b^2` factor pairs.  Since

\[
                         2h_2(1/20)<1,
\]

and `c=2^{o(b)}`, the sum of (5.3) over all pairs is `o(1)`.  Markov's
inequality shows that with probability `1-o(1)` there is no such cross-bank
tail pair.  The independent estimate in the balanced-packet theorem says
that with probability `1-o(1)` there is also no collision at any of the
three central ranks.  Hence both properties hold simultaneously.

Let `E_*` be the middle support of such a packet and put

\[
                         K=|E_*|=(2b-1)m.              \tag{5.4}
\]

All distance-one and distance-`b-1` pairs lie inside one state of one
constituent bank.  Thus (3.3) scales by `2b-1`, while division by `K`
cancels that factor.  The tail bound (4.4) and central bound (4.5) are
unchanged with `k` replaced by `K=2^{o(b)}`.  We have proved:

### Theorem 5.1 (exact packet-orbit maximum)

The balanced exact-two-design packet may be chosen so that its constituent
banks are jointly target-disjoint at ranks `b-1,b,b+1`, every middle pair
from distinct constituent banks has Johnson distance in
`[gamma b,(1-gamma)b]`, and

\[
 \boxed{\max_{A\ne B}{d_{\mathcal O(E_*)}(A,B)
                             \over d_{\mathcal O(E_*)}(A)}
       ={b^2-5\over2b^2(b-1)}.}                       \tag{5.5}
\]

Because every packet support is an exact `2`-design, the residual left by
any matching of packet supports is also an exact `2`-design.

## 6. Why this still does not give a middle near-factor

At (2.7), `c=2^s` tends to infinity faster than every fixed power of `b`.
For a microbank and a packet respectively,

\[
 k\delta_b\sim {b-1\over2}c\longrightarrow\infty,
 \qquad
 K\delta_b\sim b(b-1)c\longrightarrow\infty.         \tag{6.1}
\]

Thus the normalized codegree tends to zero, but not on the growing edge
rank scale.

This distinction is logically necessary.  The line hypergraph of a
projective plane of order `Q` is `(Q+1)`-uniform and `(Q+1)`-regular, has
pair-codegree one and hence normalized codegree `1/(Q+1)=o(1)`, but every
two edges meet and its matching number is one.  Therefore exact regularity
and `Delta_2/d=o(1)` do not imply an almost-perfect matching when the edge
rank grows.  The projective-plane example is not asserted to occur inside
the packet orbit; it proves that the verified degree/codegree data alone
cannot be used as a theorem.

The elementary one-shot alteration has the same limitation.  In a
`K`-uniform `d`-regular hypergraph, an edge has at most `Kd` conflicting
edges by the union bound.  Sampling edges at probability `Theta(1/(Kd))`
and retaining isolated sampled edges gives only a guaranteed
`Theta(1/K)` fraction of the vertices in one bite.  Iterating this estimate
requires a survival-conditioned residual theorem; the time-zero orbit
identities (1.2)--(1.4) do not provide one.

There is an exact packet-specific way to state the missing middle theorem.
For a residual `R subseteq (Omega choose b)`, let

\[
 \mathcal A(R)=\{F\in\mathcal O(E_*):F\subseteq R\}.  \tag{6.2}
\]

If there is a sequence `epsilon_b -> 0` such that every residual produced
by deleting a matching of packet supports, whenever
`|R|>=epsilon_bW`, satisfies

\[
                         \boxed{\mathcal A(R)\ne\varnothing,} \tag{6.3}
\]

then greedy continuation gives a packet matching covering
`W-o(W)` middle targets.  The proof is immediate: append an available
packet until (6.3) first ceases to apply.  Such residuals are automatically
exact `2`-designs, but no theorem here derives (6.3) from that fact.

Equation (6.3), or an equivalent switching/absorption statement valid
along the actual residual trajectory, is the precise missing positive
input.  The raw orbit has no volume obstruction, complementary codegree,
or pair-balance defect.  Its unresolved issue is hereditary availability
through the structured distance-one tour clusters.  Even a proof of
(6.3) would settle only the middle near-factor; the physical all-offset
repair in Gate `C_F` would remain separate.

## 7. The physically relevant three-rank orbit

A middle matching does not prevent two different packets from colliding at
ranks `b-1` or `b+1`.  The correct first physical lift is therefore an
augmented orbit.  Put

\[
 W_1={2b\choose b-1}={2b\choose b+1}={b\over b+1}W.   \tag{7.1}
\]

Let `E_-,E_0,E_+` be the three target supports of one separated balanced
packet.  Each has size

\[
                         K=(2b-1)qc.                  \tag{7.2}
\]

Take the full coordinate orbit of

\[
                         E^\star=E_-\sqcup E_0\sqcup E_+              \tag{7.3}
\]

on the disjoint union of the three rank layers.  Write `L_star` for the
number of simple orbit edges.  The three one-vertex degrees are exactly

\[
 d_0={L_\star K\over W},\qquad
 d_-=d_+={L_\star K\over W_1}={b+1\over b}d_0.        \tag{7.4}
\]

### Proposition 7.1 (exact fractional capacity)

The augmented orbit hypergraph has fractional matching number

\[
                         \boxed{\nu^\star={W_1\over K}.}               \tag{7.5}
\]

Consequently an integral matching of size `(1-o(1))W_1/K` covers
`W-o(W)` middle targets and all but `o(W)` targets in both adjacent
layers.

#### Proof

Give every orbit edge weight `1/d_-`.  Every adjacent vertex then has
load one, while every middle vertex has load
`d_0/d_-=b/(b+1)<1`; hence this is a fractional matching of total mass
`L_star/d_-=W_1/K`.  Conversely, summing the fractional constraints over
either adjacent layer shows that every fractional matching has total mass
at most `W_1/K`, because each edge uses exactly `K` vertices there.  This
proves (7.5).

An integral matching of the stated size covers `W_1-o(W)` vertices in
each layer.  In the middle layer this leaves

\[
 W-W_1+o(W)={W\over b+1}+o(W)=o(W),                  \tag{7.6}
\]

and the adjacent residuals are `o(W)`. \(\square\)

Thus the smaller adjacent layers create no coefficient obstruction: their
exact capacity already differs from the middle layer by only `o(W)`.

### 7.2 Exact augmented pair formula

For `r,s in {b-1,b,b+1}` and an intersection size `t`, let

\[
 a_{r,s,t}=|\{(A,B)\in E_r\times E_s:
                 A\ne B,\ |A\cap B|=t\}|             \tag{7.7}
\]

and

\[
 B_{r,s,t}={r\choose t}{2b-r\choose s-t}.             \tag{7.8}
\]

The same orbit double count as Proposition 1.1 gives, for a fixed ordered
ambient pair of this type,

\[
 \boxed{{d(A,B)\over d(A)}={a_{r,s,t}\over K B_{r,s,t}}.}             \tag{7.9}
\]

This identity includes same-rank, cross-rank, nested, and near-complement
pairs.  In particular, each flag transition already gives nested
middle--lower and middle--upper pairs, so these links cannot be ignored.

### 7.3 Separation at all three ranks

Theorem 2.1 used all `3q` chronology forms in (2.1).  If two targets from
different states have ranks `r,s`, put

\[
 u=|A\setminus B|,\quad v=|B\setminus A|,\quad
 u'=|A\cap B|,\quad v'=|\Omega\setminus(A\cup B)|.  \tag{7.10}
\]

Outside at most six exceptional pair indices, a disagreement of split
bits contributes to both `u,v`, and an agreement contributes to both
`u',v'`.  Equation (2.6), with its factor-two margin, therefore gives

\[
                         \min(u,v,u',v')\ge\gamma b   \tag{7.11}
\]

for all sufficiently large `b`.

The random-transport proof of Theorem 5.1 can also be run simultaneously
over the nine ordered rank pairs.  For a fixed rank-`r` target, the number
of rank-`s` targets for which one of the four quantities in (7.10) is below
`gamma b` is at most

\[
                         Cb^2 2^{2h_2(\gamma)b}.       \tag{7.12}
\]

Every fixed accessible target belongs to a random transported constituent
bank with probability at most `2bc/2^b`, by the four orbit ratios in the
balanced-packet theorem.  Multiplying (7.12) by the `3m` targets in the
first bank, by fewer than `2b^2` bank pairs, and by `2bc/2^b` gives

\[
             2^{-(1-2h_2(\gamma))b+o(b)}=o(1).        \tag{7.13}
\]

Hence the packet may be chosen so that every pair of targets in different
constituent banks satisfies (7.11), while retaining the three-rank
collision avoidance and exact two-design conclusion already proved.

### 7.4 The augmented maximum is asymptotically `2/b`

It remains to count the same-state tail.  Write one state's attached
targets as `L_f,M_f,U_f`.  Direct substitution of (3.1), together with
`L_f=M_f intersection M_(f+1)` and `U_f=M_f union M_(f+1)` (where a
packet boundary middle window is not retained), gives

\[
\begin{aligned}
 |\{(L,M):L\subset M\}|
 &=|\{(M,U):M\subset U\}|=b(2b-3),\\
 |\{(L,U):L\subset U\}|&={b(7b-11)\over2},\\
 N_1(L)&={q(b+3)\over2},\\
 N_1(M)&=N_1(U)={b(b^2-5)\over2}.
\end{aligned}                                           \tag{7.14}
\]

All counts are ordered except that the inclusion symbol already fixes the
two ranks.  For the first line, every nonboundary transition intersection
lies in its two adjacent retained middle windows, while each of the `b`
packet-boundary intersections lies in only one; this gives
`2(q-b)+b=b(2b-3)`.  The other lines follow from the same empty/doubled
signature check used in (3.2).  More generally, put

\[
 \sigma(A,B)=\min(u,r-u)+\min(v,2b-r-v).              \tag{7.15}
\]

The complete cases with `sigma<=2` obtained from those signatures have
the following two maxima:

\[
\begin{array}{c|c|c}
\sigma&\text{maximum partners per target, averaged over one state}
      &\text{smallest ambient }B_{r,s,t}\\ \hline
0&0&1\\
1&(2b-3)/(b-1)&b\\
2&(b+3)/2&b(b-1)/2.
\end{array}                                             \tag{7.16}
\]

The `sigma=1` maximum is the middle-rooted nested pair in the first line
of (7.14).  The `sigma=2` maximum is the lower-rank Johnson adjacency in
the third line.  Complementary targets do not occur; the near-complement
cases are included in (7.16).

For `3<=sigma<gamma b`, separation says the pair is in one state, so it
has at most `q-1` partners.  Binomial unimodality in the nine choices of
`r,s` gives

\[
 B_{r,s,t}\ge {b^2(b-1)\over2},qquad
 {q-1\over B_{r,s,t}}\le {2\over b}.                 \tag{7.17}
\]

For `sigma>=gamma b`, (7.8) is `2^{Omega(b)}` uniformly, whereas
`K=2^{o(b)}`; the trivial internal-pair bound is exponentially smaller
than `1/b`.  Equations (7.9), (7.14)--(7.17) prove:

### Theorem 7.2 (three-rank orbit codegree scale)

For the separated augmented packet orbit,

\[
 \boxed{
 {2b-3\over b(b-1)}
 \le \max_{A\ne B}{d(A,B)\over d(A)}
 \le {2\over b}.}                                    \tag{7.18}
\]

The lower bound is exact for a middle target and one of its nested
adjacent-rank target classes.  Thus the maximum normalized codegree is
`(2+o(1))/b`.

The augmented edge rank is `3K`, and

\[
 3K\max_{A\ne B}{d(A,B)\over d(A)}=\Theta(K/b)\to\infty.             \tag{7.19}
\]

Consequently the three-rank lift remains outside every inference justified
only by fixed edge rank or by a pair-codegree condition on the natural
`edge rank times normalized codegree` scale.  Equations (7.4), (7.5), and
(7.18) do not prove

\[
                         \boxed{\nu(\mathcal H^\star)
                         =(1-o(1)){W_1\over K}.}       \tag{7.20}
\]

They reduce the adjacent-rank collision problem exactly to (7.20).  A
proof still needs a packet-specific residual switch, absorber, or
survival-conditioned availability theorem; a middle-only matching cannot
substitute for it.

## 8. Serialization and the remaining all-offset repair

Suppose (7.20) is proved and let `R` packets be selected.  The number of
retained core starts and the number of coherent tours are

\[
 M=RK=W-o(W),\qquad
 T=R(2b-1)c={M\over q}.                               \tag{8.1}
\]

If every tour could be used as one physical fragment, the compiler bridge
charge would be

\[
                         gT={gM\over q}=O(W/b)=o(W).   \tag{8.2}
\]

More generally, if repair splits each tour into an average of `f_b`
fragments, then

\[
                         gt={gf_bM\over q};            \tag{8.3}
\]

since `g=(1+o(1))b` and `q=(1+o(1))b^2`, this is `o(W)` exactly whenever
`f_b=o(b)`.  The raw internal-flag ordering does **not** meet this bound:
its `b-1` retained flags in each packet are separated from the next packet
by an omitted boundary start, so it has `b` runs per tour.  Taking
`f_b=b` in (8.3) gives a `Theta(W)` bridge charge.  Thus merely linearizing
the internal flags does not serialize the construction at coefficient one.

What (7.20) would already prove is

\[
 h_b={W\over b+1}+o(W)=o(W),\qquad
 h_{b-1}+h_{b+1}=o(W).                                \tag{8.4}
\]

It proves nothing about the other `2H-2` ranks in the compiler band.  The
raw coherent tour was defined and collision-separated only through its
attached ranks `b-1,b,b+1`; it is not a theorem that every longer band
window is clean or that different selected tours have distinct targets at
those offsets.

The exact post-packing serialization gate is therefore:

* delete `o(W)` total core starts;
* split the surviving tours into `t` physical `H`-fragments with
  `t=o(W/b)`, equivalently average fragmentation `f_b=o(b)`;
* make every designated band window clean; and
* leave aggregate holes `o(W)` over all ranks `b-H,...,b+H`.

No assertion above proves this repair.  Gate `C_F` therefore has two
separate live parts even after the microbank refinement:

1. the augmented packet packing theorem (7.20), which simultaneously
   handles middle and adjacent-rank collisions at their exact capacity;
2. the all-offset repair with the sharp serialization budget (8.3).

Proving only the middle orbit matching (6.3) leaves both issues unresolved.

## 9. Completing the omitted boundary starts

There is, however, an exact repair of the raw serialization defect.  Keep
the boundary window `C_(s,b)=C_(s+1,0)` after every packet as an additional
core start.  One state now supplies a cyclic singleton word of length
`b^2`, with `b^2` core starts rather than `q=b(b-1)`.

### Lemma 9.1 (the completed word is automatically band-clean)

In the completed cyclic word, the complete inventory of forward gaps
between consecutive occurrences of the same ground coordinate is

\[
\begin{array}{c|c}
\text{gap}&\text{multiplicity}\\ \hline
2b-2&b(b-2)\\
2b-1&b\\
4b-3&b.
\end{array}                                             \tag{9.1}
\]

Consequently every cyclic interval of length at most `2b-2` has distinct
letters.  Since the live `H` satisfies `H<=b-2`, every window of length
`b-H,...,b+H` is clean.

#### Proof

Number packets and pair indices by `s,j in {0,...,b-1}` and output
positions by `1,...,b^2`.  Packet `s` emits the pair indices

\[
                         s+1,s+2,\ldots,s-1,s\pmod b.
\]

Hence the occurrence of pair `P_j` in packet `s` is at

\[
 \tau_s(j)=s(b-1)+j+b\mathbf 1_{\{s\ge j\}}.          \tag{9.1a}
\]

Successive pair occurrences have gap `b-1`, except from packet `j-1` to
packet `j`, where the gap is `2b-1` (with indices read cyclically).  At
every nonspecial packet the selected member of `P_j` flips, whereas at its
special packet it is retained.  Thus the emitted ground labels alternate
except across this unique long pair gap, where the same label occurs
twice.  The repeated label therefore has one same-label gap `2b-1`; the
other label has one gap

\[
                         (b-1)+(2b-1)+(b-1)=4b-3;
\]

the remaining `b-2` same-label gaps for this pair equal `2b-2`.  Summing
over the `b` pairs proves (9.1).  The result is independent of the initial
state, which only exchanges the two labels within a pair.  A word interval
of length `ell` spans only `ell-1` cyclic position gaps, so
`ell<=2b-2` cannot contain a repeated coordinate. \(\square\)

Write `L_i,M_i,U_i` for the length-`b-1,b,b+1` targets at all `b^2`
completed starts.  A direct FIFO signature check shows that, for one
state, each of the three families is separately collision-free.  Boundary
middle targets are transversals of the pairing; all other middle targets
are the previous defect-one targets.

### 9.2 A completed separating code

There are `3b^2` affine target forms.  For two forms of the same rank,
equality first requires compatible pair-occupancy signatures and then fixes
the state difference on every pair split in both forms.  The union of their
exceptional pair indices has size at most six, so an ordered form pair
creates at most `2^6` candidate differences.  Thus the completed collision
set `B_circ` satisfies

\[
                         |\mathcal B_\circ|\le576b^4. \tag{9.2}
\]

Set

\[
 \rho_\circ=\lceil\log_2(4\cdot576b^4)\rceil.         \tag{9.3}
\]

The random-linear-map proof of the balanced separating-code theorem,
with (9.2) in place of the old collision bound, gives a code
`C_(+,circ)` of codimension `rho_circ` which avoids `B_circ` and whose dual
distance exceeds `H`.  The balanced affine-separation proof of Section 2
then gives an `s`-dimensional subcode `C_(-,circ)` with

\[
 s=\lceil\log_2(8V_H)\rceil=o(b),\qquad c=2^s,        \tag{9.4}
\]

and the same cross-state linear separation at all three ranks.  Hence
every coset is a completed microbank of `c` full tours, containing exactly

\[
                         m_\circ=b^2c                 \tag{9.5}
\]

distinct targets at each of ranks `b-1,b,b+1`.

### 9.3 A completed one-factorization packet

The cross-pairing random-transport proof also survives completion.  Every
accessible completed target has at most three exceptional pairing edges.
Thus for two different factors their common accessible support at one of
the three ranks is still at most `Cb^C2^(b/2)`.  A fixed target belongs to
a random transported completed bank with probability at most

\[
                         {2bc\over2^b}.                \tag{9.6}
\]

The union bound is therefore `2^{-3b/2+o(b)}` over a bank pair and remains
`o(1)` over the one-factorization.  The tail-separation estimate (7.13)
is unchanged.  We obtain `2b-1` jointly three-rank-disjoint completed
banks, one on each factor, with

\[
                         K_\circ=(2b-1)b^2c            \tag{9.7}
\]

targets at each central rank.

Its middle support is again an exact two-design.  Indeed, in one completed
bank the number of middle targets containing a fixed coordinate pair is

\[
 \begin{cases}
 c(b-1),&\text{if the two coordinates form a pairing edge},\\[2pt]
 c(b^2-2)/4,&\text{otherwise}.
 \end{cases}                                           \tag{9.8}
\]

The first line is unchanged because no transversal contains both members
of one pair.  In the second line, the old defect-one contribution is
`c(b-2)(b+1)/4`, and the `b` boundary transversals contribute `cb/4` by
exact two-bit state projection.  Summing (9.8) over one aligned and
`2b-2` unaligned factors gives

\[
                         \lambda_2^\circ={cb^2(b-1)\over2},            \tag{9.9}
\]

which is exactly the parameter forced by `K_circ` middle blocks.

### 9.4 Completed augmented codegrees

For one completed state, direct substitution in the chronology formula
gives

\[
 |\{(M,L):L\subset M\}|={b(5b-1)\over2},\qquad
 |\{(M,U):M\subset U\}|=2b^2.                         \tag{9.10}
\]

The complete small-tail table has maximum average partner counts

\[
\begin{array}{c|c}
\sigma&\text{maximum partners per target, averaged over one state}\\ \hline
0&0\\
1&(5b-1)/(2b)\\
2&(b^2+6b+1)/(2b).
\end{array}                                             \tag{9.11}
\]

The first nonzero maximum is middle-rooted containment of a lower target;
the second is lower-rank Johnson adjacency.  For `sigma>=3`, the argument
of (7.17) now uses at most `b^2-1` same-state partners and gives
`2/(b-1)`.  Central pairs remain exponentially smaller.  Therefore the
completed augmented packet orbit has the exact asymptotic maximum, and in
fact for all sufficiently large odd `b`,

\[
 \boxed{
 \max_{A\ne B}{d(A,B)\over d(A)}
 ={5b-1\over2b^2}={5+o(1)\over2b}.}                  \tag{9.12}
\]

Again its edge rank times (9.12) diverges, so completion repairs
serialization but does not manufacture a growing-rank matching theorem.

### Theorem 9.2 (serialization is no longer an independent obstruction)

If the completed three-rank packet orbit has a matching of size

\[
                         (1-o(1)){W_1\over K_\circ},  \tag{9.13}
\]

then its selected tours linearize into physical `H`-fragments with

\[
 M=W-o(W),\qquad
 t={M\over b^2},\qquad
 gt=O(W/b)=o(W),                                      \tag{9.14}
\]

and all their band windows are clean.  Their target sets at ranks
`b-1,b,b+1` have only `o(W)` aggregate holes.

#### Proof

The capacity calculation of Proposition 7.1 applies with `K_circ` in
place of `K`, proving the central-rank claims.  Every selected state is one
completed cyclic tour with `b^2` starts.  Linearize it and append the first
`g-1` cyclic letters; this is one physical fragment.  Lemma 9.1 makes all
band windows clean.  There are `M/b^2` state tours, so (9.14) follows.
\(\square\)

This theorem removes the earlier packet-boundary fragmentation loss and
the cleanliness part of the physical lift.  It still does **not** control
target multiplicities at the other `2H-2` band ranks.  The remaining Gate
`C` statement is now sharply separated into:

1. a near-capacity matching of completed augmented packets as in (9.13);
2. an aggregate off-central coverage theorem for the already clean full
   tour words.

The completed fragment is not literally in the restricted subclass used
to phrase Gate `C_F`, because its `b` boundary starts were not called
ordered internal flags there.  It is nevertheless a physical
`H`-fragment in the sense of Theorem I.1, so a proof of the two items above
would invoke the direct-hole compiler itself and replace, rather than
instantiate verbatim, the old Gate-`C_F` formulation.

## 10. Exact all-band support and the absence of a scalar capacity loss

Completion also permits an exact count of the distinct targets supplied by
one state away from the three central ranks.

### Lemma 10.1 (one completed tour at every clean rank)

Let `D_ell` be the number of distinct length-`ell` cyclic window sets in
one completed state word.  Then

\[
 \boxed{
 D_\ell=
 \begin{cases}
 b(\ell+1),&1\le\ell\le b-1,\\
 b^2,&b-1\le\ell\le2b-3.
 \end{cases}}                                           \tag{10.1}
\]

#### Proof

At the level of pair indices, packet `s` appends the cyclic list

\[
                         s+1,s+2,\ldots,s-1,s.         \tag{10.2}
\]

For `ell<=b-1`, a window therefore meets one cyclic interval of `ell`
pair indices.  There are `b` choices for that interval.  Along a fixed
interval the FIFO flips create one cut between the old and new selected
members, including the two extreme cuts; hence there are exactly `ell+1`
labelled sets.  They are distinct because the interval and the cut are
recoverable from the pair occupancies and selected labels.  This proves
the first line.

For `b-1<=ell<=2b-3`, two equal cyclic window sets would have equal
successive pair-occupancy endpoints in (10.2).  Removing their common
cyclic interval reduces equality to the same interval and cut data just
used, hence to the same start.  All `b^2` starts are therefore distinct.
The two formulas agree at `ell=b-1`. \(\square\)

The collision-code construction can be extended simultaneously to the
whole band.  A length-`b+h` form has at most `|h|+2<=H+2`
nonsplit pair indices.  For two same-rank forms, equality fixes the state
difference outside at most `2H+4` coordinates.  After discarding zero,
the all-band collision set consequently has size at most

\[
 \bigl((2H+1)b^2\bigr)^2 2^{2H+4}=2^{o(b)}.           \tag{10.3}
\]

Its syndrome rank is `O(H+log b)=o(b)`.  The random dual-distance and
small-subcode arguments from Sections 2 and 9 are unchanged, because
`H=o(b/log b)`.  Thus completed microbanks may be chosen so that different
states have no common target at any one band rank; the only repeated
targets inside a bank are the intrinsic same-state repetitions counted in
(10.1).

For two different pairings, a band target has at most `H+2` exceptional
pairing edges.  The common-support coloring argument deletes at most
`2H+4` edges of the union of the pairings and gives

\[
                         2^{b/2+O(H\log b)}=2^{b/2+o(b)}              \tag{10.4}
\]

common accessible targets at a fixed band rank.  A fixed accessible
target has random-bank inclusion probability `2^{-b+o(b)}`.  Summing over
`2H+1` ranks and fewer than `2b^2` factor pairs still gives `o(1)`.
Therefore the completed one-factorization packet can be chosen internally
target-disjoint, after identifying the intrinsic repetitions, at every
rank in the band.

For `1<=h<=H`, its distinct support sizes are

\[
 \boxed{
 K_{b-h}=K_\circ{b-h+1\over b},\qquad
 K_b=K_{b+h}=K_\circ.}                                \tag{10.5}
\]

These counts have enough scalar capacity at the packet number required by
the adjacent layers.  Indeed,

\[
 {\binom{2b}{b-h}\over W}
 =\prod_{i=0}^{h-1}{b-i\over b+i+1}
 \le {b-h+1\over b+1}.                               \tag{10.6}
\]

To verify the inequality, cancel `b-h+1`; the remaining numerator factors
are termwise at most the remaining denominator factors.  A matching of
`W_1/K_circ` completed packets would have total distinct-target capacity

\[
 {W_1\over K_\circ}K_{b-h}
 =W{b-h+1\over b+1}
 \ge {2b\choose b-h}.                                \tag{10.7}
\]

At the upper rank, its capacity is `W_1`, which is at least
`binom(2b,b+h)` for every `h>=1`.  Thus no rank in the live band has a
scalar occurrence deficit.

Equation (10.7) is only a capacity theorem.  Supports of different selected
packets may overlap at off-central ranks, and neither the central matching
nor exact low-order balance prevents uncovered targets.  The remaining
all-band assertion is therefore purely a **correlated coverage** problem:
choose the near-capacity completed-packet matching so that the union, not
just the total available support, misses `o(W)` targets in aggregate over
the band.

## 11. Whole-tour product regeneration fails immediately

Completion settles cleanliness and serialization, but it also makes clear
that whole tours cannot be selected by an independently regenerated
nibble.  Let `E` be the family of the `q=b(b-1)` distinct internal middle
targets in one coherent tour and let

\[
                       \mathscr O(E)=\{\pi E:\pi\in S_{2b}\}.       \tag{11.1}
\]

Every choice of pairing, cyclic pair order, initial state, and phase origin
is a relabelling of one standard coherent tour, so this orbit contains all
internal coherent-tour supports.  The number of labelled choices is

\[
 { (2b)!\over2^b b!}\,(b-1)!\,2^b={ (2b)!\over b}:                 \tag{11.1a}
\]

choose the pairing, its directed cyclic order, and one selected member of
each pair.  Hence `|\mathscr O(E)|<=(2b)!/b`.

### Proposition 11.1 (product-thinning extinction)

Retain each middle target independently with probability `rho`.  If, for
some fixed `epsilon>0`,

\[
             1-\rho\ge{(2+\epsilon)\log b\over b},                  \tag{11.2}
\]

then with probability tending to one the retained middle layer contains no
complete internal coherent-tour support.

#### Proof

Let `Y` count surviving supports.  Since every support has `q` distinct
middle targets,

\[
 \mathbb EY=|\mathscr O(E)|\rho^q
       \le{(2b)!\over b}\rho^q.                                    \tag{11.3}
\]

Using `log rho<=-(1-rho)` and `log((2b)!)<=2b log(2b)`, (11.2) gives

\[
 \log\mathbb EY
 \le2b\log(2b)-(2+\epsilon)(b-1)\log b
 =-\epsilon b\log b+O(b)=-\Omega(b\log b).                         \tag{11.4}
\]

Thus \(\mathbb EY=o(1)\), and Markov's inequality proves the claim.
\(\square\)

This is not an upper bound on a deliberately correlated packing: a
structured residual may retain many complete tours.  It is an exact scope
wall for the simplest iterative argument.  Unlike a phase packet, whose
catalogue remains exponentially rich down to polynomial residual density,
a whole tour disappears from a product residual after only a
\(\Theta(\log b/b)\) deletion.  Therefore the remaining selector must either

1. build the near-capacity coherent-tour family by an algebraic correlated
   factor/absorption construction from the start; or
2. first select substantially shorter packets and then chain them into the
   clean completed-tour words.

Independent whole-tour regeneration cannot prove the required `o(W)`
leave.

There is a rooted form of the same obstruction.  Counting the labelled
choices in (11.1a), then double-counting incidences with a fixed middle
target, gives labelled root degree

\[
 D_{\rm tour}={[(2b)!/b]q\over W}=(b-1)(b!)^2.                     \tag{11.5}
\]

### Corollary 11.2 (product-residual root isolation)

Put

\[
                 \rho=\exp\left\{-{(2+\epsilon)\log b\over b}\right\}.
                                                                        \tag{11.6}
\]

Conditioned on retaining a fixed middle target `A`, its expected number of
available internal coherent tours is `o(1)`.  Consequently all but
\(o_{\mathbb P}(\rho W)\) retained targets are isolated in the induced
tour hypergraph.

#### Proof

The simple degree is at most the labelled degree (11.5), and each tour
through `A` requires its other `q-1` distinct targets to survive.  Therefore

\[
 \mathbb E[\deg_\rho(A)\mid A\text{ retained}]
 \le D_{\rm tour}\rho^{q-1}.                                      \tag{11.7}
\]

Stirling's estimate and `q=b(b-1)` give

\[
\begin{aligned}
 \log(D_{\rm tour}\rho^{q-1})
 &=2b\log b-2b+O(\log b)
   -{(2+\epsilon)(q-1)\log b\over b}\\
 &=-\epsilon b\log b-2b+O(\log b)\longrightarrow-\infty.
\end{aligned}                                                       \tag{11.8}
\]

Thus (11.7) is `o(1)`, uniformly in `A`.  The probability that a retained
root is nonisolated is at most its expected degree.  Summing over roots and
applying Markov's inequality proves the aggregate assertion. \(\square\)
