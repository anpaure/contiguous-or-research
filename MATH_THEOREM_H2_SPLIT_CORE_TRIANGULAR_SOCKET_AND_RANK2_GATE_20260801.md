# Split-core pivot: exact triangular allocation, a regenerative static socket, and the rank-two gate

Date: 2026-08-01  
Status: unconditional target-allocation and static routing theorems; a
fixed-`H` STW specialization; and a fail-closed physical interface rebased
on the fully literal lower-`q1` two-address repair.  The inherited algebraic
recurrence has a sharp finite signed-residence horizon and is not an
unbounded physical recurrence.  No literal global compiler, `B+O(1)`
recurrence, or unconditional coloured closure is claimed.

## 0. Verdict

Use the split-core packet of
`MATH_THEOREM_SPLIT_CORE_PIVOT_LITERAL_TWO_SIDED_COLLAR_20260801.md` at
depth `h`.  Its strict-lower fan is

\[
 \mathcal F_X=\{X\}\mathbin{\dot\cup}
   \{P_i:1\le i<h\}\mathbin{\dot\cup}
   \{S_i:1\le i<h\},                                  \tag{0.1}
\]

where

\[
 P_i=B\cup\lambda[h-i+1,h],\qquad
 S_i=B\cup\rho[1,i],\qquad X\subseteq B,\quad |B|=r-h. \tag{0.2}
\]

The exact answer has four parts.

1. The fan is a lossless two-chain triangular atom:

   \[
      X<P_1<\cdots<P_{h-1},\qquad
      S_1<\cdots<S_{h-1}.                              \tag{0.3}
   \]

   Symmetrically, one may attach `X` to the `S` chain instead.  The lengths
   are `h,h-1`, and two chains are necessary.  The fan therefore
   fits the two largest triangular boundary capacities at `h=d`, or the
   two endpoint owners of the pivot.  This uses the ray collapse rather
   than curing it.
2. If the `S` chain is stored with a mutable bottom `x`, it is a genuine
   static regenerative socket.  A two-step route moves `x` into an
   underloaded gap, replaces it by any overloaded target `y` strictly below
   `S_1`, and exposes the identical aperture `(emptyset,S_1)` again.
3. Rank two is a lossless geometric normal form and, for any fixed family
   of untouched STW underloaded sources, rank-two starts can be selected
   jointly and routed by one socket.  Rank two is **not** lossless for a
   prescribed compiler task, an arbitrary internal gap, or a fixed literal
   common-cap word.
4. The sparse split-core source has

   \[
      b_{q1}=2+\mathbf 1_{|X_L|>1}+\mathbf 1_{|X_R|>1}    \tag{0.4}
   \]

   non-tight native lower transitions.  An address-minimal repair chooses arbitrary
   indices `1<=j<h` and `2<=s<=h` and makes only

   \[
     \{\lambda_j\}\longmapsto(B-\{x_R\})+\lambda_j,
     \qquad
     \{\rho_s\}\longmapsto(B-\{x_L\})+\rho_s.       \tag{0.5}
   \]

   Every one of these `(h-1)^2` canonical choices makes all `3h` native
   lower-`q1` cells exact without changing the
   owner row, pre-row, task/rays, insertion transparency, or residence.
   Two positions are necessary among enlargement-only repairs.  Thus no
   external lower-colour occurrence debt remains.  The physical export has
   only two enlarged-position cap/guard objects, together with the literal
   singleton-host audit.  Repeated deadline jumps additionally require the
   shared-bank residence clock derived in Theorem 5.3.

The live bridge is therefore an exported **lower-chain socket state**, not
only the already exported owner/right-guard state.

## 1. Exact two-chain allocation and overload gain

Every `P_i` contains a `lambda` label and every `S_j` contains a disjoint
`rho` label.  Hence cross-shore members are incomparable, while each shore
is a strict chain and `X` lies strictly below both first members.

### Theorem 1.1 (lossless fan allocation)

The chain-cover number of \(\mathcal F_X\) is exactly two, attained by (0.3).
It is also attained by the symmetric cover

\[
 P_1<\cdots<P_{h-1},\qquad X<S_1<\cdots<S_{h-1}.       \tag{1.0}
\]

Suppose a complete lower-target chain system has two empty receiver
addresses `b_0,b_1` of capacities at least `h,h-1`, with formal tops or
owners containing the two chains.  Move every target of \(\mathcal F_X\) from
its old address and put the chains (0.3) at `b_0,b_1`.  The result is again
a complete chain system and loses no target.

