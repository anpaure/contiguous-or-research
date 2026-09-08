# Multiway long-block pair-omission atlas: exact middle integrality, phase abundance, and the owner-recycling gate

Date: 2026-07-25

## 0. Verdict

Let

\[
 n=2m+1,\qquad
 W=\binom{n}{m},\qquad
 T=\binom{n}{m-1}=\frac{m}{m+2}W.
\tag{0.1}
\]

This note proves two genuine multiway pair-omission atlases.

1. **A common-middle long-block atlas.**  Break the proved first-avoided
   matching into blocks of length at most \(m-H\).  Every block has a set
   \(C\) of \(H+2\) coordinates disjoint from all of its lower targets and
   all of its middle owners.  Conjugating the whole block by an arbitrary
   permutation of \(C\) gives

   \[
      \binom{H+2}{2}>2
   \]

   literal omitted-pair labels for every lower target in the block, while
   fixing the complete lower--middle matching.  The choices are independent
   between blocks.  If

   \[
      \frac{H\log ^2m}{m}\longrightarrow0,
   \tag{0.2}
   \]

   the number of physical selected runs is \(o(W/H)\), and the resulting
   literal word has length \(W+o(W)\).

2. **A global active-pair endpoint atlas.**  With
   \(s=\lceil20\log m\rceil\) active disjoint pairs, all but \(o(W/H)\)
   lower targets have any prescribed fixed number of active omitted-pair
   alternatives.  A fixed signature-cell refinement of the active local
   factors supports exact lower-saturating, middle-simple multiway corners,
   all with \(o(W/H)\) runs.  This is a uniform static-corner bound; no
   cumulative short-recourse theorem is asserted.

Neither result splits every low-multiplicity upper collision.  The failure
is not a shortage of phases.  If a block phase fixes its central owner path,
then a depth-\(q\) upper occurrence can change only when its owner witness
crosses a block seam.  With \(b\) directed seams, at most \(qb\) upper
occurrences move.  Hence, for every fixed multiplicity cutoff \(K\),

\[
 D^{\rm new}_{q}
 \ge
 D_{q,\le K}-(K-1)qb,
\tag{0.3}
\]

where \(D_{q,\le K}\) is the old number of unordered collision pairs lying
in load classes \(2,\ldots,K\).  Thus \(b=o(W/H)\) cannot remove an
\(\Omega(W)\) bounded-multiplicity collision census at any \(q\le H\).

At \(q=1\) this extends beyond aligned blocks.  Two low-run tight path
covers can change a first-upper occurrence only at a path endpoint or at a
lower target whose unordered predecessor/successor pair is genuinely
rewired.  Therefore complete removal of a linear bounded-multiplicity
first-upper defect requires \(\Omega(W)\) genuine lower-neighbour changes.

This is an exact obstruction to the proposed *aligned* long-block phase
mechanism, not an obstruction to constant one.  A different low-run global
path cover may rewire a positive density of owner adjacencies.  Constructing
such a cover while controlling all depths is the remaining positive gate.

## 1. Literal token and run conventions

Let (P\in\binom{[n]}2) be an omitted pair and let

\[
 \pi=(x_0,\ldots,x_{2m-2})
\tag{1.1}
\]

be a cyclic order of (Q_P=[n]\setminus P).  With cyclic indices, put

\[
 S_i=I_\pi(i,m-1),\qquad
 Y_i=I_\pi(i-1,m).
\tag{1.2}
\]

The predecessor token at (i) is the lower--middle edge

\[
 e(P,\pi,i)=(S_i,Y_i).
\tag{1.3}
\]

Its signed flags at depth (q) are

\[
 L_q(i)=I_\pi(i+q-1,m-q),\qquad
 U_q(i)=I_\pi(i-1,m+q).
\tag{1.4}
\]

For consecutive middle owners these have the intrinsic descriptions

\[
 L_q(i)=\bigcap_{r=0}^{q}Y_{i+r},
 \qquad
 U_q(i)=\bigcup_{r=0}^{q}Y_{i+r}.
\tag{1.5}
\]

Only the upper identity will be used below.  It is immediate from the
cyclic windows: (Y_i,\ldots,Y_{i+q}) successively add the (q) right
collar coordinates to (Y_i).

For a selected token system (M), (J(M)) denotes the number of maximal
cyclic intervals of selected starts over all physical source rows; a
nonempty full cyclic row is counted as one run.  The already audited
literal collar construction turns (T) selected tokens in (J) physical
runs into a contiguous-OR word of length at most

