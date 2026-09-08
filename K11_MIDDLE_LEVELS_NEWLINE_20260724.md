# A subset-flow hierarchy and an exact central-label law at \(k=11\)

## 1. Outcome

This note starts from the audited zero-margin consequence in
`K11_ZERO_MARGIN_WINDOW_ATTACK_20260724.md`: the complete rank-five and
rank-six layers are paired by inclusion.  The at most six final matching
edges are omitted only from the projected Johnson forest; after restoring
them, the same data form a spanning alternating path cover of the
middle-level graph.

No contradiction is obtained.  Two genuinely stronger necessary
invariants are proved.

First, the \(42\)-per-coordinate extension law is only the first member of
an exact hierarchy.  For every coordinate set \(X\subseteq[11]\), the
number of inclusion-matching edges which complete \(X\) is forced.  If
\(|X|=t\), that number is

\[
 \Delta_t=\binom{11-t}{6-t}-\binom{11-t}{5-t}.
\]

For \(1\le t\le6\), the values are

\[
\boxed{(\Delta_1,\ldots,\Delta_6)=(42,42,28,14,5,1).}
\tag{1.1}
\]

Resolving these matching completions along the alternating paths gives
exact entry, exit, bypass, root, and omitted-colour equations for every
coordinate star.  At (t=4), this determines the multiplicity of every
rank-four intersection colour from its endpoint and cut data.  At (t=5),
it gives a sharp omitted-colour endpoint cut.

Second, the central/external split of the (42) extension labels is not
free.  Let (R_x^{(3)}) be the number of zero runs of coordinate (x) of
length at least three in the incidence word of the low-entry segment
\(A_0,\ldots,A_{m-1}\).  If \(H=C_s\) is the exceptional triple, then the
number \(e_x^{\rm cen}\) of central rank-five/rank-six matching edges which
add (x) is exactly

\[
\boxed{
 e_x^{\rm cen}=R_x^{(3)}-1+\mathbf1_{x\in H}.
}
\tag{1.2}
\]

Consequently the external share is fixed as well:

\[
\boxed{
 e_x^{\rm ext}=43-R_x^{(3)}-\mathbf1_{x\in H}.
}
\tag{1.3}
\]

This proves in particular

\[
 R_x^{(3)}\le
 \begin{cases}
 42,&x\in H,\\
 43,&x\notin H.
 \end{cases}
\tag{1.4}
\]

For an internal seam, the two central roots and their two omitted six-set
colours also have an exact normal form.  It identifies the seam-local
length-three zero-run coordinates with the coordinates outside (H) in
the intersection of the two roots.

All arguments are finite and deterministic.  No search, solver, or
enumeration is used.

## 2. The oriented alternating path cover

Write

\[
 \mathcal V_5=\binom{[11]}5,
 \qquad
 \mathcal V_6=\binom{[11]}6.
\]

Fix the perfect inclusion matching supplied by the endpoint saturation:

\[
 \mathcal M:\mathcal V_5\longrightarrow\mathcal V_6,
 \qquad S\subset \mathcal M(S).
\tag{2.1}
\]

The alternating path cover has \(c\le6\) components.  Orient every
component from its initial five-set toward its final six-set, and write it
as

\[
 P_0,U_0,P_1,U_1,\ldots,P_\ell,U_\ell,
\tag{2.2}
\]

where

\[
 U_j=\mathcal M(P_j),
 \qquad
 P_{j+1}\subset U_j\quad(0\le j<\ell).
\tag{2.3}
\]

The associated Johnson-forest edge is \(P_jP_{j+1}\), with upper colour
\(U_j\).  The final matching edge \(P_\ell U_\ell\) is unused by the
Johnson forest.  Thus the \(c\) final five-sets are its roots and the \(c\)
final six-sets are precisely the omitted upper colours.

For a coordinate set \(X\subseteq[11]\), define:

* \(\tau_X\): the number of initial five-set endpoints containing \(X\);
* \(\sigma_X\): the number of root five-sets containing \(X\);
* \(\mu_X\): the number of omitted six-set colours containing \(X\);
* \(d_X\): the number of final matching edges \(P_\ell U_\ell\) for which
  \(X\subseteq U_\ell\) but \(X\nsubseteq P_\ell\);
* \(a_X\): the number of forest transitions entering the star of \(X\),
  meaning \(X\nsubseteq P_j\) and \(X\subseteq P_{j+1}\);
* \(b_X\): the number leaving that star;
* \(z_X\): the number of bypass transitions for which
  \(X\subseteq U_j\), but neither adjacent five-set contains \(X\); and
* \(h_X\): the number of forest transitions for which both adjacent
  five-sets contain \(X\).

The quantities are nonnegative integers.  The letters \(a,b,z,h\) refer
only to the oriented middle-level path cover, not to physical word
positions.

## 3. The full matching-extension hierarchy

### Theorem 1

Let \(X\subseteq[11]\) have size \(t\le6\).  Put

\[
 v_t=\binom{11-t}{5-t},
 \qquad
 u_t=\binom{11-t}{6-t},
 \qquad
 \Delta_t=u_t-v_t,
\tag{3.1}
\]

with an out-of-range binomial interpreted as zero.  Then

\[
\boxed{\mu_X=\sigma_X+d_X,}
\tag{3.2}
\]

\[
\boxed{a_X+z_X+d_X=\Delta_t,}
\tag{3.3}
\]

\[
\boxed{b_X+z_X=\Delta_t-\mu_X+\tau_X.}
\tag{3.4}
\]

For \(t\le5\), one also has

\[
\boxed{h_X+a_X=v_t-\tau_X,}
\tag{3.5}
\]

\[
\boxed{h_X+b_X=v_t-\sigma_X.}
\tag{3.6}
\]

In particular,

\[
 a_X-b_X=\sigma_X-\tau_X.
\tag{3.7}
\]

### Proof

Sum over the perfect matching (2.1) the difference

\[
 \mathbf1_{X\subseteq U}-\mathbf1_{X\subseteq P}.
\]

Since \(P\subset U\), every summand is zero or one.  The total is also the
difference between the numbers of complete-layer six-sets and five-sets
containing (X), namely \(u_t-v_t=\Delta_t\).  Therefore exactly
\(\Delta_t\) matching edges complete (X).

On a used matching edge (P_jU_j), a completion of (X) has two possible
forms.  If (P_{j+1}) contains (X), the subsequent forest transition
enters the (X)-star.  If (P_{j+1}) does not contain (X), the transition
bypasses the star.  The unused final matching edges contribute (d_X).
This proves (3.3).

On a final matching edge, \(U_\ell\) contains (X) either because the root
\(P_\ell\) already contains (X), or because that matching edge completes
(X).  The two alternatives are disjoint, proving (3.2).

Telescoping the indicator \(\mathbf1_{X\subseteq P_j}\) along every path
gives (3.7).  Subtract (3.7) from (3.3), and use (3.2), to obtain (3.4).

Finally, every noninitial five-set containing (X) has exactly one incoming
forest edge, which is internal to or enters the (X)-star.  This proves
(3.5).  Every nonroot five-set containing (X) has exactly one outgoing
forest edge, proving (3.6).  ∎

### 3.1 Numerical values

The hierarchy (3.3) has the exact right sides

\[
\begin{array}{c|rrrrrr}
t&1&2&3&4&5&6\\ \hline
\Delta_t&42&42&28&14&5&1.
\end{array}
\tag{3.8}
\]

For (t=1), bypass is impossible.  Equation (3.3) is exactly

\[
 f_x+d_x=42,
\]

the extension law (3.20) in the source note; (3.4) is its deletion-label
counterpart (3.24).

For a pair \(X=\{x,y\}\), (z_X) is exactly the number of forest
transitions which swap (x) and (y).  Thus the new second-order law is

\[
\boxed{a_{xy}+z_{xy}+d_{xy}=42.}
\tag{3.9}
\]