If

\[
 n_a=|C_a\cap\mathcal F_X|,\qquad
 e_a=(|C_a|-c(a))_+,                                   \tag{1.1}
\]

for the old donor addresses, then exactly

\[
          \Phi_{\rm new}
            =\Phi_{\rm old}-\sum_a\min\{n_a,e_a\}.     \tag{1.2}
\]

#### Proof

Deleting arbitrary members of an inclusion chain preserves a chain.
Equation (0.3) proves that the two receiver banks are legal and within
capacity.  Thus target partition and containment are preserved.  Removing
`n_a` targets from a donor of excess `e_a` lowers its excess by exactly
`min(n_a,e_a)`; the receivers create no excess.  Summing gives (1.2).
Cross-shore incomparability proves that one receiver chain is impossible.
\(\square\)

At `h=d`, the canonical boundary realization uses `partial_d` and
`partial_(d-1)`.  These addresses are not spare in an existing triangular
factor: their old targets must be released and reallocated in the same
target and common-cap ledger.  Alternatively, the chains are anchored at
the pivot endpoints `B union L` and `B union R`, both of cap `d`.

Formula (1.2) is the exact coloured limitation.  The packet absorbs
overload only to the extent that its named fan targets currently lie on
overloaded addresses.  The local owner, residence, source-start, and q1
claims do not specify that address map.

## 2. A regenerative one-sided lower socket

Put

\[
             C_b(x)=(x<S_1<\cdots<S_{h-1})             \tag{2.1}
\]

in a capacity-`h` boundary address `b`, where
`emptyset subsetneq x subsetneq S_1`.  The companion `P` ray occupies the
capacity-`h-1` receiver.  The deletion gap of the bottom target `x` is
always

\[
                          (\varnothing,S_1).            \tag{2.2}
\]

### Theorem 2.1 (regenerative two-step route)

Suppose `x` fits an ordinary gap `g` of an underloaded address `a`, and an
overloaded third address `c` contains a target

\[
                          \varnothing\subsetneq y\subsetneq S_1. \tag{2.3}
\]

Then

\[
                 a\xleftarrow{x}b\xleftarrow{y}c       \tag{2.4}
\]

is an admissible balancing route.  It lowers total overload by one and
changes only

\[
                          C_b(x)\longmapsto C_b(y).      \tag{2.5}
\]

In particular, deleting the new bottom `y` re-exposes the same aperture
(2.2).

#### Proof

The first fit is the hypothesis on `g`; the second is (2.2)--(2.3).  The
three addresses are distinct and the terminal is overloaded, so the exact
single-hole rotation theorem applies.  Equation (2.5) is its middle-address
replacement. \(\square\)

The exact stopping alternatives are now transparent:

* the current bottom `x` fits no underloaded gap; or
* `(emptyset,S_1)` contains no target currently held by an overloaded
  address.

The aperture has `2^|S_1|-2` targets, but raw size does not exclude either
coloured obstruction.  The state is regenerative in aperture, not finite in
the identity of its bottom target.

## 3. Rank-two normalization: exact positive and negative scopes

Let a split-core instance have `X=X_L dotunion X_R`.  Choose
`x_L in X_L,x_R in X_R`, put

\[
                    \widetilde X=\{x_L,x_R\},
             \qquad \widetilde C=B-\widetilde X.       \tag{3.1}
\]

Use singleton split shores in the normalized source.

### Theorem 3.1 (geometric rank-two normal form)

The original and normalized packets have exactly the same:

* owner path `L_t,M_j,R_t`;
* pre-insertion upper cells `U_j`;
* two lower rays `P_i,S_i`;
* abstract lower and upper q1 colours;
* owner-run/residence traces, source length, and labelled support cost.

Only the singleton lower target changes from `X` to `\widetilde X`, and the
literal source-letter distribution changes.  Therefore rank two is without
loss for the owner/q1/topology/residence projection, but not for the
literal task/deck/common-cap projection.

#### Proof

All listed set-valued owner and ray formulas depend only on
`B,x_L,x_R,L,R,D^-,D^+,q^-,q^+`.  Replacing `C,X_L,X_R` by
`B-{x_L,x_R},{x_L},{x_R}` keeps those unions unchanged.  The singleton cell
is the inserted letter itself and therefore changes. \(\square\)

