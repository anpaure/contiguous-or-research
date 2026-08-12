# Lane O: the complete `D_4` pair bridge in parent-aligned collars

Date: 2026-07-26

Method: pure mathematics only.  The displayed finite certificate in
`MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md` is used through its literal
path and ownership ledgers.  No search, solver, program, or web input is
used here.

## 0. Verdict

The strict-child early-label scheme is erased exactly: a substitution
inside a `D_s`-port hole fixes the complementary endpoints
`P,J\setminus P`, so the
next full matched window has empty local intersection on every row.

The new complete `D_4` factor does, however, give a genuine
**parent-boundary** direction.  Its first-insertion pair vector

\[
 (5,5,2,2)\longrightarrow(5,5,1,3)
\]

is only one start of the full profile.  On the six starts meeting the open
parent slab, the exact labelled change is

\[
 \boxed{d_6=2e_2-3e_3-3e_6+4e_7.}                 \tag{0.1}
\]

The other three cyclic starts have change `-d_6`.  Thus the complete
singleton profile cancels when both sectors land on the same physical
singletons, but the six parent starts are not themselves cancelled.  At a
higher context the two sectors may acquire different exterior carriers;
then cancellation is governed by their literal carrier push-forwards and
is not automatic.

There is a sharp positive higher-context fact.  For all cyclic local
intervals of length two, the canonical factor has multiplicity five on an
explicit set of eighteen pairs and multiplicity two on the complementary
eighteen pairs.  The new factor transfers nineteen units from the high
side to the low side.  With a common multiplicity scale `M` and a common
normalized residual capacity `c=(p-beta)/M`, the exact cap change is

\[
 M\Phi(c),
\]

where

\[
\Phi(c)=
\begin{cases}
0,&c\le1,\\
c-1,&1\le c\le2,\\
21-10c,&2\le c\le3,\\
-6-c,&3\le c\le4,\\
10c-50,&4\le c\le5,\\
0,&c\ge5.
\end{cases}                                           \tag{0.2}
\]

Hence the length-two profile gives genuine cap descent exactly for

\[
                    \boxed{21/10<c<5},                 \tag{0.3}
\]

with the sharp descent `10M` at `c=4`.  It worsens the cap for
`1<c<21/10`.  Thus the bridge is neither universally collar-cancelled nor
background-independently improving.

Right suffixing, left prefixing, and outer primitive wrapping all admit
exact one-node port-preserving lifts.  Their complete carrier formulas are
proved below.  More generally the established aligned context-substitution
theorem makes the replacement legal in every common aligned port context;
changed `a_1,b_4` are profile data, not unresolved gluing data.  What
remains unproved is the global statement that the
canonical coefficient-one background places a positive-density family of
these carrier profiles in the favourable residual-capacity range while
leaving their positive collars enough room.  No constant-one conclusion is
claimed.

## 1. Port paths and the exact erasure theorem

Let `J` have size `2s`.  A rooted `D_s`-port factor is a partition of the
middle-levels inclusion graph into paths

\[
 P=X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{s-1}\supset X_s=J\setminus P,qquad P\in D_s.       \tag{1.1}
\]

After insertion into a context with fixed exterior state `O`, its state
path is `O union X_0,...,O union X_s`.

### Theorem 1.1 (full matched-window erasure)

For every row of every rooted port factor,

\[
 \boxed{\bigcap_{t=0}^{s}(O\cup X_t)=O.}              \tag{1.2}
\]

In particular, any sequence of substitutions strictly inside this hole
which fixes its two ports is invisible to the full matched window.

#### Proof

Every element of `O` is present throughout.  If `x in J`, one of the two
complementary endpoints `P,J\setminus P` omits `x`, so `x` is absent from
the full
intersection.  No internal state enters the argument.  \(\square\)

Consequently an earlier split does not propagate through a later full
matched hole.  A surviving packet must alter a boundary or a crossing
collar of the serviced window.

## 2. The `D_4` certificate and its positional tensor