It retains information which is invisible in the eleven separate
coordinate equations.

### 3.2 Rank-four intersection colours

Let (|X|=4).  Two adjacent five-sets both contain (X) exactly when their
intersection is (X).  Hence (h_X) is the multiplicity of (X) as a
lower intersection colour of the Johnson forest.  Equations (3.3)--(3.6)
specialize to

\[
\boxed{
 h_X+a_X=7-\tau_X,
 \qquad
 h_X+b_X=7-\sigma_X,
}
\tag{3.10}
\]

and

\[
\boxed{
 z_X-h_X=7+\tau_X+\sigma_X-\mu_X.
}
\tag{3.11}
\]

Because the forest induced on the seven five-sets containing (X) is
acyclic,

\[
 0\le h_X\le6.
\tag{3.12}
\]

Thus every one of the 330 rank-four colours has an exact endpoint/cut
ledger, rather than only a global multiplicity sum.

### 3.3 The sharp five-set endpoint cut

Let (|X|=5).  Its star in the five-set layer is the single vertex (X),
so (h_X=0),

\[
 a_X=1-\tau_X,
 \qquad
 b_X=1-\sigma_X.
\]

Equation (3.3) gives

\[
\boxed{
 z_X+d_X=4+\tau_X,
 \qquad
 z_X=4+\tau_X+\sigma_X-\mu_X.
}
\tag{3.13}
\]

In particular,

\[
\boxed{\mu_X\le4+\tau_X+\sigma_X.}
\tag{3.14}
\]

If five or more omitted six-set colours contain one five-set (X), then
(X) must be an endpoint of the path cover.  If all six supersets of (X)
are omitted, then (X) must be both an initial endpoint and a root.

## 4. The central extension vector is a long-zero-run vector

Return to the low-entry segment

\[
 A_0,A_1,\ldots,A_{m-1}
\]

and its triple windows

\[
 C_i=A_i\cup A_{i+1}\cup A_{i+2},
 \qquad0\le i\le m-3.
\tag{4.1}
\]

The unique exceptional triple is \(H=C_s\); every \(C_i\) with \(i\ne s\)
is a five-set.  The endpoint matching of the source note pairs

\[
 C_i\longmapsto T_i=C_i\cup C_{i+1}\quad(i<s)
\tag{4.2}
\]

and

\[
 C_i\longmapsto T_{i-1}=C_{i-1}\cup C_i\quad(i>s).
\tag{4.3}
\]

These are all \(m-3\) central matching edges.

For a coordinate \(x\), let \(R_x^{(3)}\) be the number of zero runs of
\(x\) of length at least three in the binary incidence word of
\(A_0,\ldots,A_{m-1}\).

### Theorem 2

For every coordinate \(x\), the number of central matching edges adding
\(x\) is

\[
\boxed{
 e_x^{\rm cen}=R_x^{(3)}-1+\mathbf1_{x\in H}.
}
\tag{4.4}
\]

This holds whether the seam is internal or at either boundary.

### Proof

Put

\[
 \gamma_i=\mathbf1_{x\in C_i}
 \qquad(0\le i\le m-3).
\]

For (i<s), the matching edge (4.2) adds (x) exactly when

\[
 (\gamma_i,\gamma_{i+1})=(0,1).
\]

For (i>s), the matching edge (4.3) adds (x) exactly when

\[
 (\gamma_{i-1},\gamma_i)=(1,0).
\]

Consider one zero run of the binary word \(\gamma\).  If it lies strictly
to the left of the pivot (s), its right boundary contributes one counted
\(0\)-to-\(1\) transition.  If it lies strictly to the right, its left
boundary contributes one counted \(1\)-to-\(0\) transition.  If
\(\gamma_s=0\), the unique zero run containing (s) contributes neither.
Therefore

\[
 e_x^{\rm cen}
 =Z_0(\gamma)-\mathbf1_{\gamma_s=0},
\tag{4.5}
\]

where \(Z_0(\gamma)\) is the number of zero runs in \(\gamma\).  The same
argument at (s=0) or (s=m-3) says that the initial or terminal zero run
is the only possible uncounted run.