A literal counterexample is immediate.  Prescribe task
`X={1,2,3}` inside a base `B`, and normalize to `{1,2}`.  Arrange the old
context so that every `B`-bearing cell has one additional coordinate.  The
original packet has the singleton cell `{1,2,3}`; the normalized new fan has
only `{1,2}` and sets strictly containing `B`, while transported cells retain
the extra coordinate.  The prescribed task is absent.

For a general gap `(A,D)`, a rank-two fitting target exists exactly when

\[
                          |A|\le1,\qquad |D|\ge3.       \tag{3.2}
\]

Thus rank two is automatic for the large STW bottom gaps, but not for an
arbitrary internal deletion gap.  In the odd Pascal packet, choosing the
newborn task `{x,y}` is literally rank two and incurs no normalization loss;
the separate newborn tasks `{x}` and `{y}` are not covered by this choice.

## 4. A fixed-`H` STW static absorber

This is the strongest unconditional Boolean-specific use of the socket.
It is static: compiler cells and source chronology are addressed in
Section 5.

Fix `H` and, in a sufficiently large complemented STW chain system, choose
`H` untouched underloaded nonterminal source addresses `a_j`.  Let their
bottom gaps be `(emptyset,T_j)` and deficits be `1<=u_j<=d`.  The STW
construction gives

\[
                          |T_j|\ge n-\lceil n/2\rceil-C_0.     \tag{4.1}
\]

### Theorem 4.1 (fixed-`H` rank-two socket routing)

For all sufficiently large `n`, one may choose a depth-`d` split-core base
`B`, a right ray `S`, pairwise-distinct rank-two starts `X_j subseteq B`,
and pairwise target-disjoint nested flags

\[
 X_j=Z_{j,0}\subsetneq Z_{j,1}\subsetneq\cdots
       \subsetneq Z_{j,u_j-1}\subseteq B\cap T_j       \tag{4.2}
\]

so that:

1. every `Z_(j,t)` is initially held by an overloaded terminal-tail
   address;
2. no packet ray target lies in any selected source chain;
3. after the lossless fan allocation of Theorem 1.1, the socket of
   Theorem 2.1 fills every selected source deficit in order, unless total
   overload reaches zero earlier.

The final replacement leaves one fresh bottom token in the socket.  Thus
rank two is lossless for any **fixed freely selected STW repair bank**, not
for every prescribed task or every underloaded address simultaneously.

#### Proof

Greedily choose disjoint sets `A_j subseteq T_j` of size `u_j+1`; this is
possible because `H` is fixed, `u_j=O(sqrt(n))`, and every `T_j` has linear
size.  Order `A_j` and let (4.2) be the saturated chain beginning with its
first two elements.  Add one further rank-two subset of `B`, distinct from
every `X_j`, as the final token.  Its complement has rank `n-2`, so it too
belongs to an overloaded terminal-tail donor until the final replacement.

Put all these coordinates into `B`.  For every target `F` in a selected
source chain, also choose one coordinate outside `F` and put it into `B`.
There are only `O(Hd)` such requirements, while
`|B|=r-d=Theta(n)`; after deleting repetitions, extend to the required base
size.  Then `B` is not contained in any selected-source target.  Every ray
target contains `B`, proving item 2.  Choose the remaining packet/collar
labels outside `B`; `n>=r+3d` eventually supplies them.

Every target in (4.2) has rank at most `d+1`.  Hence its complement has rank
at least `n-d-1>=ceil(n/2)+C_0` for large `n`, so STW put it in the high
leftover bank.  Its complemented lower target lies on a terminal address
whose base load is at least `d`; while the target remains there that address
is overloaded.  This proves item 1.

Initialize `C_b(X_1)` with the symmetric fan cover (1.0).  For source `j`,
first put `Z_(j,0)=X_j` in its bottom gap `(emptyset,T_j)`.  After
`Z_(j,0),...,Z_(j,t-1)` have entered that source, put `Z_(j,t)` in the
current gap `(Z_(j,t-1),T_j)`.  This is strict because (4.2) is strict and
`|Z_(j,u_j-1)|<=d+1<|T_j|` for large `n`.  At every step replace the socket
bottom by the next flag member; after the last flag member, replace it by
`X_(j+1)` (or by the final token).  Every replacement fits
`(emptyset,S_1)` because it lies in `B subsetneq S_1`.  The source, boundary,
and terminal addresses are distinct.  Theorem 2.1 completes the induction.
\(\square\)

