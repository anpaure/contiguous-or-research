# Reciprocal `C_8` multilayers: common-base ownership, carrier reciprocity, and the exact inventory ceiling

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let

\[
 B=C_s=\operatorname {Cat}_s,
 \qquad
 \delta_\theta={1\over2}-{1\over\theta}.
\]

The proposed four-to-seven reciprocal-`C_8` layers separate into one
positive theorem and two exact obstructions.

1. **Positive common-base theorem.**  Any root-disjoint family of the
   sealed canonical rectangles
   
   \[
       P1100R\longleftrightarrow P1010R
   \]
   
   may be switched independently, even when the rectangles occur at
   different rooted-subtree boundaries.  The resulting object is one exact
   anchored factor.  Its full ownership components have size two and, for
   `N` switched rectangles,
   
   \[
                         \boxed{\Xi={8N\over B}.}       \tag{0.1}
   \]

2. **Exact inventory/collision obstruction.**  In one fixed canonical
   base, the number of all contextual leaf rectangles over every boundary
   is exactly
   
   \[
      \sum_{p=0}^{s-2}C_pC_{s-p-2}=C_{s-1}.            \tag{0.2}
   \]
   
   Hence no root-disjoint common-base bank contains more than `C_(s-1)`
   rectangles.  In particular four full layers of `C_(s-2)` rectangles
   are already impossible, because
   
   \[
        {C_{s-1}\over C_{s-2}}=4-{6\over s}<4.         \tag{0.3}
   \]
   
   Even granting one perfectly useful marked carrier unit per rectangle,
   the parent demand can be met only if
   
   \[
       \delta_\theta B\le C_{s-1}
       \quad\Longleftrightarrow\quad
       \boxed{\theta\le4+{6\over s-2}}.               \tag{0.4}
   \]
   
   Thus the entire disjoint rooted-subtree leaf library is insufficient
   whenever `theta>=4+epsilon` for fixed `epsilon>0`.  The count is only
   critical in the same width-`O(1/s)` band already isolated in Lane G.

3. **Carrier-sign obstruction.**  Every rectangle is reciprocal.  Its two
   entrance boundary columns move one aggregate unit from the local even
   coordinate `beta` to the adjacent odd coordinate `gamma`; its two exit
   columns move exactly one unit from `gamma` back to `beta`.  At an
   arbitrary cyclic-window depth the exact vector is two forward carrier
   derivatives minus two forward carrier derivatives.  Adjacent-block
   conjugation pushes this complete vector forward; it does not reverse
   only the unwanted exit/collar arm.  Reversing the packet shore negates
   both arms together.

Consequently the known library does not produce four to seven independent
same-pair layers.  Different coordinate conjugates live over different
base factors, overlapping packets cannot be superposed independently, and
their union of root matchings gives no ownership theorem.  If a new common
base with commuting packet involutions were constructed, bounded components
and small `Xi` would be possible; no such construction is presently known.

No coefficient-one conclusion is claimed.

## 1. One rectangle and its reciprocal boundary flags

Use the abstract octahedral rectangle notation

\[
\begin{array}{c|ccc}
 &X_t&X_{t+1}&X_{t+2}\\ \hline
P&Kxy&Kxw&Kzw\\
Q&Kxz&Kyz&Kyw
\end{array}
\longmapsto
\begin{array}{c|ccc}
P&Kxy&Kyz&Kzw\\
Q&Kxz&Kxw&Kyw.
\end{array}                                             \tag{1.1}
\]

The two old exchange sequences are

\[
 \begin{array}{c|cc}
 P&y\mapsto w&x\mapsto z\\
 Q&x\mapsto y&z\mapsto w,
 \end{array}                                            \tag{1.2}
\]

and the new sequences reverse the two exchanges on each row:

\[
 \begin{array}{c|cc}
 P&x\mapsto z&y\mapsto w\\
 Q&z\mapsto w&x\mapsto y.
 \end{array}                                            \tag{1.3}
\]

For the canonical contextual leaf packet, `y=beta=2p+2` and
`z=gamma=2p+3`.  Comparing (1.2) and (1.3) gives the exact four boundary
histograms:

\[
\begin{array}{c|c}
\text{column}&\text{new minus old aggregate}\\ \hline
\text{first deletion}&e_\gamma-e_\beta\\
\text{first insertion}&e_\gamma-e_\beta\\
\text{last deletion}&e_\beta-e_\gamma\\
\text{last insertion}&e_\beta-e_\gamma.
\end{array}                                             \tag{1.4}
\]