A zero run of length ℓ in the incidence word of the (A_i)'s produces a
zero run of length ℓ−2 in the triple-window word \(\gamma\) precisely
when ℓ≥3.  This is a bijection between the zero runs counted by
(R_x^{(3)}) and the zero runs of \(\gamma\).  Hence

\[
 Z_0(\gamma)=R_x^{(3)}.
\]

Finally, \(\gamma_s=1\) exactly when \(x\in H\).  Substitution in (4.5)
proves (4.4).  ∎

### 4.1 Exact external share

The full inclusion matching adds every coordinate exactly 42 times.  Hence
Theorem 2 immediately gives

\[
\boxed{
 e_x^{\rm ext}=42-e_x^{\rm cen}
 =43-R_x^{(3)}-\mathbf1_{x\in H}.
}
\tag{4.6}
\]

Since the external count is nonnegative, (1.4) follows.

Summing (4.4) is an exact audit.  The source note proves

\[
 \sum_xR_x^{(3)}=R^{(3)}=m+8-\rho,
 \qquad \rho=|H|.
\]

Therefore

\[
 \sum_xe_x^{\rm cen}
 =(m+8-\rho)-11+\rho
 =m-3,
\]

which is exactly the number of central matching edges.  Dually,

\[
 \sum_xe_x^{\rm ext}=465-m,
\]

the exact number of external matching edges.

### 4.2 Coupling to the rank-four budget at (n_5=133)

Let (E_{1,x}) and (E_{2,x}) be the numbers of zero runs of (x) of
length exactly one and two in the (A)-incidence word.  Then

\[
 Z_x=E_{1,x}+E_{2,x}+R_x^{(3)}.
\tag{4.7}
\]

Substitute (4.7) and the exact source identity

\[
 Z_x+\lambda_x+r_x=65+h_x+2i_x
\]

into (4.6), where \(h_x=\mathbf1_{x\in H}\) and
\(i_x=\mathbf1_{x\in B_s\cap B_{s+1}}\).  One obtains the new exact bridge

\[
\boxed{
 e_x^{\rm ext}
 =\lambda_x+r_x+E_{1,x}+E_{2,x}
  -22-2h_x-2i_x.
}
\tag{4.8}
\]

In particular,

\[
 \lambda_x+r_x+E_{1,x}+E_{2,x}
 \ge22+2h_x+2i_x.
\tag{4.9}
\]

This couples the repeat/literal rank-four incidence to the formerly free
external extension-label vector.  It is not a contradiction because the
length-one zero-run vector remains unconstrained coordinatewise.

## 5. The two internal seam roots

Assume now that (H=C_s) is internal.  Put

\[
 P=C_{s-1},\qquad Q=C_{s+1},
 \qquad U=T_{s-1},\qquad V=T_s.
\tag{5.1}
\]

The ordered state schedule has a left-oriented (02) block ending at
(P), and a right-oriented (13) block beginning at (Q).  Thus (P,Q)
are roots of two distinct forest components, and (U,V) are their omitted
matching colours.  In particular,

\[
\boxed{c\ge2.}
\tag{5.2}
\]

The window identities give

\[
 U=P\cup H,
 \qquad
 V=Q\cup H.
\tag{5.3}
\]

Since (P,Q) have rank five and (U,V) rank six, there are unique
coordinates

\[
 p\in H\setminus P,
 \qquad
 q\in H\setminus Q.
\tag{5.4}
\]

Moreover \(H\subseteq P\cup Q\), directly from the definitions of the
three consecutive triple windows.  Therefore \(p\ne q\), \(p\in Q\), and
\(q\in P\).  If the exceptional jump has excess \(\eta\), then

\[
 |U\cup V|=7+\eta.
\]

Because \(H\subseteq P\cup Q\), this is also \(|P\cup Q|\).  Hence

\[
\boxed{|P\cap Q|=3-\eta.}
\tag{5.5}
\]

Also