This theorem is deliberately fixed-`H`.  One rank-two start is needed per
source address, and the shared base has only `binom(r-d,2)` such targets.
For growing `H`, distinct-target Hall and common-base support become new
cuts.  No polynomial or exponential STW leave bound is improved here.

## 5. Two-address literal q1, inherited recurrence, and optional reset

The local no-reset recurrence below independently replays the authoritative
one-ended result in
`MATH_THEOREM_A_K2_PIVOT_ONE_ENDED_PREFIX_EXTENSION_AND_RELATIVE_EROSION_20260801.md`;
the new contribution here is its explicit target-ticket collision ledger and
the socket coupling in Section 6.

Lane A's literal audit distinguishes the sparse split source from its
abstract Johnson collar.  For each adjacent owner pair let `J_i` be the OR
of the native shared `h` source letters.  Four transitions can satisfy

\[
                         J_i\subsetneq V_i\cap V_{i+1}. \tag{5.1}
\]

Their exact missing-coordinate sets are

\[
\begin{array}{c|c}
L_{h-2}\to L_{h-1}&C\cup X_L\\
L_{h-1}\to M_0&X_R-\{x_R\}\\
M_h\to R_0&X_L-\{x_L\}\\
R_0\to R_1&C\cup X_R.
\end{array}                                             \tag{5.2}
\]

The first and fourth are nonempty; the middle two vanish exactly when the
opposite shore is a singleton.  This proves (0.4) for the sparse source and
explains why global-start placement alone does not repair its internal
shared cells.

The four-address source of
`MATH_THEOREM_A_SPLIT_PIVOT_PHYSICAL_COLLAR_AND_BPLUS1_TERMINAL_PATH_20260801.md`
already removes these deficits.  It is not minimal.  The legal-enlargement
envelopes give the following address-minimal family.

### Theorem 5.1 (two-address family and minimum)

For arbitrary `1<=j<h` and `2<=s<=h`, make exactly the two changes (0.5)
in the sparse source.  Then:

1. the owner row and the rank-`r+1` pre-insertion row are unchanged;
2. all `3h` native lower cells and all `3h` spanning upper cells are exact;
3. `X`, both rays, insertion transparency, the owner residence ledger,
   source length, and coordinate support are unchanged; and
4. two modified source positions are necessary among all repairs made only
   by enlarging existing letters while fixing the owner row.

Thus (0.5) supplies a canonical menu of `(h-1)^2` repairs.  This is a
guaranteed menu, not always the exhaustive menu: if `X_R` or `X_L` is a
singleton, the corresponding seam deficit in (5.2) is empty and one extra
boundary position can be legal on that shore.

#### Proof

The singleton `lambda_j` is at source position `h+j-1`.  It belongs to
exactly the owners

\[
 L_{j-1},\ldots,L_{h-1},M_0,\ldots,M_{j-1},           \tag{5.3}
\]

all of which contain `B-{x_R}`.  It lies in both deficient left shared
blocks.  Adding `B-{x_R}` therefore leaves every owner fixed and supplies
both left missing sets.  The pre-row windows replacing central owners by
their adjacent unions also contain `B-{x_R}`.  The `rho_s` calculation is
symmetric: its containing owners are

\[
 M_s,\ldots,M_h,R_0,\ldots,R_{s-1},                  \tag{5.4}
\]

and all contain `B-{x_L}`; its position lies in both right deficient
blocks.  Hence the pre-row is fixed and every missing set in (5.2) is
supplied.

Equivalently, for source owners

\[
 O_t\cap O_{t+1}
   =C_t\cup(a_t\cap a_{t+h+1}),                      \tag{5.5}
\]

and the two additions make (5.5) tight at the four formerly deficient
edges; already tight edges cannot grow past their fixed owner intersection.
Every insertion-born left ray contains `X` together with the adjacent
`C+X_L+lambda_h` letter and hence already contains `B`; the right side is
symmetric.  Thus the extra core in (0.5) changes no ray.  The two letters
adjacent to `X` are unchanged and their union contains `B`, proving
arbitrary-width insertion transparency.  Owner residence follows from the
fixed owner row.

For minimality, the always-nonempty outer left deficit can be supplied only
from the shared range `[h-1,2h-2]`, while the always-nonempty outer right
deficit can be supplied only from `[2h+2,3h+1]`.  The ranges are disjoint,
so one modified position cannot repair both.  \(\square\)