Thus the packet has a favourable marked entrance arm only together with
an oppositely oriented exit arm.  This conclusion is local and survives
every common prefix and suffix: those contexts merely adjoin different
physical carrier cores to the four displayed occurrences.

Each affected rooted cyclic coordinate word undergoes one adjacent swap
in its deletion half and one adjacent swap in its insertion half.  Hence

\[
                         d(P)=d(Q)=2.                  \tag{1.5}
\]

## 2. The complete cyclic-window carrier vector

At a fixed proper cyclic interval length, split the common omitted-label
tail into its even and odd lists `E,O`.  Put

\[
             \partial_{\beta}^{\gamma}H
       =e_{H\cup\{\gamma\}}-e_{H\cup\{\beta\}}.       \tag{2.1}
\]

The audited rectangle calculation gives

\[
 \boxed{
 \Delta_q=
   \partial_{\beta}^{\gamma}\operatorname{suf}(O)
  +\partial_{\beta}^{\gamma}\operatorname{suf}(E)
  -\partial_{\beta}^{\gamma}\operatorname{pre}(E)
  -\partial_{\beta}^{\gamma}\operatorname{pre}(O).} \tag{2.2}
\]

The prefix/suffix lengths in (2.2) are the unique lengths prescribed by
the window depth.  Formula (2.2) already includes the two cyclic collars.
At depth one, two terms collide and it reduces to a four-cell rectangle

\[
                         \Delta_1=-e_A+e_B+e_C-e_D,    \tag{2.3}
\]

with `A,B,C,D` distinct.  Therefore

\[
             {1\over2}\|\Delta_1\|_1=2.              \tag{2.4}
\]

At every audited interior depth `2<=q<=s-2`, the eight cells in (2.2)
are distinct and

\[
             {1\over2}\|\Delta_q\|_1=4.              \tag{2.5}
\]

If one forgets the carrier core and remembers only whether the active
coordinate is `beta` or `gamma`, then (2.2) projects to zero: its two plus
derivatives and two minus derivatives cancel.  Hence no uncarried
coordinate marginal can orient this switch.

### Proposition 2.1 (conjugation transports; it does not repair sign)

Let `h` be a coordinate automorphism and conjugate the complete factor,
packet, and physical context.  Then

\[
                         \boxed{\Delta_q^{,h}=h_*\Delta_q.}         \tag{2.6}
\]

In particular an adjacent-block conjugation either fixes the active pair
`{beta,gamma}` or exchanges its two members.  It transports all four
terms of (2.2) simultaneously.  Choosing the opposite packet shore gives
`-Delta_q`; it also reverses all four terms simultaneously.

#### Proof

Every target in (2.2) is obtained from a row/start occurrence by set
intersection followed by adjoining its exterior carrier.  Coordinate
permutations commute with intersection, union, complement, and adjoining
the correspondingly conjugated carrier.  This proves (2.6).  The generators
of the Dyck-coordinate automorphism group are the disjoint swaps
`(2i,2i+1)`, so the last assertion follows. \(\square\)

If only the local packet is relabelled while the exterior carrier is held
fixed, (2.6) is not available: the literal row/start push-forward must be
recomputed.  In particular, the abstract phrase "conjugate carrier" does
not certify a physical sign in a fixed parent.

## 3. Exact cap gain and the absence of a background-independent sign

Let

\[
                         K_c(\mu)=\sum_T(\mu(T)-c)_+
\tag{3.1}
\]

for an integer cap `c`.  For the four-cell rectangle (2.3), the gain from
the displayed orientation is

\[
\begin{aligned}
 G_+(\mu)={}&K_c(\mu)-K_c(\mu+\Delta_1)\\
 ={}&\mathbf1_{\mu(A)>c}+\mathbf1_{\mu(D)>c}
    -\mathbf1_{\mu(B)\ge c}-\mathbf1_{\mu(C)\ge c},   \tag{3.2}
\end{aligned}
\]

while the reverse orientation has

\[
\begin{aligned}
 G_-(\mu)={}&K_c(\mu)-K_c(\mu-\Delta_1)\\
 ={}&\mathbf1_{\mu(B)>c}+\mathbf1_{\mu(C)>c}
    -\mathbf1_{\mu(A)\ge c}-\mathbf1_{\mu(D)\ge c}.  \tag{3.3}
\end{aligned}
\]