\[
 T+(2H+1)J+O(1).
\tag{1.6}
\]

The proved first-avoided matching (M_0) is lower-saturating and
middle-simple, and satisfies

\[
 J_0:=J(M_0)=O\!\left(\frac{W\log ^2m}{m}\right).
\tag{1.7}
\]

No divisibility is suppressed in (0.1), and no fractional token is used in
this report.

## 2. The exact \(\operatorname{Sym}(C)\) block atlas

Fix (1\le H<m), and put

\[
 g=H+2,\qquad \ell=m-H.
\tag{2.1}
\]

Break each physical run of (M_0) into consecutive nonempty blocks of at
most \(\ell\) tokens.  If (K) is the total block count, then exactly

\[
 K
 =\sum_{R}\left\lceil\frac{|R|}{\ell}\right\rceil
 \le J_0+\frac{T}{\ell}.
\tag{2.2}
\]

Here and below a harmless strict improvement caused by integral ceilings
is not used.

### Theorem 2.1 (common-middle multiway block atlas)

Let (I=[a,b]) be one of the blocks, of size
(s=b-a+1\le\ell), in a row \(\pi\) omitting the pair (A).  Set

\[
 R_I=\bigcup_{i=a}^{b}Y_i.
\tag{2.3}
\]

Then

\[
 R_I=I_\pi(a-1,m+s-1),
 \qquad
 |[n]\setminus R_I|=m+2-s\ge H+2.
\tag{2.4}
\]

The complement contains (A) and at least (H) consecutive row
coordinates immediately after (R_I).  Call the first (H) of those
coordinates

\[
 G_I=(z_1,\ldots,z_H)
\tag{2.5}
\]

and put

\[
 C_I=A\mathbin{\dot\cup}\{z_1,\ldots,z_H\}.
\tag{2.6}
\]

For every \(\sigma\in\operatorname{Sym}(C_I)\), extended identically on
([n]\setminus C_I), replace the block by the corresponding segment of
the conjugate row \(\sigma\pi\).  Then:

1. every (S_i) and (Y_i), (i\in I), is fixed;
2. the segment is a literal row segment omitting
   \(B_\sigma=\sigma(A)\);
3. choices of \(\sigma\) are independent between blocks, and every corner
   has exactly the same lower-saturating, middle-simple matching as (M_0);
4. the omitted-pair labels seen by every lower target in (I) range over
   all

   \[
      \binom{C_I}{2},
   \]

   hence over exactly \(\binom{H+2}{2}\) alternatives;
5. every corner has at most (K) physical runs.

#### Proof

Because (s\le m-H<m), the (m)-windows
(Y_a,\ldots,Y_b) do not wrap around the whole local row.  Their union is
the interval in (2.4), of length (m+s-1\).  Since (A) is absent from
the local row, it belongs to the complement; the local-row part of the
complement has size (m-s\ge H).  This proves (2.4)--(2.6).

The support of \(\sigma\) is disjoint from (R_I), so it fixes every
(S_i\subset Y_i\subset R_I).  Conjugating an exact local factor on
([n]\setminus A) by \(\sigma) gives an exact local factor on
([n]\setminus\sigma(A)), and \(\sigma\pi) is one of its literal rows.
Thus all block phases have the same central token edges.

It follows immediately that arbitrary independent choices preserve the
complete central matching.  The symmetric group on (C_I) is transitive
on its two-subsets, so the omitted pair assumes every value in
\(\binom{C_I}{2}\).  Finally, each chosen block is rendered as one literal
row segment, giving at most one selected run per block.  \(\square\)

The theorem directly constructs literal segments.  It does not require
all blocks bearing the same omitted pair to lie in one globally
preselected local factor.  This is permitted precisely because the output
is a literal contiguous-OR word, not a fractional average of local
factors.

## 3. Exact nested chronology of a block phase

The multiway phase is not a separate choice at each depth.  One
permutation \(\sigma\) controls the entire nested flag packet.

### Proposition 3.1 (triangular upper packet)

Let (i=b-r), where (0\le r<s), and let (1\le q\le H).
Every lower flag of the token at (i) is fixed.  For its upper flag:

- if (q\le r), then (U_q(i)\subset R_I) and it is fixed;
- if (q>r), put (h=q-r) and

  \[
     Z_h=\{z_1,\ldots,z_h\}.
  \tag{3.1}
  \]

  Then

  \[
     U_q(i)\cap C_I=Z_h,
     \qquad
     U_q^\sigma(i)
      =\bigl(U_q(i)\setminus Z_h\bigr)\cup\sigma(Z_h).
  \tag{3.2}
  \]

Consequently the cell ((i,q)) has exactly

\[
 \binom{H+2}{h}
\tag{3.3}
\]

different upper targets across the phase orbit, and the sets at different
depths are nested under the same \(\sigma\).

#### Proof

The right endpoint of (R_I) is the last coordinate of (Y_b).  The
window (U_q(b-r)) extends (q-r) positions beyond this endpoint, which
are exactly (z_1,\ldots,z_{q-r}).  Its remaining coordinates lie in
(R_I) and are fixed.  This proves (3.2).  The symmetric group on
(C_I) is transitive on (h)-subsets, proving (3.3).  Since
(Z_1\subset\cdots\subset Z_H), their images under one \(\sigma\) remain
nested.  Lower flags never extend past the right endpoint of (Y_b), so
they lie in (R_I).  \(\square\)

At depth (q), only the last (q) tokens of a block can vary.  Therefore

\[
 |\{S:U_q^\sigma(S)\text{ depends on }\sigma\}|\le qK,
\tag{3.4}
\]

and, through depth (H),

\[
 \begin{aligned}
 |\{S:\text{some upper flag of }S\text{ varies}\}|&\le HK,\\
 \#\{(S,q):U_q(S)\text{ varies}\}
 &\le\frac{H(H+1)}2K.
 \end{aligned}
\tag{3.5}
\]

## 4. Exact boundary and word-length ledger

Combining (1.7) and (2.2),

\[
 K\le
 O\!\left(\frac{W\log ^2m}{m}\right)
 +\frac{mW}{(m+2)(m-H)}.
\tag{4.1}
\]

Under (0.2), (H=o(m)), and hence

\[
 K=O\!\left(\frac{W\log ^2m}{m}\right)=o(W/H).
\tag{4.2}
\]

The literal collar ledger (1.6) gives, uniformly over all corners,