The price has moved to the ambient interface.  Each of the two enlarged
letters must lie below every cap and guard row meeting its source position;
the selected singleton **occurrence** disappears, and every mixed exterior
interval using that position must be replayed.  The singleton target itself
survives only if another literal singleton occurrence exists.  These
permissions do not follow from marginal owner/q1 correctness.

### Theorem 5.2 (inherited algebraic `K2` recurrence)

Keep the logical enriched labels instead of choosing new ones.  On a
plateau, where `h` is fixed and the core becomes `B'=B+beta`, use

\[
                         (j,s)\longmapsto(j,s).        \tag{5.6}
\]

On a deadline jump put `H=h+1` and

\[
 \Lambda'=(\alpha,\Lambda),\qquad P'=(P,\gamma),
 \qquad (j,s)\longmapsto(j+1,s).                     \tag{5.7}
\]

Then the repaired central blocks nest literally:

\[
 A_H^-(j+1)=(\{\alpha\})A_h^-(j),\qquad
 A_H^+(s)=A_h^+(s)(\{\gamma\}),                     \tag{5.8}
\]

while the outer sparse blocks satisfy

\[
 E_H^-=(\{\gamma\})E_h^-,\qquad
 E_H^+=E_h^+(\{\alpha\}).                           \tag{5.9}
\]

Consequently every parent **packet** source letter, including both enriched
full-core letters and every internal opposite-bank singleton backup,
survives literally at a jump.
All child owner, pre-row, ray, and native-q1 formulas are the standard
Pascal formulas.  The enriched positions remain their exact simultaneous
owner/pre-row caps.  No native packet owner/pre, q1, ray, or
maximal-envelope identity forces a fresh-position reset.  Signed residence
is a separate trace condition and has the finite horizon in Theorem 5.3.

The index state never runs out.  If `1<=j<h`, then
`1<=j+1<h+1`; if `2<=s<=h`, then `2<=s<h+1`.  After `t` jumps,
`h-j` is constant, while `s` is unchanged.  A singleton backup already
inside the packet is copied by (5.8)--(5.9).  In particular, if the active
pair was born at a previous jump, its opposite `D^+` and `D^-` singleton
copies persist under every later plateau and jump.  An external backup from
a base scaffold is only a ticket in global `Q`; these local identities do
not transport its child occurrence.

For the canonical interior family the physical source indices are

\[
 p_L=h+j-1,\qquad p_R=2h+s,qquad
 (p_L,p_R)\longmapsto(p_L+2,p_R+2).                  \tag{5.9a}
\]

This `(+2,+2)` rule is not the singleton-shore seam specialization: its
left/right seam positions shift by `+1,+3` respectively.

#### Proof

On a plateau, substituting `B'=B+beta` in the same two maximal-envelope
letters proves (5.6) and the usual common-core owner formulas.  At a jump,
prepending `alpha` to `Lambda` shifts the old `lambda_j` to
`lambda'_(j+1)`, while appending `gamma` to `P` leaves `rho_s` at index `s`.
This proves (5.8); the definitions of the two exterior banks give (5.9).
Taking the required window unions gives
`M'_0=M_0+alpha`, `M'_t=M_(t-1) union M_t`, and
`M'_H=M_h+gamma`, together with the standard left/right collars and rays.
Theorem 5.1 supplies native q1 for the inherited source.  Literal block inclusion
proves preservation of the active source cells and every internal
opposite-bank backup.  \(\square\)

There is therefore no enrichment-**location** reset gate in the algebraic
packet.  Ambient compiler guards can reject a particular inherited position,
and the shared-bank residence clock can expire; both are separate physical
obstructions.  The global transport of all other old targets between Pascal
sectors also remains open.
Literal block nesting is not whole-deck nesting: intervals crossing one of
the four newly inserted block seams can gain `alpha` or `gamma`.  Only rows
inside one embedded block, and the packet rows explicitly checked above,
transport without an additional screened-sector audit.

### Theorem 5.3 (sharp shared-bank residence horizon)

Start at a pairwise-disjoint packet of depth `h_0`.  After `t` deadline
jumps put `h=h_0+t`, and index the jump-born coordinates by birth time
`1<=i<=t`.  Their complete local owner traces are

\[
\begin{aligned}
 \operatorname{tr}(\alpha_i)
   &=0^{t-i}1^{h+1}0^{\,2h_0+2i-1}1^{t-i+1},\\
 \operatorname{tr}(\gamma_i)
   &=1^{t-i+1}0^{\,2h_0+2i-1}1^{h+1}0^{t-i}.
\end{aligned}                                                    \tag{5.10}
\]