Consequently

\[
                         \boxed{\max(G_+,G_-)\le2,}    \tag{3.4}
\]

and the constant is attained when precisely the two removed cells are
above cap and the two added cells are below cap.  There is no nonnegative
universal sign: if all four old loads equal `c`, then

\[
                         G_+(\mu)=G_-(\mu)=-2.          \tag{3.5}
\]

The analogous exact upper bound at an eight-cell depth is four, and all
eight loads equal to `c` make both orientations cost four.  Thus independent
shore orientation does not solve the zero-margin carrier problem.

For pairwise target-disjoint packets, the cap objective and (3.2)--(3.3)
add exactly.  When physical carrier images collide, neither the best signs
nor their gains add; the joined histogram must be evaluated first.

## 4. A constructive disjoint-packet ownership theorem

Let `F` be one fixed anchored exact factor.  A sealed reciprocal packet
`lambda` consists of two old rows, two new rows, and a token set
`T_lambda` such that both shores own every middle-state and adjacent-union
token of `T_lambda` exactly once and own no token outside it.  Both shores
have the same two root ports.

### Theorem 4.1 (root-disjoint reciprocal packets form an exact cube)

Let `L` be any family of contextual canonical rectangles whose two-element
root sets are pairwise disjoint.  Then:

1. their token sets `T_lambda` are pairwise disjoint;
2. either shore may be selected independently in every packet;
3. together with all unchanged rows, every selection is one anchored exact
   factor;
4. in the full ownership overlay, every switched packet is one component
   of side size two and every unchanged row is isolated; and
5. if two cube vertices differ on `N` packets, then
   
   \[
                            \boxed{\Xi={8N\over B}.}    \tag{4.1}
   \]

#### Proof

The old rows of `F` partition both token shores.  Therefore disjoint old
root sets own disjoint token sets.  Sealedness says that the new shore of
one rectangle owns exactly the same token set as its two old rows.  This
proves Items 1--3.

Inside a nontrivial rectangle, the exchanged middle states give cross-owner
edges between its two roots, while the common port tokens give the two
diagonal shore edges.  Hence its full overlay is connected and has side
size two.  No ownership edge can leave its sealed token set.  This proves
Item 4.  Finally (1.5) gives `D_K=2+2=4`, so one component contributes
`b_KD_K=8` to `B Xi`.  Summation proves (4.1). \(\square\)

This theorem is the maximal automatic ownership statement.  If two
packets share an old root, their sealed token sets overlap in the complete
token set of that old row.  Taking both new shores as an independent union
then owns those overlap tokens twice (and removes the old row only once).
Thus overlapping packets are not independent Boolean coordinates.  They
may participate in a separately proved joint strand recombination, but a
union of their root edges is not such a proof.

## 5. The exact leaf inventory and the four-layer collision

At boundary `p`, the contextual canonical rectangles are indexed by

\[
                         (P,R)\in D_p\times D_{s-p-2},
\tag{5.1}
\]

and their number is `C_pC_(s-p-2)`.  Summing over every possible rooted
boundary gives the exact Catalan convolution

\[
 \boxed{
 \#\{\text{all common-base contextual leaf rectangles}\}
 =\sum_{p=0}^{s-2}C_pC_{s-p-2}=C_{s-1}.}              \tag{5.2}
\]

This counts all rectangles, before deleting collisions.  Hence every
root-disjoint selection has size at most `C_(s-1)`.  Since

\[
 {C_{s-1}\over C_{s-2}}
 ={2(2s-3)\over s}=4-{6\over s},                      \tag{5.3}
\]

there do not exist four root-disjoint full layers, each containing
`C_(s-2)` standard leaf rectangles, in one common canonical base.  A
fortiori, five, six, or seven such layers do not exist.

One marked entrance carrier can move at most one useful unit per rectangle
by (1.4).  Therefore the exact optimistic common-base supply is at most
`C_(s-1)`.  Comparing with `delta_theta B` gives

\[
 \delta_\theta\le{C_{s-1}\over C_s}
 ={s+1\over2(2s-1)}.                                  \tag{5.4}
\]

Solving (5.4) yields precisely

\[
                         \theta\le{2(2s-1)\over s-2}
                         =4+{6\over s-2},              \tag{5.5}
\]

which proves (0.4).  This bound grants root disjointness, perfect target
separation, and perfect cap efficiency to every available rectangle.  It
is therefore an obstruction before the carrier-sign difficulty of
Section 3.