For one rooted rank-four path write

\[
 X_t=(P\setminus\{a_1,\ldots,a_t\})
       \cup\{b_1,\ldots,b_t\},\qquad0\le t\le4,        \tag{2.1}
\]

and let `9` be the distinguished odd-graph coordinate.  Its oriented
coordinate word is

\[
 q(P)=(a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,9).            \tag{2.2}
\]

For the canonical factor `F` and the new factor `G`, the fourteen words
are

\[
\begin{array}{c|c|c}
P&q_F(P)&q_G(P)\\ \hline
1234&243186579&423186579\\
1235&235184679&253187649\\
1236&623187459&321674589\\
1237&231764589&372186459\\
1245&452186739&124536789\\
1246&642187539&146238759\\
1247&421765389&174238569\\
1256&216543879&251673489\\
1257&215743689&127534869\\
1345&145328679&314562789\\
1346&164328759&634185729\\
1347&143726589&374182569\\
1356&136524879&153627489\\
1357&135724689&317542869.
\end{array}                                             \tag{2.3}
\]

The displayed path table for `G` partitions all seventy `X`-states and
all fifty-six adjacent-union `Y`-states, and has the same prescribed ports
as `F`.  Thus both are literal integral `D_4`-port factors.

For any position set `A\subseteq\mathbb Z_9`, define the full positional
tensor

\[
 D_A=\sum_{P\in D_4}
 \left(e_{\{q^G_i(P):i\in A\}}
       -e_{\{q^F_i(P):i\in A\}}\right).              \tag{2.4}
\]

For a cyclic interval of length `ell` beginning at `j`, write

\[
 \Delta_{\ell,j}=D_{\{j,j+1,\ldots,j+\ell-1\}}.       \tag{2.5}
\]

This tensor, rather than the four pair totals, is the exact local datum
seen by every higher context.

## 3. The complete singleton parent profile

A depth-three window through a rank-four path has a singleton local target.
The six starts which meet the open parent slab have targets

\[
                   a_2,a_3,a_4,b_1,b_2,b_3.           \tag{3.1}
\]

Reading these six columns of (2.3) gives

\[
\begin{aligned}
 u_F&=(9,9,12,12,12,12,9,9),\\
 u_G&=(9,11,9,12,12,9,13,9),
\end{aligned}                                          \tag{3.2}
\]

on coordinates `1,...,8`.  Hence

\[
             u_G-u_F=2e_2-3e_3-3e_6+4e_7=d_6.         \tag{3.3}
\]

On

\[
 E_0=\{1,8\},\quad E_1=\{2,3\},\quad
 E_2=\{4,5\},\quad E_3=\{6,7\},                     \tag{3.4}
\]

the pair totals are

\[
 (18,21,24,21)\longrightarrow(18,20,24,22).           \tag{3.5}
\]

Thus the reported first-insertion move `E_2 -> E_3` is not repaid by the
other five parent starts.  Those five contribute `E_1 -> E_2`, and the
six-start result is the composite bridge `E_1 -> E_3`.

The complementary three starts have targets `b_4,9,a_1`.  Their exact
profiles are

\[
\begin{aligned}
 v_F&=(5,5,2,2,2,2,5,5,14),\\
 v_G&=(5,3,5,2,2,5,1,5,14),
\end{aligned}                                          \tag{3.6}
\]

and

\[
                         v_G-v_F=-d_6.                 \tag{3.7}
\]

Therefore

\[
                  u_F+v_F=u_G+v_G=14\sum_{x=1}^9e_x.  \tag{3.8}
\]

Equation (3.8) is the exact point-margin identity.  It fixes the complete
nine-start singleton profile, not the six-start subprofile.  Consequently
the six-start bridge is cancelled at the physical singleton scale, where
there is no exterior carrier and the same cells receive (3.3) and (3.7).

## 4. Exact parent lifts and port legality

Add one selected coordinate `alpha`, one unselected coordinate `beta`, and
let `c` be the new distinguished outer coordinate.  The following three
one-node lifts are exact.