\[
\boxed{
 U\cap V=(P\cap Q)\cup\{p,q\},
 \qquad |U\cap V|=5-\eta.
}
\tag{5.6}
\]

Every member of \(H\setminus\{p,q\}\) belongs to both roots.  Consequently

\[
\boxed{
 |(P\cap Q)\setminus H|=5-\rho-\eta.
}
\tag{5.7}
\]

The source note identifies the seam-local length-three zero-run coordinates
as

\[
 (U\cap V)\setminus H.
\]

By (5.6), this set is exactly

\[
\boxed{(P\cap Q)\setminus H.}
\tag{5.8}
\]

Thus the internal length-three run defect is literally the part of the
two-root intersection lying outside the seam mask.

The two unused matching edges complete both the pair \(\{p,q\}\) and the
set (H).  In the notation of Theorem 1,

\[
\boxed{d_{\{p,q\}}\ge2,
 \qquad d_H\ge2.}
\tag{5.9}
\]

For (H) of rank four this spends two of the fourteen forced completions
in (3.8); for (H) of rank three it spends two of twenty-eight.

Finally, the two central unused matching edges have added labels (p,q).
Combining this with (4.4), the number of *used central forest edges* labelled
(x) is

\[
\boxed{
 f_x^{\rm cen}
 =R_x^{(3)}-1
  +\mathbf1_{x\in H\setminus\{p,q\}}.
}
\tag{5.10}
\]

Its sum is (m-5), the number of forest edges in the two central path
pieces.

## 6. Why the finite graph package still does not contradict itself

The new equations are stronger than (3.20)--(3.24), but their global sums
close exactly.

For example, sum (3.10) over all 330 four-sets.  Every forest edge has one
rank-four intersection, while each transition enters exactly four
rank-four stars.  The result is

\[
 (462-c)+4(462-c)=5(462-c),
\]

which agrees with the endpoint side because each five-set endpoint contains
five rank-four subsets.

Likewise, every forest transition bypasses exactly six rank-four stars,
and every unused matching edge completes exactly ten of them.  Summing
(3.3) at (t=4) gives

\[
 4(462-c)+6(462-c)+10c=14\cdot330.
\]

The central-label identity also closes exactly by the audit following
(4.6).  Hence none of these summed equations supplies a contradiction.
Their force is coordinatewise and subsetwise.

More conceptually, a spanning alternating path cover of the two middle
levels is not itself exceptional: cutting a middle-level Hamilton cycle
already produces such a cover, and every perfect inclusion matching obeys
the hierarchy of Theorem 1.  The zero-margin problem must therefore use the
extra physical information: the six offset blocks, the long central
two-sided-rainbow segment, the seam roots, and the lower-entry run budget.

## 7. Self-audit and exact remaining target

The proof uses only the following audited inputs:

1. the perfect rank-five/rank-six inclusion matching;
2. the spanning alternating path cover with \(c\le6\);
3. the canonical central matching rules (4.2)--(4.3);
4. the exact identity (R^{(3)}=m+8-\rho); and
5. for (4.8), the (n_5=133) coordinate identity from the source note.

No equation assumes that arbitrary rankwise balanced data can be glued, and
no selected witness is changed.  The symbols \(d_X,\mu_X,\sigma_X\) refer
to the same (c) final matching edges throughout.

Boundary seams require no modification of Theorem 2: the unique initial or
terminal zero run containing the pivot is exactly the uncounted run in
(4.5).  Section 5 is explicitly restricted to an internal seam.

The strongest new usable gate is now:

> combine the exact external extension vector (4.6), or its rank-four form
> (4.8), with the physical endpoint-offset restrictions on the external
> rank-five/rank-six matching edges.

Any upper bound on which coordinates can be added by the external
(00,01,23,33) blocks immediately becomes a lower bound on the long-run
vector (R_x^{(3)}).  Conversely, a lower bound on a coordinate's long-run
count forces a deficit in its external extension capacity.  That is a
strictly smaller problem than the previously free central/external label
split, but it is not solved here.