If `N` packets are selected, Theorem 4.1 gives `Xi=8N/B`.  Even the
optimistic inventory maximum has

\[
                         \Xi\le8{C_{s-1}\over C_s}=2+O(s^{-1}),      \tag{5.6}
\]

so variance is not the obstruction.

## 6. Why adjacent-block conjugates do not create common-base layers

Let `h` lie in the full Dyck-coordinate automorphism group

\[
 H_s=\langle(2i\ 2i+1):1\le i<s\rangle.
\tag{6.1}
\]

Conjugating a packet of `F` produces a sealed packet of the conjugate base
`hF`:

\[
                         hF\longleftrightarrow h\tau_pF.             \tag{6.2}
\]

It does not produce an additional independently selectable packet of the
original base `F`.  Different choices of `h` in (6.2) generally have
different old token owners.  Combining their root matchings therefore
does not establish either lower-state ownership or adjacent-union
ownership.

There are only two safe ways to use conjugation.

1. Fix one `h` globally and conjugate the entire common-base cube of
   Theorem 4.1.  The inventory remains exactly `C_(s-1)` and the carrier
   vectors are the push-forwards (2.6).
2. Construct a new common factor containing packets from several
   conjugate bases and prove its complete token ledger directly.  No such
   factor follows from coordinate conjugacy alone.

The same issue appears dynamically.  Along a path of whole-factor
conjugates `F^(g_0),...,F^(g_t)`, the signed histograms telescope:

\[
 \sum_{j=0}^{t-1}
   \bigl(\mu(F^{g_{j+1}})-\mu(F^{g_j})\bigr)
 =\mu(F^{g_t})-\mu(F^{g_0}).                          \tag{6.3}
\]

Repeated traversal of parallel adjacent-block edges cannot accumulate
carrier beyond the two endpoint factors.

## 7. Joined matchings and component size

Suppose, beyond the proved common-base theorem, that several packet layers
have somehow been realized jointly.  Contract the common root-port edges.
The full ownership components contain the connected components of the
union of their root matchings.  Therefore the authoritative moment is

\[
                         B\Xi=\sum_Kb_KD_K,            \tag{7.1}
\]

not the sum of the separate layer moments.

The number `u` of matching layers gives no component bound.  For `u=1`,
components have size at most two.  For every `u>=2`, the universal maximum
component size on `B` roots is exactly `B`: two partial matchings can be
chosen as the alternating edges of one spanning path.  Thus bounded layer
count alone permits a giant component.

If the layer involutions are globally defined, preserve one common domain,
and commute, then their root orbits have size at most `2^u`.  This is a
valid sufficient condition, but contextual leaf involutions are partial
and overlapping leaf rotations need not commute.  The audited smallest
overlapping matching-pure `C_8` pair already fails the strand test by
closing an internal cycle in either order.

If components have side size at most `L`, coordinate-position inversion
blocks are disjoint, and every incident reciprocal packet contributes its
two adjacent row swaps without cancellation, then

\[
 \Xi\le {4LN\over B},                                  \tag{7.2}
\]

because the sum of rooted distances is `4N`.  For the root-disjoint cube
`L=2`, (7.2) is equality and recovers (4.1).  Without the commuting or
root-disjoint hypothesis, neither (7.2) nor bounded components is
automatic.

## 8. Proved boundary and exact redirect

What is proved:

1. the reciprocal entrance/exit flag table (1.4) and full carrier vector
   (2.2);
2. covariance of that vector under genuine physical conjugation, with no
   one-arm sign reversal;
3. exact best-orientation cap formulas (3.2)--(3.5);
4. simultaneous legality and `Xi=8N/B` for every root-disjoint common-base
   family;
5. the exact `C_(s-1)` inventory ceiling, four-layer collision (5.3), and
   threshold `theta<=4+6/(s-2)`;
6. the common-base and joined-matching obstructions.

The surviving constructive lemma is narrower than “take four conjugate
layers”:

> Construct one anchored exact factor pair containing more than
> `C_(s-1)` sealed reciprocal packets, or packets with more than one
> favourably signed marked carrier unit each, such that their full
> ownership components are uniformly bounded and their complete physical
> carrier rectangles satisfy the target-specific hinge inequality after
> all collisions.

Standard leaf shifts cannot meet this lemma beyond the critical band;
coordinate conjugation alone does not put several shifted libraries on one
base.  A new non-leaf packet or a directly audited joint factor is needed.