### Theorem 4.1 (right, left, and primitive one-node lifts)

For the right suffix context `x10`, put

\[
 \widetilde X_t=\alpha\cup X_t\ (0\le t\le4),\qquad
 \widetilde X_5=\beta\cup(J\setminus P).              \tag{4.1}
\]

Its coordinate word is

\[
 Q_R=(a_1,a_2,a_3,a_4,\alpha,
      b_1,b_2,b_3,b_4,\beta,c).                       \tag{4.2}
\]

For the left prefix context `10x`, put

\[
 \widetilde X_0=\alpha\cup P,\qquad
 \widetilde X_{t+1}=\beta\cup X_t\ (0\le t\le4),     \tag{4.3}
\]

with coordinate word

\[
 Q_L=(\alpha,a_1,a_2,a_3,a_4,
      \beta,b_1,b_2,b_3,b_4,c).                       \tag{4.4}
\]

For the outer primitive context `1x0`, put

\[
\begin{aligned}
 \widetilde X_0&=\alpha\cup P,\\
 \widetilde X_t&=\{\alpha,\beta\}\cup
                   (J\setminus Y_{4-t})\quad(1\le t\le4),\\
 \widetilde X_5&=\beta\cup(J\setminus P),
\end{aligned}                                          \tag{4.5}
\]

with coordinate word

\[
 Q_J=(a_4,a_3,a_2,a_1,\alpha,\beta,
      b_4,b_3,b_2,b_1,c).                             \tag{4.6}
\]

Every lifted row has the literal ports

\[
                    \alpha\cup P,\qquad
                    \beta\cup(J\setminus P).          \tag{4.7}
\]

Replacing the lifted `F` packet by the lifted `G` packet preserves both
ambient ownership ledgers exactly.

#### Proof

For (4.1), the lifted `X`-ledger is the old `X`-ledger with `alpha`
adjoined, plus the fixed terminal collar.  Its adjacent unions are

\[
 \alpha\cup Y_0,\ldots,\alpha\cup Y_3,
 \quad\{\alpha,\beta\}\cup(J\setminus P),             \tag{4.8}
\]

so the old `Y`-ledger and the fixed collar prove equality.

For (4.3), the first adjacent union is the fixed collar
`{alpha,beta} union P`; the other four are `beta union Y_t`.  Again both
ledgers agree.

For (4.5), the four internal lifted `X`-states are the complements of
`Y_3,Y_2,Y_1,Y_0`, with `alpha,beta` adjoined.  Their ledger is therefore
the complemented old `Y`-ledger.  Consecutive internal states have union

\[
                 \{\alpha,\beta\}\cup(J\setminus X_t), \tag{4.9}
\]

because `Y_t intersect Y_(t-1)=X_t`; these form the complemented old
interior `X`-ledger.  The two remaining boundary colours are the fixed
sets `{alpha,beta} union P` and
`{alpha,beta} union (J\setminus P)`.  Thus both discrepancies vanish.
Formulae
(4.2), (4.4), and (4.6) follow by reading the exchange orders.  \(\square\)

### Theorem 4.2 (complete carrier push-forward)

Let an ambient cyclic interval of length `L` in one of the words `Q_C`
meet the variable local positions in `A_C(L,k)\subseteq\mathbb Z_9` and
meet the new fixed coordinates in
`O_C(L,k)\subseteq\{alpha,beta\}`.  Its exact
signed target profile is

\[
 \boxed{
 \widetilde\Delta^{\,C}_{L,k}
 =O_C(L,k)\cup\iota(D_{A_C(L,k)}).}                   \tag{4.10}
\]

For `C=R,L`, contracting `alpha,beta` restores the cyclic order (2.2), so
`A_C(L,k)` is an interval and (4.10) is one of the
`Delta_(ell,j)`, with its actual collar adjoined.  For `C=J`, contraction
gives the order

\[
                      (3,2,1,0,7,6,5,4,8).            \tag{4.11}
\]

