# Audit of the fixed-annulus mesoscopic two-packet switch

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

This note independently audits
`MATH_THEOREM_FIXED_ANNULUS_MESOSCOPIC_TWO_PACKET_SWITCH_20260726.md`.
All notation below is local to that report:

\[
n=2m,\qquad k=m-q_0,\qquad
2\le t<q_0,\qquad u=k-t+1.
\]

The conclusion is that Theorems 3.1 and 4.1, Corollary 5.3, the capacity
constants in Section 6, and the protected-support codegree exponent in
Theorem 7.2 are correct.  Two compressed bookkeeping points have been
expanded in the source report: the index reversal in Theorem 3.1 and the
factor-two cancellation after contracting middle complements.  No
substantive correction to the construction is needed.

The audit does **not** turn the orbit average into an integral selection.
The protected-deck matching and signed reserve orientation in Section 8
remain unproved.

## 1. Exact cancellation table

Write

\[
U=(e_1,\ldots,e_t),\qquad
V=(e_2,\ldots,e_t,e_1),
\]

let \(Z=JP=(z_1,\ldots,z_N)\), and let

\[
Q=(z_2,\ldots,z_u,z_1,z_{u+1},\ldots,z_N).
\]

For \(1\le j<t\), the contribution to

\[
\mathbf I_r(VP)-\mathbf I_r(UP)
\]

is

\[
\begin{split}
 &[V_{\le j}\cup P^-_{r-j}]-[U_{\le j}\cup P^-_{r-j}]\\
 &\quad+[V_{>j}\cup P^+_{r-t+j}]
          -[U_{>j}\cup P^+_{r-t+j}].
\end{split}
\tag{1.1}
\]

In the second difference

\[
\mathbf I_r(JUQ)-\mathbf I_r(JVQ),
\]

take index \(t-j\), not index \(j\).  Reversal of the block gives

\[
\begin{split}
 &[U_{>j}\cup Q^-_{r-t+j}]-[V_{>j}\cup Q^-_{r-t+j}]\\
 &\quad+[U_{\le j}\cup Q^+_{r-j}]
          -[V_{\le j}\cup Q^+_{r-j}].
\end{split}
\tag{1.2}
\]

Thus the post-block pair cancels when

\[
Q^-_{r-t+j}=P^+_{r-t+j},
\tag{1.3}
\]

and the pre-block pair cancels when

\[
Q^+_{r-j}=P^-_{r-j}.
\tag{1.4}
\]

Now \(Q^-_d=P^+_d\) for \(d\le m-1\), while
\(Q^+_d=P^-_d\) exactly for \(d\ge u\).  If \(r=k\), both context
sizes in (1.3)--(1.4) lie in

\[
[k-t+1,k-1]=[u,k-1].
\]

If \(r=m\), they lie in \([m-t+1,m-1]\), which is contained in
\([u,m-1]\) because \(m-t+1-u=q_0\).  This proves both protected-deck
identities with the word alignment and reversal fully accounted for.
Complementing every interval proves the upper protected identity.

## 2. The triangular direction and literal distinctness

Put \(r_s=k-s\), where \(s\ge1\) and \(s\le H-q_0\).  Relation
(1.3) still holds at every relevant context size.  Relation (1.4) fails
exactly when

\[
r_s-j<u
\quad\Longleftrightarrow\quad
j\ge t-s.
\tag{2.1}
\]

Consequently the uncancelled vector is exactly

\[
\sum_{j\ge t-s}
\left(
[V_j\cup P^-_{r_s-j}]-[U_j\cup P^-_{r_s-j}]
+[U_j\cup Q^+_{r_s-j}]-[V_j\cup Q^+_{r_s-j}]
\right),
\tag{2.2}
\]

where \(1\le j<t\).  The index set has size
\(\min\{s,t-1\}\).

There is no hidden cancellation in (2.2).  For an included \(j\), put
\(d=r_s-j\).  Then \(1\le d<u\), and

\[
P^-_d=\{z_1,\ldots,z_d\},\qquad
Q^+_d=\{z_2,\ldots,z_{d+1}\};
\tag{2.3}
\]

these exterior sets differ.  Also \(U_j\ne V_j\).  Since the block and
exterior alphabets are disjoint, the two independent distinctions in
(2.3) and in the block section make all four targets for a fixed \(j\)
distinct.  Targets belonging to two different indices have different
intersection cardinalities with the block alphabet, so they too are
distinct.  Hence