The middle zero-run is strictly internal.  Either coordinate is
signed-resident exactly when

\[
                         t\le h_0+2i-2.               \tag{5.11}
\]

Consequently the entire inherited shared bank is resident exactly through

\[
                         t\le h_0.                    \tag{5.12}
\]

The first failure is the oldest pair at jump `t=h_0+1`.  Plateaux do not
change this clock, and changing only the two enrichment sites does not
change any trace in (5.10).

#### Proof

At time `t`, the two source occurrences of either birth-`i` coordinate have
separation

\[
                         \Delta_i=3h_0+t+2i.          \tag{5.13}
\]

One occurrence supplies `h+1` consecutive owner memberships before the
other begins.  Hence the separating internal zero-run has length

\[
        g_i=\Delta_i-(h+1)=2h_0+2i-1.                \tag{5.14}
\]

Signed depth-`h` residence requires `g_i>=h+1`, which is (5.11).  The
strongest row is `i=1`, giving (5.12).  Directly reading the clipped end
runs gives (5.10).  Neither a plateau nor an enrichment-site change moves
the two bank occurrences.  \(\square\)

The minimal literal counterexample is `h_0=2,t=3,h=5`:

\[
 \operatorname{tr}(\alpha_1)=0^2 1^6 0^5 1^3,
 \qquad
 \operatorname{tr}(\gamma_1)=1^3 0^5 1^6 0^2.       \tag{5.15}
\]

The zero-gap has length `5<6` and is internal, so exterior continuation
cannot repair it.  On the actual triangular deadline schedule this third
jump is `d_21=5`, corresponding to odd `k=41` when initialized before the
first `2->3` jump.

An exact bounded clock is

\[
                         \tau=h_0-t.                  \tag{5.16}
\]

Each jump decrements `tau`, each plateau leaves it fixed, and the packet is
resident iff `tau>=0`.  A genuine shared-bank rebase at current depth `b`
would reset the clock and remain safe through depth `2b`; repeated rebases
could use the cadence `b,2b,4b,...`.  No bounded-support rebase is proved
here: it must remove or relocate one occurrence of every expiring shared
label, or discharge the residence row nonflatly.  In a hypothetical rolling
repair, birth pair `i` reaches its first illegal jump at
`t_i=b+2i-1`: service starts before jump `b+1`, and thereafter one old pair
reaches deadline every two jumps.  This is a necessary calendar, not a
compatible bounded-cost construction.

### Corollary 5.4 (bank-overlap and occurrence state)

After `t` inherited jumps the only cross-bank label reuse is

\[
\begin{aligned}
 \Lambda_t&=(\alpha_t,\ldots,\alpha_1,\bar\Lambda),&
 D_t^+&=(\bar D^+,\alpha_1,\ldots,\alpha_t),\\
 P_t&=(\bar P,\gamma_1,\ldots,\gamma_t),&
 D_t^-&=(\gamma_t,\ldots,\gamma_1,\bar D^-).
\end{aligned}                                                    \tag{5.17}
\]

All barred banks and jump labels are otherwise disjoint.  Hence

\[
 \Lambda_t\cap D_t^+=\{\alpha_i\},\qquad
 P_t\cap D_t^-=\{\gamma_i\},                         \tag{5.18}
\]

and every other pair of moving banks is disjoint.  This reuse creates no
owner or q1 target collision: the inherited owner row remains a simple
Johnson path and both q1 palettes remain injective.  It does create the
signed-trace obstruction of Theorem 5.3, as well as occurrence aliases.
Each jump label has two singleton source occurrences unless one
is the active enriched label, in which case its opposite-bank singleton is
the retained backup.  A target matching must select one occurrence of each
singleton target.  Likewise, the two new ray tops at a jump are aliases of
native central lower-q1 targets and are counted once by target value.

Thus the carried label state has bounded **schema**: the active pair, two
backup occurrence addresses, and two alias-selection rules.  One canonical
rule selects every `alpha_i` singleton in `D^+`, every `gamma_i` singleton
in `D^-`, and the native shared occurrence for every ray/q1 equality.  This
removes per-label local choices; an ambient typed guard may instead force a
choice into global `Q`.  Formula (5.17), the ray word, and the right source
boundary still have length growing with `h`.  The scalar clock (5.16) is
bounded-state data, but the missing physical rebase is not supplied.

### Optional fresh reset

One may instead choose