An interval in (4.11) need not be an interval in the original order.
Hence arbitrary primitive wrapping requires the full positional tensor
`D_A`; the interval table alone is insufficient.

#### Proof

Every target is the unordered set of the coordinates in its cyclic
carrier interval.  Fixed coordinates are identical on the two packet
shores.  Removing them leaves exactly the position set in (2.4), proving
(4.10).  The order assertions follow from (4.2), (4.4), and (4.6).
\(\square\)

The lifts are therefore integral and port-legal.  Pairwise disjoint
aligned lifts commute.  Overlapping or nested lifts must be grouped into a
joint atom unless their displayed ledgers are proved disjoint or laminar;
pairwise exactness alone does not prove arbitrary multiscale composition.

## 5. Which aggregate carrier lengths can survive?

Put

\[
                         \Delta_\ell=\sum_{j\in Z_9}
                                      \Delta_{\ell,j}. \tag{5.1}
\]

Directly from (2.3),

\[
                  \Delta_1=\Delta_4=\Delta_5=\Delta_8=0, \tag{5.2}
\]

where lengths four and five are the two exact ownership ledgers and
lengths one and eight are the point-margin ledger and its complement.
On the other hand,

\[
 \frac12\|\Delta_2\|_1=19,\qquad
 \frac12\|\Delta_3\|_1=22,                            \tag{5.3}
\]

and complementation gives the same masses at lengths seven and six.
Thus there is no higher-context collar-cancellation identity at lengths
two, three, six, or seven.

Even a zero aggregate in (5.2) requires a common physical carrier.  If
different starts acquire different exterior carriers, the indexed
push-forwards in (4.10) need not cancel.

At the lifted rank-five level there is an analogous forced list.  Summing
over all starts of a common lifted carrier gives zero signed profile at
ambient cyclic lengths

\[
                         L=1,5,6,10.                   \tag{5.3a}
\]

Lengths five and six are the lifted `X/Y` ownership ledgers; lengths one
and ten are point margins and complements.  No ledger identity forces
the lifted length-two or length-three profiles to vanish.

Every one-node lift exposes a nonzero short carrier.  For example,

\[
 Q_R[0,2)=\{a_1,a_2\},\quad
 Q_R[0,3)=\{a_1,a_2,a_3\},                             \tag{5.4}
\]

and the corresponding start-resolved masses are seven and six.  The left
lift has the same sectors one position later.  In the primitive lift,

\[
 Q_J[0,2)=\{a_4,a_3\},\quad
 Q_J[0,3)=\{a_4,a_3,a_2\},                             \tag{5.5}
\]

with masses nine and seven.  Hence all three exact parent lifts can expose
nonzero higher profiles.

## 6. The length-two canonical high/low transfer

Let `h_F(S)` count occurrences of the unordered pair `S` among all
cyclic length-two intervals of the fourteen words `q_F(P)`.  Literal
reading of (2.3) gives

\[
 h_F(S)=
 \begin{cases}
 5,&S\in\mathcal H,\\
 2,&S\notin\mathcal H,
 \end{cases}                                           \tag{6.1}
\]

where

\[
\begin{aligned}
\mathcal H=\{&12,13,18,19,23,24,29,34,35,45,46,56,\\
              &57,67,68,78,79,89\}.
\end{aligned}                                          \tag{6.2}
\]

The displayed vector `Delta_2` has all of its negative support in
`mathcal H` and all of its positive support in the complement.  Its
negative coefficients consist of nine ones, three twos, and one four;
its positive coefficients consist of six ones, two twos, and three
threes.  More precisely,

\[
\begin{array}{c|l}
5\to5&18,19,45,57,89\\
5\to4&12,13,23,24,35,56,67,68,78\\
5\to3&29,34,46\\
5\to1&79\\ \hline
2\to2&15,16,17,28,38,49,59\\
2\to3&25,26,36,37,48,58\\
2\to4&14,47\\
2\to5&27,39,69.
\end{array}                                           \tag{6.3}
\]