\[
\|d_s^-\|_1=4\min\{s,t-1\}.
\tag{2.4}
\]

Complementation is a bijection and preserves coefficients, so the upper
direction has the same norm.  This verifies Theorem 4.1 exactly.

## 3. Within-component protected collision

Reverse \(UP\) and cyclically rotate.  Its interval deck becomes that of

\[
JUZ.
\]

The word \(JUQ\) is obtained by moving \(z_1\) across

\[
d=u-1=k-t
\]

successive exterior symbols.  For \(r=k\) or \(r=m\), one has

\[
d<\min\{r,n-r\}.
\]

The exact one-symbol relocation count therefore gives

\[
|\mathcal I_r(UP)\cap\mathcal I_r(JUQ)|
=n-2d=2q_0+2t.
\tag{3.1}
\]

Next, \(JV\) is obtained from \(JU\) by moving \(e_1\) across
\(t-1\) symbols.  Such a move introduces exactly \(2(t-1)\) new
rank-\(r\) interval targets.  Intersecting with a fixed deck can therefore
increase by at most that number.  It follows that

\[
|\mathcal I_r(UP)\cap\mathcal I_r(JVQ)|
\le 2q_0+4t-2.
\tag{3.2}
\]

Starting from the reversal \(JVZ\) of \(VP\) gives the identical bound
for the other shore.  Thus Corollary 5.3 is correct.  In particular, for
\(K/2+O(1)\) components and \(q_0,t=O(\sqrt m)\), the sum of these
internal overlaps at either protected rank is

\[
O(K(q_0+t))=O(W/\sqrt m)=o(W).
\tag{3.3}
\]

This is only the within-component contribution; the report correctly
leaves cross-component collision to the protected-deck matching gate.

## 4. Exact capacity constants

Let \(L=H-q_0\) and

\[
S(L,t)=\sum_{s=1}^{L}\min\{s,t-1\}.
\]

At a fixed lower depth, (2.2) has
\(2\min\{s,t-1\}\) positive cells and the same number of negative
cells.  Switching shores can therefore change the number of holes by at
most \(2\min\{s,t-1\}\): it can fill no more positive cells and create
no more negative cells.  Including the upper depth gives the exact
state-independent upper bound

\[
4S(L,t)
\tag{4.1}
\]

per component.  Since at most \(K/2+O(1)\) components are present, the
aggregate hole count can change by at most

\[
2KS(L,t)+O(m).
\tag{4.2}
\]

The total two-sign \(\ell^1\) variation, which is twice (4.1), is

\[
8S(L,t)
\tag{4.3}
\]

per component.  Thus the report consistently distinguishes raw
incidence capacity from possible hole descent.

If \(t=c\sqrt m+O(1)\), put \(\lambda=b-a\).  Then

\[
{S(L,t)\over m}\longrightarrow
\sigma(\lambda,c):=
\begin{cases}
\lambda^2/2,&\lambda<c,\\
c\lambda-c^2/2,&\lambda\ge c.
\end{cases}
\tag{4.4}
\]

Since \(K=(e^{-a^2}+o(1))W/(2m)\), the total possible aggregate hole
change in (4.2) is at most

\[
(e^{-a^2}\sigma(\lambda,c)+o(1))W.
\tag{4.5}
\]

The total raw \(\ell^1\) variation is twice this asymptotic quantity.
For \(t=2\), (4.2) is

\[
2KL=O(W/\sqrt m)=o(W).
\tag{4.6}
\]

At one fixed offset \(s\), all components together change the two-sign
hole count by at most

\[
2K\min\{s,t-1\}+O(\sqrt m)=O(W/\sqrt m)=o(W).
\tag{4.7}
\]

These calculations verify the constants in Section 6 and the important
rankwise limitation: the switch bank can repair an \(O(W)\) aggregate
residual but cannot repair a linear residual on any one depth.

## 5. Protected-support codegrees

Let \(\mathcal R_r\) be the distinct common two-packet support at rank
\(r\in\{k,m\}\), with \(\rho_r=|\mathcal R_r|\).  Equation (3.2)
gives

\[
2n-(2q_0+4t-2)\le \rho_r\le2n.
\tag{5.1}
\]

In the labelled \(S_n\)-orbit, the degree of a rank-\(r\) target is

\[
D_r={n!\rho_r\over\binom nr}.
\tag{5.2}
\]

If \(A_{r,j}\) counts ordered template pairs at Johnson distance \(j\),
orbit--stabilizer gives