\[
                         \lambda'_1=\alpha,
              \qquad     \rho'_H=\gamma.             \tag{5.19}
\]

This is a valid **static child** repair by Theorem 5.1.  Both newborn
singletons still survive: the sparse jump has a second `{alpha}` in `E_H^+`
and a second `{gamma}` in `E_H^-`.  But (5.19) de-enriches the inherited
positions, so (5.8) fails and parent selected full-core cells and mixed
intervals may disappear.  A fresh reset is therefore optional
reoptimization requiring a retraction/reassignment ledger, not the default
recurrence.

### Three compiler interfaces

Address count alone does not order the repairs.  The exact local comparison
is:

| interface | changed source positions | selected `lambda/rho` singleton occurrences removed | `lambda/rho` singleton tasks needing alternate hosts |
|---|---:|---:|---:|
| four-site seam repair | 4 | 0 | 0 from the `lambda/rho` bank |
| two-site interior repair | 2 | 2 | 0--2, depending on duplicate hosts |
| hybrid repair | 3 | 1 | 0--1, depending on a duplicate host |

The hybrid merges the two deficits on one shore at one singleton position
and uses the two non-singleton seam enrichments on the other.  Every row has
the same owners, pre-row, native q1, rays, and residence.  On the canonical
deadline jump, choosing the fresh pair (5.19) puts the two-site row at zero
unhosted newborn singleton tasks by the opposite-bank copies in (5.10); a one-shore fresh hybrid has the
same property for its one enriched newborn label.  On a plateau, or for an
old `lambda/rho` label with no duplicate singleton occurrence, the warning
is active.  Therefore the two-site interface is address-minimal, not
strictly compiler-better than the four-site interface.

When `X_L,X_R` are both singletons, there are also two seam-position
choices: `{q^-}->B^-` and `{q^+}->B^+`.  They preserve every
`lambda/rho` singleton occurrence, but the two `q` singleton targets still
need their own multiplicity audit.  This is the rank-two specialization of
the complete minimum-position family, not a free global compiler closure.
In particular, `K_4 -> K_2` is a valid local guard-count reduction, not a
literal compiler implication until the singleton and common-cap ledgers
pass.  The inherited `K2` recurrence needs no reset ledger.

Finally, the frozen one-sided right owner/guard export is not the static
socket state (2.1).  A sufficient physical carried-state export must add

\[
 \Xi_R^{\rm carry}=(h_0,t,\tau;j,h-j,s; b;S_1,\ldots,S_{h-1};x;
        a,\ell,c;\mathcal K_{2};\mathcal S_{2};
        \mathcal A;\omega_h;Q),                       \tag{5.20}
\]

where `a,ell,c` give the mutable lower address and load/capacity,
`tau=h_0-t` is the signed-residence lifetime,
`\mathcal K_2` records the two enriched source positions and all incident
cap/guard rows, `\mathcal S_2` records the two singleton backup occurrences,
`\mathcal A` chooses one physical occurrence for every local duplicate
target, `omega_h` is the literal right boundary, and `Q` is the simultaneous
global target/sector/common-cap state.  The cell ledger inside `Q` must
permit `x` to be replaced by the planned `y`.  Only the optional fresh
reset (5.19) adds a de-enrichment replay ledger `\mathcal R`; it does not
reset `tau`.

Without (5.20), left-start placement solves only the clipped left residence
flags and the old right export carries only owner/q1 continuation.  It does
not physicalize the static rotations in Theorem 4.1.  This is the precise
surviving recurrence gate.

## 6. No-reset coupling to the triangular socket

### Theorem 6.1 (exact static target-chain socket)

Suppose the fan has been allocated in the symmetric form

\[
 P_1<\cdots<P_{h-1},\qquad
 C_b(x)=(x<S_1<\cdots<S_{h-1}),qquad x\subsetneq B.  \tag{6.1}
\]

Under the inherited packet recurrence of Theorem 5.2 this remains a legal
two-address chain allocation without any enrichment-site reset.  This
target-chain statement holds algebraically for every `t`; realizing it by
the inherited physical packet additionally requires `tau>=0` or a separate
residence discharge.

* On a plateau,

  \[
      P_i'=P_i+\beta,\qquad S_i'=S_i+\beta,qquad x'=x. \tag{6.2}
  \]

  The socket aperture grows from `(emptyset,S_1)` to
  `(emptyset,S_1+beta)`, so every old replacement target below `S_1` still
  fits.
