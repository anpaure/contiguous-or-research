# Zero-block collapse of the canonical birail Hall defect

Date: 2026-08-01  
Status: unconditional abstract theorem and exact restricted-graph reduction;
conditional identification of the folded-C8 target antidiagonals.  It does
not plant the host, lift the antidiagonals to physical addresses, transport
the background compiler unconditionally, or bound the regenerative length
charge.  Section 3.1 gives conditional exact transport once an already
admissible typed block refinement is present.

## 0. Outcome

Put `m=d-1`, `N=2m`, and suppose both terminal threshold multisets are

\[
                  \{0^m,1,2,\ldots,m\}.               \tag{0.1}
\]

For a pairing `pi`, let

\[
 C_\pi(a,c)=\#\{i:x_i\le a,\ y_{\pi(i)}\le c\},
 \qquad
 \delta(\pi)=\max_{a,c}(C_\pi(a,c)-a-c)_+,            \tag{0.2}
\]

and let

\[
 t(\pi)=\#\{i:x_i=0,\ y_{\pi(i)}=0\}.                 \tag{0.3}
\]

Then, for every pairing--not only an antitone one,

\[
                         \boxed{\delta(\pi)=t(\pi).}   \tag{0.4}
\]

In fact, (0.4) needs only the **simple-positive property**: on each shore,
every positive integer threshold occurs at most once.  The zero
multiplicities, positive supports, and the two shore sizes need not have the
canonical form (0.1), provided a full pairing is defined.

Thus arbitrary restrictions on the physically reachable pairing set do not
restore a positive-threshold sorting problem.  The only abstract terminal
cost is the number of forced zero-to-zero pairs.

## 1. Exact proof

At `(a,c)=(0,0)`, equation (0.2) gives

\[
                         \delta(\pi)\ge t(\pi).        \tag{1.1}
\]

Fix any other corner `(a,c)`.  Apart from the `t(pi)` zero--zero pairs,
every counted pair has either a positive left threshold in `{1,...,a}` or a
positive right threshold in `{1,...,c}`.  There is at most one ticket of
each positive threshold on either shore.  Charge a pair to its positive
left threshold when one exists, and otherwise to its positive right
threshold.  At most `a+c` pairs are charged.  Hence

\[
                         C_\pi(a,c)\le t(\pi)+a+c.     \tag{1.2}
\]

Equations (1.1)--(1.2) prove (0.4).

The same proof establishes the stated simple-positive generalization.  The
number of distinct positive integers at most `a` is at most `a`, regardless
of gaps in the support; similarly on the right.  It also covers corners
beyond `m`, since there are then at most `m<=a` or `m<=c` positive threshold
tickets on the corresponding shore.

## 2. Arbitrary structural zeros

Let `H` be any bipartite graph of physically allowed pairings, with shores

\[
 L=L_0\dot\cup L_+,
 \qquad
 R=R_0\dot\cup R_+,
 \qquad
 |L_0|=|L_+|=|R_0|=|R_+|=m,                           \tag{2.1}
\]

where the zero-threshold tickets are `L_0,R_0`.

### Theorem 2.1 (cross-matching criterion)

There is a zero-defect perfect pairing in `H` if and only if both

\[
                     H[L_0,R_+]
 \quad\hbox{and}\quad H[L_+,R_0]                       \tag{2.2}
\]

have perfect matchings.

#### Proof

By (0.4), zero defect is equivalent to avoiding every `L_0 R_0` edge.  All
`m` vertices of `L_0` must then use the only `m` vertices in `R_+`, so those
edges are a perfect matching.  The unused vertices are exactly `L_+` and
`R_0` and must form the other perfect matching.  The converse follows by
taking the union of the two cross matchings. \(\square\)

Therefore the former southwest-corner family reduces, on the canonical
marginals, to the two ordinary Hall systems for the cross graphs.  No
reachability of the antitone permutation and no sorting of positive labels
is required.

If `H` has a perfect matching, put cost one on `L_0 R_0` edges and zero on
all other edges.  Then its exact birail deficiency is the min-cost perfect
matching value

\[
 \lambda_{\rm ray}(H)=
 \min_{M\text{ perfect in }H}|M\cap(L_0\times R_0)|.  \tag{2.3}
\]

Equivalently, with unrestricted real dual variables,

\[
 \lambda_{\rm ray}(H)=
 \max\left\{
   \sum_{u\in L}\alpha_u+\sum_{v\in R}\beta_v:
   \alpha_u+\beta_v\le c_{uv}\ (uv\in E(H))
 \right\}.                                             \tag{2.4}
\]

This is ordinary bipartite matching duality.  If no perfect matching exists,
the value is `+infinity` and the formula is not invoked.

### Robust scope

For arbitrary multiplicities, define the positive repetition excesses

\[
 e_L=\sum_{s\ge1}(\mu_L(s)-1)_+,
 \qquad
 e_R=\sum_{s\ge1}(\mu_R(s)-1)_+.                    \tag{2.5}
\]

The same charging argument gives the useful uniform estimate

\[
                    t(\pi)\le\delta(\pi)
                    \le t(\pi)+e_L+e_R.              \tag{2.6}
\]

Indeed at most `a+e_L` counted pairs can be charged to positive left
thresholds at a corner `(a,c)`, and at most `c+e_R` to positive right
thresholds.  Thus a bounded number of repeated positive tickets creates
only bounded extra defect.