Consequently the complete multiplicity distributions are

\[
 h_F:\quad 18\text{ cells at }5,\quad18\text{ cells at }2, \tag{6.4}
\]

and

\[
 h_G:\quad
 8\text{ at }5, 11\text{ at }4, 9\text{ at }3,
 7\text{ at }2, 1\text{ at }1.                       \tag{6.5}
\]

Both have total mass `126=14*9`.

### Theorem 6.1 (exact uniform-background cap hinge)

Suppose a physical carrier injects these thirty-six targets without
identifications, every local occurrence has common multiplicity `M>0`,
and the unaffected background gives the same residual capacity `p-beta`
on the thirty-six cells.  Put

\[
                         c={p-\beta\over M}.            \tag{6.6}
\]

Then

\[
 K_p(\beta+Mh_G)-K_p(\beta+Mh_F)=M\Phi(c),            \tag{6.7}
\]

with `Phi` given in (0.2).  In particular the new factor is strictly
cap-improving exactly for `21/10<c<5`, and its maximum descent is `10M`
at `c=4`.

#### Proof

By (6.4)--(6.5), after dividing every hinge by `M`, the old and new
contributions are

\[
 18(5-c)_++18(2-c)_+                                  \tag{6.8}
\]

and

\[
 8(5-c)_++11(4-c)_++9(3-c)_++7(2-c)_++(1-c)_+.       \tag{6.9}
\]

Subtracting on the intervals cut out by `1,2,3,4,5` gives (0.2).
\(\square\)

This theorem is a genuine higher-context drain, not merely a nonzero
signed vector.  It is also a sharp obstruction: the same packet worsens
cap overload when `1<c<21/10`.

### Theorem 6.2 (length three is nonzero but uniformly cap-neutral)

On the support changed by `Delta_3`, the old and new multiplicity
multisets are both

\[
                    \boxed{\{0^4,1^{18},2^{16},3^1\}.} \tag{6.10}
\]

All targets outside that support are unchanged.  Consequently, under one
common injective carrier and one scalar background, the length-three cap
tail is exactly the same for `F` and `G` at every cutoff.  The same holds
at length six by complementation.

#### Proof

Reading cyclic triples in (2.3), the changed cells have the following
old-to-new multiplicities:

\[
\begin{array}{c|l}
1\to0&136,368,349\\
2\to1&124,125,235,246,346,357,567,178,478,289,589,179,
       239,149,459\\
2\to0&679\\
3\to1&279\\
0\to1&258,479\\
0\to2&147,259\\
1\to2&127,236,247,257,267,367,148,348,389,489,379,159,
       569,169\\
1\to3&369.
\end{array}                                           \tag{6.11}
\]

The two sides of (6.11) each have the multiplicity census in (6.10).
Applying any scalar hinge `(x-c)_+` and summing therefore gives equality.
Complementing target sets proves the length-six statement.  \(\square\)

This distinguishes two notions which must not be conflated.  The vector
`Delta_3` is nonzero and has positive mass twenty-two, so a nonuniform
background or carrier collision can expose it.  Nevertheless it supplies
no scalar-background descent.

### Lemma 6.3 (point-star margins and robustness)

For every `ell` and every local coordinate `x`,

\[
 \sum_{S\ni x}\Delta_\ell(S)=0.                       \tag{6.12}
\]

Moreover, if `beta_0` is a scalar background and `beta(S)` is arbitrary,
the difference between the two associated cap-change values is at most

\[
                         \sum_S|\beta(S)-\beta_0|.     \tag{6.13}
\]

#### Proof

In each cyclic word of length nine, a fixed coordinate belongs to exactly
`ell` of the nine cyclic `ell`-intervals.  Summing over the fourteen rows
proves (6.12) on both packet shores.  For (6.13), each hinge
`(u-beta)_+` is one-Lipschitz in `beta`; sum the coordinatewise bounds.
\(\square\)