\[
{\lambda_{r,j}\over D_r}
= {A_{r,j}\over
\rho_r\binom rj\binom{n-r}{j}}.
\tag{5.3}
\]

It remains to verify the numerator at \(j=1\).  A single rank-\(r\)
cycle deck has exactly \(2n\) ordered distance-one pairs.  Thus the two
within-packet contributions total \(4n\).  If two cycles differ by
relocating one symbol, delete that symbol.  Cross pairs containing it in
neither or both target sets project injectively to distance-one pairs of
one common cycle, contributing fewer than \(4n\).  In either mixed
membership direction, there are at most \(r\) choices for the interval
containing the moved symbol and at most two interval extensions of the
remaining \((r-1)\)-set.  Both mixed directions contribute at most
\(4r\).  Hence a relocation creates fewer than \(8n\) ordered cross
pairs.

Apply this first to the long exterior relocation.  The subsequent block
relocation introduces at most \(2(t-1)\) new targets.  For each new target
there are at most \(2r\) distance-one partners in a fixed cycle deck:
choose the deleted target element, and note that a fixed \((r-1)\)-set
is contained in at most two cyclic \(r\)-intervals.  Doubling the cross
direction and adding the within-packet term yields

\[
A_{r,1}\le20n+8(t-1)r.
\tag{5.4}
\]

Equations (5.1), (5.3), and \(r(n-r)=\Theta(m^2)\) imply

\[
{\lambda_{r,1}\over D_r}
=O((t+1)/m^2).
\tag{5.5}
\]

For \(r=k\) and \(j\ge2\), use
\(A_{r,j}\le\rho_r^2=O(m^2)\).  The product
\(\binom rj\binom{n-r}j\) is at least its smaller endpoint value on
\(2\le j\le r\).  Its \(j=2\) value is \(\Theta(m^4)\), while its
\(j=r\) value is

\[
\binom{m+q_0}{2q_0}
=\exp(\Theta(\sqrt m\log m)),
\]

so (for all sufficiently large \(m\))

\[
{\lambda_{r,j}\over D_r}=O(m^{-3}).
\tag{5.6}
\]

At rank \(m\), contract every complement pair.  For \(j<m/2\), an
ordered atom pair lifts to exactly two ordered set-pairs at distance
\(j\), while both the edge size and ambient vertex count are halved; the
ratio (5.3) is unchanged.  At \(j=m/2\), an atom pair has four set-pair
lifts and the atom neighbor count is halved, again leaving (5.3)
unchanged.  The \(j=m-1\) set stratum is the \(j=1\) atom stratum, and
the complement pair itself is one atom rather than a nontrivial
codegree.  On the remaining strata
\(2\le\min\{j,m-j\}\), the symmetric product
\(\binom mj^2\) is at least \(\binom m2^2=\Theta(m^4)\), so the same
crude argument proves (5.6).  This proves

\[
\max_{S\ne T,\ T\ne S^c}{\operatorname{codeg}(S,T)\over D_r}
=O((t+1)/m^2).
\tag{5.7}
\]

For \(t=O(\sqrt m)\), this is \(O(m^{-3/2})\).  The mixed
tight--middle estimate also checks: for a fixed tight \(k\)-set, every
intersection stratum of middle sets has size at least

\[
\binom{m+q_0}{q_0},
\]

whereas a component contains only \(O(m^2)\) ordered mixed pairs.
Normalizing by a vertex degree therefore gives at most

\[
{O(m)\over\binom{m+q_0}{q_0}}
=\exp(-\Theta(\sqrt m\log m)).
\tag{5.8}
\]

Thus the protected-support codegree claims, including the exponent, are
valid.

## 6. Exact proved boundary

The audited construction supplies all of the following:

1. an exact two-packet switch preserving the complete middle and
   depth-\(q_0\) load vectors;
2. a nonzero literal triangular direction at every deeper annular depth;
3. only \(o(W)\) forced within-component protected collision;
4. \(\Theta(W)\) aggregate raw capacity at mesoscopic width, but only
   \(o(W)\) capacity on each individual depth; and
5. an orbit protected-support relative codegree
   \(O(m^{-3/2})\), with exponentially smaller mixed codegrees.

What is not supplied is a theorem converting these favorable time-zero
codegrees into a protected-deck matching through a growing-uniformity
residual, nor a common sign choice satisfying all literal reserve
inequalities.  Those two assertions are exactly the residual boundary;
no coefficient-one conclusion follows from this audit alone.