If deleting at most `e` exceptional paired indices leaves the canonical
property that each positive threshold occurs at most once on each shore,
then the same charging proof gives

\[
                         \delta(\pi)\le t(\pi)+e.      \tag{2.7}
\]

The precise deletion formulation is needed; an arbitrary perturbation of
the entire marginal multiplicities is not covered merely because it changes
`e` numerical values.

## 3. Folded-C8 target antidiagonals

Suppressing the fixed literal core, the four phase rays are

\[
\begin{aligned}
 P_0(j)&=K\cup\{z,a_3\}\cup F[1,j],
 &S_0(q)&=K\cup\{z,a_1\}\cup F[q,d],\\
 P_1(j)&=K\cup\{z,a_1\}\cup F[1,j],
 &S_1(q)&=K\cup\{z,a_3\}\cup F[q,d],
\end{aligned}                                           \tag{3.1}
\]

for `1<=j<d` and `2<=q<=d`.  The two antidiagonals

\[
 P_0(j)\longleftrightarrow S_1(j+1),
 \qquad
 P_1(j)\longleftrightarrow S_0(j+1)                    \tag{3.2}
\]

are bijections of the two ray families.  Directly,

\[
\begin{aligned}
 P_0(j)\cap S_1(j+1)&=K\cup\{z,a_3\},&
 P_0(j)\cup S_1(j+1)&=K\cup\{z,a_3\}\cup F,\\
 P_1(j)\cap S_0(j+1)&=K\cup\{z,a_1\},&
 P_1(j)\cup S_0(j+1)&=K\cup\{z,a_1\}\cup F.
\end{aligned}                                           \tag{3.3}
\]

Thus the set-value algebra supplies two constant-cap antidiagonal
candidates of exactly the form suggested by Theorem 2.1.

This is not yet a physical cross matching.  More sharply, an abstract
threshold pairing such as `(P_0(j),S_1(j+1))` is a **paired two-coordinate
ticket**: its prefix and suffix entries are two adjacent disjoint interval
cells, and in (3.2) they live in opposite phase words.  It is not one
right-hand compiler cell of capacity one.  Treating it as one cell both
undercounts the required physical cell consumption by a factor of two and
mixes incompatible endpoint states.

The threshold-pairing vertices are occurrence-labelled tickets, whereas
(3.2)--(3.3) are identities of target values.  To use them one must prove
either two simultaneous cell banks in one endpoint state or a
matching-closed transport between the phase states.  Concretely:

1. the four occurrence families are literally the `L_0,L_+,R_0,R_+`
   shores of one terminal robust-core state;
2. both coordinates of every selected ticket have distinct legal physical
   cells in compatible complete cap states;
3. those two cell banks are disjoint from one transported background compiler
   matching; and
4. the host/cut state is owner-legal, upper-safe, resident, and recycled
   with bounded total `chi`.

The existing two-host packet already gives a phasewise diagonal matching
for its local `2d-2` ray targets.  The new theorem is complementary: under
arbitrary structural zeros it identifies the exact weaker abstract terminal
criterion and eliminates the need for a global comparator network.  It does
not turn a paired threshold ticket into one physical cell.

### 3.1 Full-block transport removes a separate background-Hall gate

There is a stronger conclusion when the typed host rail is already present
as actual old source letters.  Replacing an old letter `X` by a consecutive
nonempty block with the same total union has an injective full-block lift on
old physical intervals.  Every lifted interval has exactly its old OR.
Every genuinely new ray occurrence is a side cell, hence is outside the
full-block image.

Consequently, suppose an old target-to-cell matching is restricted to the
targets not reassigned to the new ray bank and remains guard/deadline
admissible after the refinement.  If the common-cap contraction is exact
(in the usual notation, the transported subblocks have total union equal to
the old block), then its full-block lifts remain a matching and are
automatically cell-disjoint from the ray diagonal/cross matching.  No new
residual Hall argument is needed for that pure refinement.  This is exactly
the local zero-response theorem already proved for the two-host packet.

The qualification "admissible after the refinement" is essential.  It is
not automatic when the purported host must first be planted by changing the
owner chronology, maximal erosion, deadline state, or common cap.  In that
case the planting/rethread itself may invalidate old matching cells.  Thus
the remaining background issue is part of **host embedding**, not an
independent ray-pairing problem once an actual typed host exists.

## 4. Correct conditional OR consequence

Let a terminal safe chronology have:

* a transported background bank with deletion number at most `C`;
* the canonical ray marginals (0.1);
* literal cross matchings (2.2) using cells disjoint from the background;
* upper defect `u`; and
* true uncontracted length charge `chi`.

Then the ray bank contributes zero additional matching deficiency, so the
correct serial bound gives

\[
                         \nu(k)\le B(k)+u+\chi+C.      \tag{4.1}
\]

This removes positive-threshold comparator transport from the remaining
theorem.  For a literal pure block refinement, full-block transport supplies
the background linkage automatically.  What remains is therefore the
phase-common/clipped host **embedding** (including admissibility of those
transported cells), the addressed ray bank/cut sidecars, and
nonaccumulating regeneration.  The known two-host packet already supplies
the addressed ray diagonal once that host is embedded; the two cross
matchings are the weaker criterion needed by alternative structurally
restricted realizations.