* On a jump,

  \[
  P_i'=P_i,\ S_i'=S_i\ (i<h),\qquad
  P_h'=M_0,\ S_h'=M_h.                                \tag{6.3}
  \]

  The old aperture `(emptyset,S_1)` is literally unchanged.  The two new
  tops extend the chains to the new capacities; they are aliases of child
  native lower-q1 targets and must be charged once.

Hence every abstract two-step rotation of Theorem 2.1 remains admissible
after either local transition whenever its current bottom and replacement
targets are carried in `Q`.

#### Proof

Equations (6.2)--(6.3) are the exact plateau/jump ray identities.  Since
`x subsetneq B`, one has `x<S_1+beta` on a plateau.  On a jump,
`S_h'=M_h=B+rho[1,h]` strictly contains `S_(h-1)`, and the left calculation
is symmetric.  Theorem 5.2 shows that these ray formulas coexist with the
same inherited enriched sites.  \(\square\)

This is an exact **static compiler-chain** coupling, not yet a physical
source coupling.  Initially the packet supplies literal cells for `X` and
the rays.  After a balancing route replaces the socket bottom by an
arbitrary target `y`, the geodesic source does not automatically contain a
cell equal to `y` at the required typed address.  The mutable occurrence,
release, deadline, and cap data in `Q` are therefore essential.  No-reset
solves enrichment chronology only within the residence horizon; it neither
manufactures the socket's changing literal source cells nor rebases the
shared-bank traces.

### Exact local ticket transition

| ticket | plateau | jump | physical rule |
|---|---|---|---|
| inserted task `X` | same mask | same mask | same literal `[X]` |
| active enriched cells | each gains `beta`; old untagged values move to global `Q` | persist literally | exact maximal envelopes |
| active singleton backups | internal copies persist; external copies are a `Q` hypothesis | same | select one recorded occurrence |
| old ray tickets | gain `beta`; old untagged values need sector hosts | persist | jump adds two q1 aliases |
| central packet q1 | gain `beta`; old untagged values need sector hosts | parent owners become child lower colours; parent upper turns become child owners | native cells, one ticket per value |
| socket bottom `x` (and later `y`) | same target | same target | requires mutable occurrence transport in `Q` |
| fresh jump singletons | -- | two literal copies of each `alpha,gamma` | select one copy |
| shared jump-label traces | unchanged | `tau` decreases by one | physical packet requires `tau>=0` |

Within the packet these are all forced occurrence identifications.  The
simple owner row, injective q1 palettes, cross-shore ray incomparability,
and distinct active labels exclude any further local target collision.
This does not exclude the pre-Hall signed-residence failure of Theorem 5.3.
Collisions with the exterior word remain part of global common `Q`.

## 7. Proof boundary

The new split-core packet therefore yields

\[
 \boxed{\text{lossless two-chain fan + regenerative static socket
 + fixed-}H\text{ STW rank-two routing}.}
\]

It does not yet yield

\[
 \boxed{\text{one literal compiler chronology carrying those rotations}.}
\]

The weakest next theorem is a matching-closed realization of the exported
carried state (5.20), especially mutable-bottom occurrence transport and
the global old-target Pascal-sector/common-cap ledger, together with a
shared-bank residence rebase before `tau` becomes negative.  Fresh
enrichment-site reset does not supply that rebase.

## 8. Independent finite replay

The dependency-free audit

```text
scratch/audit_h2_split_core_triangular_socket_rank2_20260801.py
```

reconstructs the sparse and four-address sources, checks every legal
two-address position through the common owner/pre-row envelope, replays a
literal representative of the complete `(h-1)^2` Cartesian menu, verifies
the four/two/hybrid occurrence tradeoff, checks the two remote newborn
singleton hosts, and replays four consecutive inherited jumps (simplicity,
both palettes, native cells, active locations, and singleton multiplicity)
for every base row through `h=64`.  For every `2<=h_0<=12` it continues one
representative through jump `h_0+1` and checks (5.10)--(5.16), including the
first failing internal zero-gap.  It also verifies the fan, socket aperture,
and rank-two gap criterion.  Its fail-closed status is
`PASS_WITH_SHARP_INHERITED_K2_RESIDENCE_HORIZON`.  The JSON is

```text
scratch/h2_split_core_triangular_socket_rank2_20260801.audit.json
```

The STW statement in Theorem 4.1 is proved symbolically from the frozen
terminal-tail construction; the finite replay is not an extrapolation of
that asymptotic claim.