\[
 \begin{aligned}
 |w|
 &\le T+(2H+1)K+O(1)\\
 &=W-\frac{2W}{m+2}+o(W)
  =W+o(W).
 \end{aligned}
\tag{4.3}

Thus the atlas is integral, common-middle, genuinely multiway, and
constant-one compatible at the boundary scale.  Equation (3.4), however,
already signals that most of its upper flags are rigid.

## 5. A global active-pair signature atlas

The preceding construction gives many phases to **every** lower target but
acts only at block collars.  A complementary construction gives many
global first-avoided endpoints while keeping one fixed boundary atlas.

Fix (s\ge2) disjoint active pairs
(P_1,\ldots,P_s).  For each (a), fix an exact local factor
(F_a) on ([n]\setminus P_a).  In a row of (F_a), refine the cyclic
start set according to the complete active avoidance signature

\[
 \chi(S)=
 \bigl({\bf1}_{\{S\cap P_h=\varnothing\}}\bigr)_{h=1}^{s}.
\tag{5.1}
\]

These maximal constant-signature intervals are the signature cells.

### Lemma 5.1 (sharp active boundary count)

In a fixed row of (F_a), the signature has at most (4(s-1)) boundary
edges.  An arbitrary union of signature cells therefore has at most
(2(s-1)) selected cyclic runs.  Across all active factors,

\[
 J_{\rm act}\le2s(s-1)R_m,
\qquad
 R_m=\operatorname{Cat}_{m-1}
 =\frac1{2m-1}\binom{2m-1}{m-1}.
\tag{5.2}
\]

Moreover

\[
 \frac{R_m}{W}
 =\frac{m+1}{2(2m-1)(2m+1)},
\tag{5.3}
\]

so exactly

\[
 \frac{HJ_{\rm act}}W
 \le
 \frac{Hs(s-1)(m+1)}{(2m-1)(2m+1)}.
\tag{5.4}
\]

#### Proof

For a fixed coordinate pair (P_h), the starts at which a cyclic
((m-1))-window avoids (P_h) form the intersection of two circular
arcs, hence at most two cyclic intervals.  Its indicator changes at most
four times.  The bit for (P_a) is constantly one in (F_a), leaving
(s-1) changing bits.  This gives at most (4(s-1)) signature boundaries.

On a cyclic row with (B>0) cell boundaries, an arbitrary binary union of
the cells has at most (B/2) selected runs.  If (B=0), it has at most one
run, which is also at most (2(s-1)).  Every local exact factor has (R_m)
rows.  Summing over the (s) factors proves (5.2).  Formula (5.3) follows
by cancelling factorials, and (5.4) follows from (5.2).  \(\square\)

Let the order of the inactive pairs be fixed.  Every priority order of the
active pairs gives a first-avoided matching: on a signature cell in factor
(a), it takes the whole cell exactly when (a) is the earliest avoided
active pair.  Lower targets avoiding no active pair use the common fixed
tail.  Thus all priority endpoints live in one signature-cell system.

### Theorem 5.2 (multiway overlay integrality)

Let (M^1,\ldots,M^r) be any finite collection of these priority endpoint
matchings.  Form the coloured bipartite union graph on lower and middle
vertices.  Join two connected components whenever, in some colour, they
contain tokens from the same physical signature cell, and take transitive
closure.  Call the resulting unions macrocomponents.

Choose one colour independently on every macrocomponent and retain that
colour's matching edges there.  Every resulting corner:

1. saturates every lower target exactly once;
2. is middle-simple;
3. occupies, in every physical row, a union of complete signature cells;
4. has

   \[
      J\le J_{\rm tail}+2s(s-1)R_m.
   \tag{5.5}
   \]

#### Proof

In an ordinary connected component of the coloured union, the restriction
of every colour saturates all lower vertices of that component and uses
only middle vertices of the same component.  Choosing one colour therefore
gives a matching on that component.  Different components have disjoint
middle vertex sets, so independent choices remain middle-simple.

Joining components only reduces the number of independent choices and
cannot harm this argument.  The additional joining rule ensures that all
edges of one colour lying in one physical signature cell receive one common
choice.  Since an endpoint occupies either the whole cell or none of it,
every corner also occupies the whole cell or none.  Lemma 5.1 gives the
active run bound; the tail is common to all endpoints.  \(\square\)

Macrocomponents can be giant.  The theorem proves exact integrality and a
uniform boundary atlas; it does **not** prove that phase choices remain
independent at individual lower targets, nor that an arbitrary compiled
walk between corners has small cumulative carrier cost.

## 6. Almost every target has many active alternatives

For a lower target (S), put

\[
 Z_s(S)=|\{a\le s:S\cap P_a=\varnothing\}|.
\tag{6.1}
\]

### Proposition 6.1 (exceptional-family bound)

For every fixed positive integer (r), there is a constant (C_r) such
that

\[
 \bigl|\{S\in\tbinom{[n]}{m-1}:Z_s(S)<r\}\bigr|
 \le
 C_rT\sqrt m\,s^{r-1}(3/4)^s.
\tag{6.2}
\]

#### Proof

Include each coordinate independently with probability

\[
 p=\frac{m-1}{2m+1}.
\tag{6.3}
\]

The events of avoiding the (s) disjoint active pairs are independent,
each with probability

\[
 \rho=(1-p)^2=\left(\frac{m+2}{2m+1}\right)^2>\frac14.
\tag{6.4}
\]

Thus their count is \(\operatorname{Bin}(s,\rho)\).  Elementary Stirling
bounds at the mean give an absolute (c>0) such that

\[
 \Pr(|X|=m-1)\ge c/\sqrt m.
\tag{6.5}
\]

Conditioned on this event, (X) is uniform on
(\binom{[n]}{m-1}).  Therefore

\[
 \begin{aligned}
 \Pr(Z_s<r\mid |X|=m-1)
 &\le \frac{\sqrt m}{c}
   \sum_{j=0}^{r-1}\binom{s}{j}\rho^j(1-\rho)^{s-j}\\
 &\le C_r\sqrt m\,s^{r-1}(3/4)^s.
 \end{aligned}
\tag{6.6}
\]

Multiplication by (T) proves (6.2).  \(\square\)

Take (s=\lceil20\log m\rceil), with natural logarithm.  Under (0.2),
for every fixed (r), the right side of (6.2) is (o(W/H)).  Also

\[
 \frac{Hs^2}{m}\longrightarrow0,
\tag{6.7}
\]

so (5.4) and the proved tail estimate give

\[
 J_{\rm tail}+J_{\rm act}=o(W/H).
\tag{6.8}
\]

Take the (s) cyclic rotations of one active priority list.  The rotation
beginning with (P_a) assigns every (S) avoiding (P_a) to phase (a).
Hence every nonexceptional target realizes at least (r) distinct active
omitted-pair labels across exact low-run endpoints.  In particular, taking
(r=3) gives more than two alternatives outside (o(W/H)) targets.

## 7. Omitted-pair labels are not upper-target colours

Distinct omitted-pair labels alone do not separate upper targets.

### Lemma 7.1 (label blindness)

Let (S\in\binom{[n]}{m-1}) and
(U\in\binom{[n]}{m+q}) with (S\subset U).  If two pairs
(P,P'\) lie in ([n]\setminus U), then there are literal tokens based at
(S), one omitting (P) and one omitting (P'), whose depth-(q) upper
target is the same set (U).  The middle owner may be chosen to be the
same in both tokens.

#### Proof

Choose (x\in U\setminus S), put (Y=S\cup\{x\}), and order a local row
segment as

\[
 x,\quad S\text{ in any order},\quad
 U\setminus Y\text{ in any order}.
\tag{7.1}
\]

Complete the remaining coordinates arbitrarily.  Since (P,P'\subset
[n]\setminus U), the displayed segment lies in both local universes.  It
has predecessor owner (Y) and upper target (U) in either universe.
\(\square\)

There is a second limitation on selectors based on one common priority.
For avoidance sets (E_1,\ldots,E_k\subseteq[s]), a priority order gives
distinct first phases exactly when there are distinct
(a_i\in E_i) for which all relations

\[
 a_i<x\qquad(x\in E_i\setminus\{a_i\})
\tag{7.2}
\]

form an acyclic directed graph.  Necessity is immediate; acyclicity is
sufficient by a topological ordering.

For example,

\[
 E_1=\{d,a,b\},\qquad
 E_2=\{d,b,c\},\qquad
 E_3=\{d,c,a\}
\tag{7.3}
\]

admit no rainbow priority: the earliest of (a,b,c,d) lies in at least
two of the three sets.

For \(m\ge4\) (and, when restricting to the observed window, \(H\ge3\)),
this obstruction is literal.  Choose four disjoint coordinate pairs
(P_d,P_a,P_b,P_c), and an ((m+3))-set (U_0) containing
(P_a\cup P_b\cup P_c) and avoiding (P_d).  Put

\[
 \begin{aligned}
 S_1&=U_0\setminus(P_a\cup P_b),\\
 S_2&=U_0\setminus(P_b\cup P_c),\\
 S_3&=U_0\setminus(P_c\cup P_a).
 \end{aligned}
\tag{7.4}
\]

Their avoidance sets among the four pairs are exactly (7.3).  Let
(V_d=U_0).  For (p\in\{a,b,c\}), choose a two-set
(D_p\subset[n]\setminus U_0) and put

\[
 V_p=(U_0\setminus P_p)\cup D_p.
\tag{7.5}
\]

Whenever (p\in E_i), (S_i\subset V_p), (V_p\cap P_p=\varnothing),
and (|V_p|=m+3).  Hence a literal omitted-(P_p) token at (S_i) can be
chosen with depth-three upper target (V_p).  The three middle owners are
automatically distinct for every phase choice: two of the sets in (7.4)
have symmetric difference four, whereas equality after adjoining one
coordinate to each would require symmetric difference at most two.

Thus every coherent priority leaves at least two of this literal
three-token packet in the same phase and hence at the same coded upper
target (V_p).  This is a local selector obstruction.  It is not asserted
that this three-token gadget, by itself, extends to a full low-run global
matching.

## 8. Universal fixed-owner path rigidity

The decisive limitation of the long-block construction is stronger than
the priority obstruction.

### Lemma 8.1 (induced lower-window path)

Let (r=m-1) and (L=2r+1=2m-1).  In a cyclic order on (L) coordinates,
put (S_i=I_\pi(i,r)).  Two distinct windows (S_i,S_j) are adjacent in
the Johnson graph (J(L,r)) exactly when their starts differ by (1) or
(-1) modulo (L).  Consequently every proper consecutive family

\[
 \{S_a,S_{a+1},\ldots,S_b\}
\tag{8.1}
\]

induces a path.

Any literal single-run phase using exactly the lower-target set (8.1) must
traverse that induced path forward or backward.  Away from a depth-(q)
end collar, its flags are therefore one of only the two vectors

\[
 \begin{aligned}
 L_q^\to(S_i)&=\bigcap_{h=0}^{q-1}S_{i+h},&
 U_q^\to(S_i)&=\bigcup_{h=-1}^{q}S_{i+h},\\
 L_q^\leftarrow(S_i)&=\bigcap_{h=0}^{q-1}S_{i-h},&
 U_q^\leftarrow(S_i)&=\bigcup_{h=-q}^{1}S_{i+h}.
 \end{aligned}
\tag{8.2}
\]

In particular, all omitted-pair labels collapse to at most two effective
interior phases.

#### Proof

Two cyclic intervals of length (r) in a cycle of length (2r+1) have
intersection (r-1) exactly when their cyclic start distance is one.
This proves the induced-path assertion.  Consecutive lower targets in a
literal tight run are Johnson-adjacent.  A traversal using every vertex of
an induced path once is one of its two orientations.  The intersection and
union identities in (8.2) then follow directly from consecutive windows.
\(\square\)

At \(q=1\), even the two orientations coincide at internal vertices,
away from the depth-one end collar:

\[
 L_1(S_i)=S_i,
 \qquad
 U_1(S_i)=S_{i-1}\cup S_i\cup S_{i+1}.
\tag{8.3}
\]

### Theorem 8.2 (all-depth seam charge)

Consider any aligned multiway atlas obtained by partitioning common
central owner paths into phase blocks, where every phase agrees with the
base on the **ordered consecutive owner list** inside its block and may
change only the literal continuation beyond the block.  Let \(b\) be the
number of directed right block seams.  For every \(1\le q\le m-1\), the
set \(M_q\) of upper occurrences which can differ
from the base corner satisfies

\[
 \boxed{|M_q|\le qb.}
\tag{8.4}
\]

#### Proof

By (1.5), an upper occurrence is fixed whenever its (q+1) consecutive
owner witness lies wholly inside one common block.  A directed seam between
two consecutive owners is crossed by at most \(q\) relevant forward owner
spans, starting in the \(q\) positions immediately before it.  Taking the union
over seams proves (8.4).  Multiple seam crossings only overcount.  \(\square\)

For the \(\operatorname{Sym}(C)\) atlas, (b\le K), and (8.4) is exactly
the collar bound (3.4).  The number of phase labels does not enter (8.4).

## 9. Persistence of every bounded-multiplicity collision sector

Fix a depth (q).  Let \(\mu_q(U)\) be the base upper-target load, and for
a fixed integer (K_0\ge2) define

\[
 D_{q,\le K_0}
 =\sum_{\substack{U\\2\le\mu_q(U)\le K_0}}
     \binom{\mu_q(U)}2,
\qquad
 C_{q,\le K_0}
 =\sum_{\substack{U\\2\le\mu_q(U)\le K_0}}
     (\mu_q(U)-1).
\tag{9.1}
\]

The first quantity counts unordered old collision pairs; the second is the
minimum number of occurrences which must leave their old targets in order
to split every old packet completely.

### Theorem 9.1 (collision survival under a multiway aligned atlas)

Every corner of the atlas in Theorem 8.2 has at least

\[
 \boxed{
 D_q^{\rm new}
 \ge
 \left[D_{q,\le K_0}-(K_0-1)qb\right]_+
 }
\tag{9.2}
\]

unordered upper collision pairs.  Complete splitting of all old packets
counted in (9.1) requires

\[
 \boxed{C_{q,\le K_0}\le qb.}
\tag{9.3}
\]

#### Proof

Every old collision pair whose two occurrences lie outside (M_q) remains
at its old common target.  A moved occurrence from a load class at most
(K_0) belongs to at most (K_0-1) old pairs.  Equation (8.4) therefore
gives (9.2).  In a load-(k) old packet, at least (k-1) occurrences must
move before all (k) are separated, proving (9.3).  \(\square\)

For fixed (K_0),

\[
 C_{q,\le K_0}\ge\frac{2}{K_0}D_{q,\le K_0}.
\tag{9.4}
\]

If (b=o(W/H)), then (qb=o(W)) uniformly for (q\le H).  Therefore
every \(\Omega(W)\) bounded-multiplicity collision sector leaves
\(\Omega(W)\) collision pairs in every corner.  This proves the requested
all-sector limitation, rather than a statement about only one activated
pair sector.

## 10. The first-upper owner-recycling theorem

The preceding theorem assumes an aligned common owner path.  At (q=1)
one can state exactly what a non-aligned escape must do.

Let (P) be an arbitrary literal tight path cover of the lower targets.
Let (E(P)) be the set of lower targets lying at path endpoints.  Then

\[
 |E(P)|\le2J(P).
\tag{10.1}
\]

For an internal lower target (S), let (N_P(S)) be its unordered pair of
lower neighbours.  For two covers (P_0,P), define

\[
 R(P_0,P)
 =\{S\notin E(P_0)\cup E(P):N_{P_0}(S)\ne N_P(S)\}.
\tag{10.2}
\]

### Theorem 10.1 (exact (q=1) no-recycling bound)

Let (a) be the number of lower-target occurrences whose first-upper
target differs between (P_0) and (P).  Then

\[
 \boxed{
 a\le2J(P_0)+2J(P)+|R(P_0,P)|.
 }
\tag{10.3}
\]

If the base first-upper loads are \(\mu_0(U)\), put

\[
 D_{\le K_0}
 =\sum_{\substack{U\\2\le\mu_0(U)\le K_0}}
     \binom{\mu_0(U)}2.
\tag{10.4}
\]

Then every new cover satisfies

\[
 \boxed{
 D_1(P)\ge
 \left[
 D_{\le K_0}
 -(K_0-1)\bigl(2J(P_0)+2J(P)+|R(P_0,P)|\bigr)
 \right]_+.
 }
\tag{10.5}
\]

Complete splitting of all old packets also requires

\[
 \boxed{
 |R(P_0,P)|
 \ge
 C_{\le K_0}-2J(P_0)-2J(P),
 }
\tag{10.6}
\]

where

\[
 C_{\le K_0}
 =\sum_{2\le\mu_0(U)\le K_0}(\mu_0(U)-1)
 \ge\frac{2}{K_0}D_{\le K_0}.
\tag{10.7}
\]

#### Proof

For a lower target internal in (P), (8.3) says that its first-upper target
is the union of it and its two unordered lower neighbours.  Therefore an
occurrence can change only at an endpoint of one of the covers or at a
target in (R(P_0,P)).  Equations (10.1)--(10.2) give (10.3).  The old-pair
charging argument from Theorem 9.1 gives (10.5).  Finally, complete
splitting requires at least (C_{\le K_0}) moved occurrences, which with
(10.3) gives (10.6).  Formula (10.7) follows termwise from

\[
 k-1\ge\frac2{K_0}\binom{k}{2}
 \qquad(2\le k\le K_0).
\]

\(\square\)

The first-upper target layer has size

\[
 \binom{n}{m+1}=W,
\tag{10.8}
\]

whereas the token core has (T<W) occurrences.  Its exact integer-floor
baseline is therefore

\[
 c_1^+=\left\lfloor\frac{T}{W}\right\rfloor=0.
\tag{10.9}
\]

Thus its unhalved floor energy is exactly

\[
 Q_1^+(P)
 =\sum_U\mu_P(U)(\mu_P(U)-1)=2D_1(P).
\tag{10.10}
\]

Combining (10.5) and (10.10) retains the integer floor without relaxation.
In particular, if (K_0) is fixed,
(D_{\le K_0}=\Omega(W)), and
(J(P_0),J(P)=o(W/H)), then every collision-free (P) must satisfy

\[
 |R(P_0,P)|=\Omega(W).
\tag{10.11}
\]

For an aligned fixed-block atlas, (R=0).  If the two orientations use the
same (K)-block partition, their common endpoint set has size at most
(2K), and hence

\[
 D_1(P)\ge D_{\le K_0}-2(K_0-1)K.
\tag{10.12}
\]

For the specific \(\operatorname{Sym}(C)\) atlas only the terminal
first-upper occurrence of a block varies, sharpening this to

\[
 D_1(P)\ge D_{\le K_0}-(K_0-1)K.
\tag{10.13}
\]

## 11. Exact matching is not the algebraic obstruction

The necessity of owner-path recycling should not be confused with a Hall
failure.

### Lemma 11.1 (arbitrary omitted labels admit an exact middle matching)

Assign to every lower target (S\in\binom{[n]}{m-1}) an arbitrary pair

\[
 P(S)\in\binom{[n]\setminus S}{2}.
\tag{11.1}
\]

Join (S) to (Y=S\cup\{x\}) whenever

\[
 x\in[n]\setminus(S\cup P(S)).
\tag{11.2}
\]

This bipartite graph has a matching saturating every lower target.

#### Proof

Every lower vertex has exactly (m) allowed middle neighbours.  Every
middle (m)-set (Y) has at most its (m) lower facets as neighbours.
For any family (\mathcal A) of lower targets, edge counting gives

\[
 m|\mathcal A|
 \le m|N(\mathcal A)|.
\tag{11.3}
\]

Thus Hall's condition holds.  \(\square\)

Every matched edge in Lemma 11.1 embeds in a literal omitted-(P(S)) row
segment.  Hence arbitrary pair-label assignment and exact middle
integrality are compatible token by token.  What the lemma does not give is
a clustered physical chronology.

There is an even sharper (q=1) statement.

### Lemma 11.2 (collision-free first upper layer exists tokenwise)

Let (S\mapsto Y(S)) be any exact lower-saturating, middle-simple central
matching.  There is an injection

\[
 Y(S)\longmapsto U(S)\in\binom{[n]}{m+1},
 \qquad Y(S)\subset U(S).
\tag{11.4}
\]

For every \(S\), every pair

\[
 P\in\binom{[n]\setminus U(S)}2
\tag{11.5}
\]

gives a literal token with the same (S,Y(S),U(S)).  Thus each token has

\[
 \binom m2>2\qquad(m\ge3)
\tag{11.6}
\]

omitted-pair alternatives, the central matching stays exact, and all
first-upper targets are distinct.

#### Proof

The inclusion graph between the middle and ((m+1))-layers is
((m+1))-regular on two vertex classes of equal size (W).  Regular
bipartite Hall gives a perfect matching of those two full layers.  Restrict
it to the distinct middle owners (Y(S)), obtaining (11.4).

The complement of (U(S)) has size (m).  Choose any pair (P) in that
complement, write

\[
 Y(S)=S\cup\{x\},\qquad U(S)=Y(S)\cup\{d\},
\]

and begin a local cyclic order with the segment

\[
 x,\quad S\text{ in any order},\quad d.
\tag{11.7}
\]

Completing the unused coordinates gives a literal omitted-\(P\) token with
the desired lower, middle, and first-upper targets.  \(\square\)

Rendering the tokens in Lemma 11.2 separately uses \(T=\Theta(W)\) runs.
The lemma therefore proves that neither Hall nor literal token existence is
the remaining obstruction.  The missing operation is to cluster such
choices into \(o(W/H)\) tight paths while changing a positive density of
owner adjacencies as required by (10.11).

## 12. Clean final lemma and precise boundary

The proved synthesis can be stated as follows.

### Theorem 12.1 (multiway atlas / collision-recycling dichotomy)

Assume (0.2).  There is a literal integral pair-omission atlas
\(\mathcal A_H\) with the following properties.

1. Every corner saturates all \(T\) lower targets and has one common exact
   middle matching.
2. Every lower target has at least \(\binom{H+2}{2}\) omitted-pair phases.
3. If \(K\) is the block count in (2.2), every corner has

   \[
      J\le K\le J_0+\frac{T}{m-H}=o(W/H)
   \]

   physical runs and literal word length \(W+o(W)\).
4. For every depth \(q\le H\), at most \(qK\) upper occurrences can differ
   from the base corner.
5. Consequently, for every fixed \(K_0\), an
   \(\Omega(W)\) depth-\(q\) collision census supported on loads at most
   \(K_0\) survives with \(\Omega(W)\) collision pairs in every corner.

Moreover, any low-run literal tight cover which completely removes a
linear bounded-multiplicity first-upper census must change the unordered
lower-neighbour relation at \(\Omega(W)\) internal targets.

#### Proof

Items 1--3 are Theorem 2.1 and Section 4.  Item 4 is Theorem 8.2 with one
directed seam per block.  Item 5 is Theorem 9.1.  The final assertion is
Theorem 10.1.  \(\square\)

The theorem genuinely builds the requested more-than-binary, exact-middle,
low-boundary atlas.  It also proves that this atlas cannot accomplish the
requested universal collision splitting.  The only constructive escape
left by the proof is a global, positive-density owner-path rewiring with
low physical run count.  Lemma 11.2 shows that a collision-free exact
first-upper target assignment exists before chronology is imposed; Theorem
10.1 quantifies exactly how much chronology must change to realize one.

No constant-one conclusion is claimed.  No signed relaxation, fractional
factor, web search, or finite/computational search is used.