Thus the length-two drain survives an inhomogeneous background whenever
the `L^1` error in (6.13) is smaller than `-M Phi(c)`.  Conversely,
additive point-star potentials cannot certify its sign, because every such
linear test annihilates (6.12).

## 7. Heterogeneous backgrounds and the exact collar gate

Let `u(T)` be the old full affected-window histogram of one physical
joint atom, let `d(T)` be its signed old-to-new profile, and let

\[
                         c(T)=(p-\beta(T))_+            \tag{7.1}
\]

be the residual capacity left by all unaffected windows.  The exact cap
change is

\[
 \boxed{
 \Delta K=\sum_T\left[(u(T)+d(T)-c(T))_+
                         -(u(T)-c(T))_+\right].}       \tag{7.2}
\]

Writing `d_+=max(d,0)` and `d_-=max(-d,0)`, this is `G-R`, where

\[
 R=\sum_{d(T)<0}
    \min\{d_-(T),(u(T)-c(T))_+\},                     \tag{7.3}
\]

\[
 G=\sum_{d(T)>0}
    \bigl(d_+(T)-(c(T)-u(T))_+\bigr)_+.               \tag{7.4}
\]

Thus cap descent is equivalent to the literal inequality `R>G`: the
negative cells must contain removable old excess, and the positive cells
must have unused residual capacity.

For the six-start singleton bridge (3.3), this specializes to

\[
\begin{aligned}
\Delta K_6={}&(11-c_2)_+-(9-c_2)_+\\
 &(9-c_3)_+-(12-c_3)_+\\
 &(9-c_6)_+-(12-c_6)_+\\
 &(13-c_7)_+-(9-c_7)_+ .                              \tag{7.5}
\end{aligned}
\]

It has no background-independent sign.  At the isolated physical
singleton scale the complementary three-start profile lands on the same
cells and cancels it exactly.

More generally let `dhat_6,dhat_3` be the two occurrence-indexed ledgers
whose aggregate vectors are `d_6,-d_6`, and let `P_C,Q_C` be their
physical carrier push-forwards in an outer context.  The exact complete
profile is

\[
 \boxed{\Delta_C=P_C\widehat d_6+Q_C\widehat d_3.}    \tag{7.6}
\]

It cancels if and only if the right side vanishes.  If the two sectors are
transported by fixed injections `phi_6,phi_3`, then

\[
                 \Delta_C=(\phi_6)_*d_6-(\phi_3)_*d_6. \tag{7.7}
\]

Equal images cancel.  Disjoint images have positive and negative mass
twelve and can realize six units of cap descent on the six-start image
when its residual capacities satisfy (7.5), while the compensating image
has enough room.  Partial overlap is decided by literal addition in
(7.6).

## 8. Quantitative implication and exact remaining gate

The `D_4` factor therefore passes the finite parent-profile test in the
strongest possible qualified sense:

* strict matched windows are erased by the port endpoints;
* the full physical singleton profile is exactly collar-cancelled;
* parent-aligned higher contexts expose nonzero length-two and length-three
  profiles;
* the length-two profile has an explicit canonical high-to-low cap-descent
  regime;
* outside that residual-capacity regime the same packet can be neutral or
  harmful.

To obtain `PCap=o(W)`, one still needs a family of product-compatible
joint parent atoms and one common choice over all depths such that

\[
 \sum_{q\le H}
 \left(K_p\left(\beta_q+\sum_Au_{A,G_A,q}\right)
             -(W-N_q)\right)_+=o(W).                  \tag{8.1}
\]

The missing theorem must prove, for the actual canonical backgrounds and
carrier maps, that the total removable excess (7.3) exceeds the positive
collar congestion (7.4) by the required amount.  It must also close every
overlap class into one joint atom; disjoint one-node legality does not by
itself settle nested windows.

Thus the new factor is not killed by a universal collar invariant.  It is
a real cap-active parent primitive.  What remains is a global
carrier-capacity and overlap theorem, not another finite port-factor
existence question.
