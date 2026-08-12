# Composition lane: bottom-up flag conveyors and coherent PCap

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

First suppose a rooted size-\(s\) port factor is substituted strictly
inside a larger exact factor with its outer collars fixed, and write one of
its rooted geodesics as

\[
 X_t=(P\setminus\{\alpha _1,\ldots,\alpha _t\})
       \cup\{\beta _1,\ldots,\beta _t\},
 \qquad 0\le t\le s.                                  \tag{0.1}
\]

The two usual child labels are

\[
 \lambda^- =\{\alpha_s\},\qquad
 \lambda^+ =\{\beta_1\}.                              \tag{0.2}
\]

For this fixed-collar architecture, the exact ancestor calculation gives a
sharper object.  For every protected depth \(q\ge s-1\), the complete
affected profile of this row is determined by the two nested flags

\[
 D_b=P\setminus\{\alpha_1,\ldots,\alpha_b\},
 \quad 1\le b\le s-1,                                 \tag{0.3}
\]

\[
 I_a=\{\beta_1,\ldots,\beta_a\},
 \quad 1\le a\le s-1,                                 \tag{0.4}
\]

after intersection with fixed context gates and adjoining fixed exterior
carriers.  There are exactly \(2(s-1)\) potentially changed windows per
changed row, independently of how far above the packet the ancestor lies.
The endpoint labels in (0.2) account for only two of these windows.

This has four consequences.

1. A child-label move does have one marked descendant at every ancestor,
   but it is accompanied by \(2s-4\) flag-prefix collar terms.  The label
   alone does not determine the ancestor profile.
2. At the literal first parent, where the protected targets are singletons,
   the complete affected histogram of every exact substitute is identical.
   Thus every apparent label move is repaid exactly by its collar.  This is
   universal, not special to the rooted pentagon.
3. Rooted pentagons, coordinate-component packets, and mixed contexts
   compose integrally as port factors.  They do not compose as independent
   cap moves unless their whole flag signatures are put into common joint
   atoms.  Nested contexts generally make the outer gates depend on the
   inner choice.
4. For a fixed-collar packet changing \(k\) rows, at every
   \(q\ge s-1\),

   \[
       \frac12\|\Delta_q\|_1\le2(s-1)k.                \tag{0.5}
   \]

   Conversely, if \(L\) protected tokens in one carrier slice can reach at
   most \(b\) targets under the entire composed library, then

   \[
                         K_{q,p}\ge(L-bp)_+.            \tag{0.6}
   \]

The exact common-choice requirement is the coherent multidepth weighted
dual in Theorem 5.1 below, together with its integral rounding term.  None
of the three current atom families proves that dual.  In particular, a
single-transposition component library has \(b\le2\) on its distinguished
target orbit, while a rooted pentagon has zero complete action at its first
parent.  Mixed contexts can enlarge the reachable palette, but only after
their complete flag tables are joined; target labels chosen separately at
successive depths do not define a legal conveyor.

The new \(D_4\)-port factor is the first certified boundary primitive which
escapes the old pair-total invariant.  Its first-insertion pair totals are

\[
 (5,5,1,3)\quad\hbox{instead of}\quad(5,5,2,2).         \tag{0.7}
\]

Its complete matched singleton profile is nevertheless collar-cancelled.
It is useful only in the second architecture: a **parent-aligned**
replacement allowed to alter boundary/collar tokens.  After a further
outer lift, its length-\(2,3,6,7\) local interval profiles are nonzero, so
it is not universally shadow-invisible.  Their cap effect is exactly
state-dependent: the same profile can decrease, preserve, or increase
overload according to its residual background.  Section 3B gives the exact
tensor and hinge test.

Thus the nested early-label idea is closed.  The bottom-up idea survives
only as a **parent-aligned boundary-word conveyor**: one must transport the
whole deletion/insertion flag and every cyclic collar interval, not one
label.  The exact remaining assertion is stated in Section 7.

## 1. One fixed-collar internal slab inside an arbitrary ancestor

Fix a global rooted row with cyclic middle states \((Z_j)\).  A local
size-\(s\) slab occupies positions \(0,1,\ldots,s\), with open positions
\(1,\ldots,s-1\).  Its local coordinate set is \(J\), \(|J|=2s\).  A
fixed-collar substitution changes only the restrictions

\[
                         Z_t\cap J=X_t,
                   \qquad1\le t\le s-1,                \tag{1.1}
\]

and fixes \(Z_0,Z_s\), every state and transition token outside the slab,
and every restriction to the exterior of \(J\).  A parent-aligned
replacement which alters those collars is not covered by this model; its
correct state is the full cyclic boundary word of Section 3B.

For a depth \(q\), the target at start \(h\) is

\[
                         T_q(h)=\bigcap_{j=h}^{h+q}Z_j. \tag{1.2}
\]

Assume

\[
                         q\ge s-1,\qquad q+s-1<p,       \tag{1.3}
\]

so the displayed interval does not wrap around the entire global cycle.
This is the regime relevant when a logarithmic packet is viewed from its
own depth and from higher protected depths.

For \(1\le b\le s-1\), define the fixed left gate and carrier

\[
 G^-_{q,b}=\bigcap_{j=b-q}^{-1}(Z_j\cap J),
 \qquad
 B^-_{q,b}=\bigcap_{j=b-q}^{b}(Z_j\setminus J).         \tag{1.4}
\]

An intersection over an empty index interval is \(J\).  For
\(1\le a\le s-1\), define the fixed right gate and carrier

\[
 G^+_{q,a}=\bigcap_{j=s+1}^{a+q}(Z_j\cap J),
 \qquad
 B^+_{q,a}=\bigcap_{j=a}^{a+q}(Z_j\setminus J).         \tag{1.5}
\]

Again, an empty local-gate intersection is \(J\).  The objects in
(1.4)--(1.5) depend on the ambient row, context, depth, and offset, but not
on the chosen local substitute.

### Theorem 1.1 (exact fixed-collar ancestor flag formula)

For every \(q\) satisfying (1.3), the only targets which can change under
the local substitution are the following \(2(s-1)\) targets:

\[
 \boxed{
 T^-_{q,b}
   =B^-_{q,b}\cup\bigl(G^-_{q,b}\cap D_b\bigr),
       \quad1\le b\le s-1,}                            \tag{1.6}
\]

\[
 \boxed{
 T^+_{q,a}
   =B^+_{q,a}\cup\bigl(G^+_{q,a}\cap I_a\bigr),
       \quad1\le a\le s-1.}                           \tag{1.7}
\]

The start of (1.6) is \(b-q\), and the start of (1.7) is \(a\).

#### Proof

First,

\[
 \bigcap_{t=0}^{b}X_t
   =P\setminus\{\alpha_1,\ldots,\alpha_b\}=D_b.        \tag{1.8}
\]

Indeed, every inserted coordinate is absent from \(X_0\), while an
original coordinate survives all states through \(X_b\) exactly when it
has not yet been deleted.  Similarly,

\[
 \bigcap_{t=a}^{s}X_t
   =\{\beta_1,\ldots,\beta_a\}=I_a.                    \tag{1.9}
\]

Every original coordinate is absent from \(X_s=J\setminus P\), and an
inserted coordinate is present throughout \(X_a,\ldots,X_s\) exactly when
it was inserted by time \(a\).

Now classify a window meeting an open position.  If it starts at or before
zero and ends at or after \(s\), it contains both endpoint states.  Since

\[
                         X_0\cap X_s=P\cap(J\setminus P)
                                      =\varnothing,      \tag{1.10}
\]

its restriction to \(J\) is empty and is independent of every open state.
If it starts at or before zero but ends before \(s\), its endpoint in the
slab is a unique \(b\in\{1,\ldots,s-1\}\), and its start is \(b-q\).
Equations (1.4) and (1.8), with exterior and local coordinates separated,
give (1.6).  If it starts after zero, then meeting the open slab forces a
unique start \(a\in\{1,\ldots,s-1\}\); it contains \(X_a,\ldots,X_s\),
and (1.5) and (1.9) give (1.7).  A window meeting no open state is fixed.
These cases exhaust all starts. \(\square\)

### Corollary 1.2 (literal propagation of the child labels)

At every ancestor depth \(q\ge s-1\), the deletion label and insertion
label occur in the two marked targets

\[
 T^-_{q,s-1}
   =B^-_{q,s-1}\cup
       \bigl(G^-_{q,s-1}\cap\{\alpha_s\}\bigr),        \tag{1.11}
\]

\[
 T^+_{q,1}
   =B^+_{q,1}\cup
       \bigl(G^+_{q,1}\cap\{\beta_1\}\bigr).          \tag{1.12}
\]

Thus changing a child label \(x\) to \(y\) changes the corresponding
marked ancestor target by replacing \(G\cap\{x\}\) with
\(G\cap\{y\}\).  It need not literally replace \(x\) by \(y\): a context
gate may erase one or both labels.  In addition, all the other
\(D_b,I_a\) terms in (1.6)--(1.7) move with the same integral row choice.

## 2. Complete packet signatures and the sharp movement bound

Let \(K\) be a packet of \(k\) rooted rows.  For each root \(P\in K\),
let \((D_b^0(P),I_a^0(P))\) and
\((D_b^1(P),I_a^1(P))\) be its old and new flag pairs.  Define the complete
depth-\(q\) signed signature

\[
\begin{aligned}
 \Delta_{K,q}
 =\sum_{P\in K}\Bigg[&
  \sum_{b=1}^{s-1}
   \left(e_{B^-_{P,q,b}\cup(G^-_{P,q,b}\cap D_b^1(P))}
        -e_{B^-_{P,q,b}\cup(G^-_{P,q,b}\cap D_b^0(P))}\right)\\
 &+\sum_{a=1}^{s-1}
   \left(e_{B^+_{P,q,a}\cup(G^+_{P,q,a}\cap I_a^1(P))}
        -e_{B^+_{P,q,a}\cup(G^+_{P,q,a}\cap I_a^0(P))}\right)
                    \Bigg].                            \tag{2.1}
\end{aligned}
\]

This is the full ancestor action, including every collar.  Cancellation
between equal old and new targets is automatic in (2.1).

### Proposition 2.1 (uniform ancestor movement)

For every \(q\) satisfying (1.3),

\[
 \boxed{
       \frac12\|\Delta_{K,q}\|_1\le2(s-1)k.}           \tag{2.2}
\]

Consequently, for every current histogram \(\mu_q\),

\[
 \boxed{
  |K_p(\mu_q+\Delta_{K,q})-K_p(\mu_q)|
       \le2(s-1)k.}                                    \tag{2.3}
\]

#### Proof

There are \(2(s-1)k\) indexed occurrences in (2.1).  Moving one occurrence
contributes either zero or one negative and one positive unit.  This gives
(2.2).  Two histograms of equal total mass satisfy

\[
                         |K_p(x)-K_p(y)|
                           \le\frac12\|x-y\|_1,         \tag{2.4}
\]

because only mass removed from old coordinates can lower the hinge, and
the same argument with \(x,y\) reversed bounds an increase.  This proves
(2.3). \(\square\)

The bound is independent of the ancestor depth.  The naive count
\(q+s-1\) counts windows which contain both local endpoint states; (1.10)
shows that all of those windows are actually inert.

For a coordinate-component packet with new rooted row

\[
                         C'_P=\sigma C_{\sigma^{-1}P},  \tag{2.5}
\]

the new flags in (2.1) are

\[
 D_b^1(P)=\sigma D_b^0(\sigma^{-1}P),\qquad
 I_a^1(P)=\sigma I_a^0(\sigma^{-1}P).                  \tag{2.6}
\]

Thus (2.1), not merely the endpoint action
\(S\mapsto\sigma S\), is the exact ancestor vector of a
single-transposition component.  A rooted pentagon supplies a different
finite list of flag pairs, but enters the same formula.

## 3. Why endpoint labels are insufficient

The endpoint projection of a rooted row is

\[
 (D_{s-1},I_1)=(\{\alpha_s\},\{\beta_1\}).             \tag{3.1}
\]

For \(s\ge3\), this projection does not determine the two flags.  Holding
\(\alpha_s\) fixed, one may interchange \(\alpha_1,\alpha_2\); holding
\(\beta_1\) fixed, one may interchange \(\beta_2,\beta_3\).  Both choices
remain maximal Johnson geodesics with the same endpoints and the same two
labels, but change \(D_1\) or \(I_2\).  A gate which contains one exchanged
coordinate and not the other distinguishes their ancestor profiles in
(1.6) or (1.7).

Therefore there is no function

\[
             \text{ancestor profile}
              =F(\lambda^-,\lambda^+,\text{context})  \tag{3.2}
\]

valid for all port factors.  The correct state is the full pair of nested
flags (0.3)--(0.4).

### Theorem 3.1 (universal first-parent repayment)

Place any size-\(s\) exact port substitute in its literal one-node parent
of semilength \(s+1\), and inspect depth \(q=s\).  If old and new factors
agree outside the affected windows, then their complete affected singleton
histograms are equal.  In particular,

\[
                             \Delta_s=0.                \tag{3.3}
\]

#### Proof

In an exact factor of semilength \(s+1\), every coordinate belongs to
exactly \(\operatorname {Cat}_{s+1}\) rooted depth-\(s\) occurrences.
Every such target is a singleton, so the full depth-\(s\) histogram is

\[
              \operatorname {Cat}_{s+1}
                   \sum_x e_{\{x\}},                   \tag{3.4}
\]

independently of the factor.  Subtract the common histogram of all
unaffected slots. \(\square\)

This theorem includes the rooted-pentagon first-parent calculation as the
case \(s=3\).  It also applies to a complete component switch or any mixed
composition which is an exact parent factor.  Intrinsic marked labels can
move, but their total signed action is cancelled by the remaining terms of
(2.1).

The theorem is local to the literal first parent.  After further outer
lifting, targets have larger local parts, and point-margin conservation no
longer forces (3.3).  The higher action is then exactly (2.1).

### 3A. Strict-interior erasure and the missing scale gain

There is an even more elementary form of the first-parent obstruction.  If
a substituted slab lies strictly inside a matched ancestor window, then
that window contains both fixed ports \(P\) and \(J\setminus P\).  Its local
intersection is therefore empty by (1.10).  No choice made strictly inside
the hole is visible to that window.

Moving from scale \(s\) to \(s+1\) also creates no asymptotic counting
surplus.  Write

\[
 H_{m,s}=\frac12\binom{2(m-s)}{m-s}.                    \tag{3.5}
\]

With \(k=m-s\),

\[
 \frac{H_{m,s+1}}{H_{m,s}}
    =\frac{k}{2(2k-1)},
 \qquad
 \frac{\operatorname {Cat}_{s+1}}{\operatorname {Cat}_s}
    =\frac{2(2s+1)}{s+2}.                              \tag{3.6}
\]

Hence

\[
 \boxed{
 \frac{H_{m,s+1}\operatorname {Cat}_{s+1}}
      {H_{m,s}\operatorname {Cat}_s}
 =\frac{k(2s+1)}{(2k-1)(s+2)}=1+o(1)}                 \tag{3.7}
\]

whenever \(s\to\infty\) and \(s=o(m)\).  Thus the Catalan increase is
exactly repaid by the loss of parent contexts.  Passing to one higher scale
does not improve a supply-to-demand ratio normalized by
\(H_{m,s}\operatorname {Cat}_s\).  Combined with strict-interior erasure,
this closes the nested early-label variant.  Only substitutions aligned
with one boundary, and therefore exposing one of (1.6)--(1.7), survive.

### 3B. The complete \(D_4\) boundary primitive

Let \(F_0\) be the canonical MSW \(D_4\)-port factor and let \(G\) be the
explicit fourteen-row factor in
`MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md`.  For a rooted row write

\[
 q_F(P)=(\alpha_1,\alpha_2,\alpha_3,\alpha_4,
          \beta_1,\beta_2,\beta_3,\beta_4,9),           \tag{3.8}
\]

and, with cyclic indices in \(\mathbb Z_9\), put

\[
 I_{\ell,j}(q)=\{q_j,q_{j+1},\ldots,q_{j+\ell-1}\},    \tag{3.9}
\]

\[
 \boxed{
 \Delta_{\ell,j}
   =\sum_{P\in\mathcal D_4}
      \left(e_{I_{\ell,j}(q_G(P))}
            -e_{I_{\ell,j}(q_{F_0}(P))}\right).}       \tag{3.10}
\]

The two columns of fourteen words in that certificate determine every
entry of (3.10) by inspection.  If an ancestor target meets the local word
in segment \((\ell,j)\), has exterior carrier \(O\), and uses affine local
labelling \(\iota\), then the exact target action is

\[
                         \boxed{O\cup\iota(\Delta_{\ell,j}).}       \tag{3.11}
\]

Thus (3.10) is the complete higher-context profile, not only a marked
projection.

At the first-insertion position, its singleton vector is

\[
 \delta_{\beta_1}
    =4(e_3-e_2)-e_4-e_6+2e_7.                          \tag{3.12}
\]

For

\[
 E_0=\{1,8\},\quad E_1=\{2,3\},\quad
 E_2=\{4,5\},\quad E_3=\{6,7\},                       \tag{3.13}
\]

the four pair totals of (3.12) are

\[
                              (0,0,-1,+1),              \tag{3.14}
\]

which proves (0.7).  But if \(\delta_j=\Delta_{1,j}\), the complete
singleton ledger obeys

\[
                              \sum_{j\in\mathbb Z_9}\delta_j=0.    \tag{3.15}
\]

This is the exact collar repayment at the matched scale.

The cancellation does not persist at every higher interval length.  Put

\[
                         \Delta_\ell=\sum_{j\in\mathbb Z_9}
                                             \Delta_{\ell,j}.       \tag{3.16}
\]

The audited word table gives

\[
 \Delta_1=\Delta_4=\Delta_5=\Delta_8=0,                \tag{3.17}
\]

while

\[
 \frac12\|\Delta_2\|_1=19,qquad
 \frac12\|\Delta_3\|_1=22.                           \tag{3.18}
\]

Complementation gives the same masses for \(\Delta_7,\Delta_6\),
respectively.  Hence \(G-F_0\) is not collar-cancelled after an arbitrary
higher lift.  It has a genuine nonzero boundary action.

It does not have a state-independent cap sign.  For one pushed profile
write \(u\) for its old local load and \(\beta\) for fixed background,
and set \(c=(p-\beta)_+\).  The exact overload change is

\[
 \boxed{
 \Delta K_{\ell,j}
  =\sum_S\left[(u(S)+\Delta_{\ell,j}(S)-c(S))_+
                      -(u(S)-c(S))_+\right].}           \tag{3.19}
\]

If

\[
                         m_{\ell,j}=\frac12
                                      \|\Delta_{\ell,j}\|_1,       \tag{3.20}
\]

then

\[
                         -m_{\ell,j}\le\Delta K_{\ell,j}
                                      \le m_{\ell,j}.               \tag{3.21}
\]

Both extreme signs are algebraically realizable by residual backgrounds
whenever the ambient cap is larger than the finite local multiplicities.
To obtain the negative extreme, place the negative support above cap and
leave residual capacity on the positive support.  To obtain the positive
extreme, leave the negative support below cap and fill the positive support
to cap before adding the new units.  Disjoint positive and negative
supports permit these background choices independently.  This statement
does not assert that both artificial backgrounds occur as exact-factor
histograms; it proves that no background-free sign theorem is possible.
Thus no conservation law forces cancellation beyond (3.17), but the pair
transfer alone cannot certify descent.

At one aligned size-four scale the number of disjoint context slabs is

\[
 H_{m,4}=\frac12\binom{2(m-4)}{m-4}
             =\left(\frac1{1024}+o(1)\right)W.          \tag{3.22}
\]

The complete start-resolved table has \(m_{\ell,j}\le10\).  Therefore,
if one fixed pushed profile \((\ell,j)\) occurs once in every aligned
context, even perfect routing can decrease one depth's cap tail by at most

\[
                         10H_{m,4}
                          =\left(\frac{10}{1024}+o(1)\right)W.      \tag{3.23}
\]

For a general depth, with carrier-profile multiset \(\Pi_{C,q}\) in
context \(C\), the exact optimistic ceiling is

\[
 \boxed{
  |K_{q,p}(F')-K_{q,p}(F)|
     \le\sum_C\sum_{(\ell,j)\in\Pi_{C,q}}m_{\ell,j}.}  \tag{3.24}
\]

This is an explicit capacity bound, not a descent theorem: the same binary
choice in context \(C\) fixes the signs of every one of its profiles and at
every depth.

In particular:

* at the matched singleton scale, \(\Delta K=0\) for every background;
* at higher contexts, algebraic cap descent is possible and can use the
  nonzero profiles (3.18), but exact-factor routing is unproved;
* a proof of descent must align their negative supports with current
  overload and their positive supports with residual capacity, using one
  common choice across all depths.

## 4. What composes integrally

There are two valid composition operations.

1. A rooted port factor may be inserted in a common context which fixes
   its entrance and complementary exit port and preserves both the state
   and adjacent-union ledgers.  A fixed-collar deployment is governed by
   (2.1); a parent-aligned deployment which alters collar tokens requires
   the whole cyclic boundary-word tensor, as in (3.10).
2. Given a current anchored factor \(F\) and a port-preserving coordinate
   image \(\sigma F\), either complete shore of every ownership component
   may be chosen.  Recomputing a new overlay after a switch permits another
   such step.

Both operations preserve integrality and exact middle ownership.  Hence
rooted pentagons, single-transposition packets, and their mixed contextual
lifts can be composed as factors.

They need not compose as independent profile choices.  At a fixed family
of serviced depths, join two local substitutions whenever some protected
window depends on both of them.  Take transitive closure and call the
resulting blocks **profile atoms**.  A nested ancestor switch changes the
gates in (1.4)--(1.5) of a descendant switch, so a whole nested chain can
belong to one atom.  Likewise, component partitions from different
coordinate transpositions need not be laminar.

For every profile atom \(A\), let \(\mathscr L_A\) be the finite set of
joint integral states which are actually legal on that atom.  Every
affected window is assigned to the unique atom containing all choices on
which it depends.  Then and only then there are nonnegative simultaneous
histograms \(u_{A,g,q}\) and fixed backgrounds \(\lambda_q\) such that

\[
                 \mu_q^{\mathbf g}
                    =\lambda_q+\sum_Au_{A,g_A,q}        \tag{4.1}
\]

for one common integral choice \(g_A\in\mathscr L_A\) at every depth.
Equation (2.1) computes these histograms when an atom contains one slab;
for a nested atom it is applied after fixing the whole joint decorated
state.

## 5. The exact common-choice PCap theorem

Let

\[
 N_q=\binom p{m-q},\qquad c_q=W-N_q,\qquad
 K_p(x)=\sum_S(x(S)-p)_+,                              \tag{5.1}
\]

and, for a protected depth set \(\mathcal Q\), put

\[
 \operatorname {PCap}_{\mathcal Q}(F)
   =\sum_{q\in\mathcal Q}(K_p(\mu_q^F)-c_q)_+.          \tag{5.2}
\]

Choose a probability distribution \(\pi_A\) on each joint library and set

\[
 \bar\mu_q=\lambda_q+
       \sum_A\sum_{g\in\mathscr L_A}\pi_A(g)u_{A,g,q}. \tag{5.3}
\]

### Theorem 5.1 (coherent full-flag dual)

The minimum fractional PCap value equals

\[
\boxed{
\begin{aligned}
 \max_{0\le\gamma_q\le1}\Bigg\{&
  \sum_{q\in\mathcal Q}
   \left[
    \langle\gamma_q,\lambda_q-p\mathbf1\rangle
      -c_q\|\gamma_q\|_\infty
   \right]\\
 &+\sum_A\min_{g\in\mathscr L_A}
       \sum_{q\in\mathcal Q}
          \langle\gamma_q,u_{A,g,q}\rangle
                         \Bigg\}.                      \tag{5.4}
\end{aligned}}
\]

In particular, the minimizing state of one atom is common to all depths
and to every flag coordinate in (2.1).

#### Proof

For every nonnegative vector \(x\) and \(c\ge0\),

\[
 (K_p(x)-c)_+
 =\max_{0\le\gamma\le1}
   \left[
      \langle\gamma,x-p\mathbf1\rangle
       -c\|\gamma\|_\infty
   \right].                                            \tag{5.5}
\]

Indeed, first dualize each hinge in \(K_p\), multiply by the scalar which
dualizes the outer positive part, and absorb the scalar into \(\gamma\).
For fixed \(\gamma\), the least admissible scalar is
\(\|\gamma\|_\infty\).  Substitute (5.3), sum over \(q\), and apply
finite-dimensional minimax.  The minimization over each probability
simplex is attained at one joint state \(g\), yielding (5.4). \(\square\)

This is the precise common-integral-choice gate requested by the conveyor
problem.  Separate favorable choices for separate depths prove nothing
about (5.4).

For the integral step, independently sample the profile atoms according to
the same distributions and define

\[
 V_q(S)=\sum_A\operatorname {Var}_{\pi_A}u_{A,g,q}(S). \tag{5.6}
\]

Exactly as for one hinge, some integral choice satisfies

\[
 \boxed{
 \operatorname {PCap}_{\mathcal Q}(F_*)
 \le \operatorname {PCap}_{\mathcal Q}(\bar\mu)
   +\frac12\sum_{q\in\mathcal Q}\sum_S\sqrt{V_q(S)}.} \tag{5.7}
\]

Thus a sufficient integral theorem consists of (5.4) being \(o(W)\) and

\[
                  \sum_{q\in\mathcal Q}\sum_S
                         \sqrt{V_q(S)}=o(W).            \tag{5.8}
\]

Large nested profile atoms are precisely what can make (5.8) fail.

## 6. Explicit PCap bounds for a proposed conveyor

### 6.1 Action-capacity upper bound

Suppose a sequence of fixed-collar packet switches has shore sizes
\(k_1,\ldots,k_M\), each based at the same scale \(s\), and expose them
sequentially so that their actual increments are used.  Proposition 2.1
and the triangle inequality give, for every \(q\ge s-1\),

\[
 |K_{q,p}(F_M)-K_{q,p}(F_0)|
       \le2(s-1)\sum_{j=1}^Mk_j.                       \tag{6.1}
\]

Since an outer positive part is one-Lipschitz,

\[
 \boxed{
 |\operatorname {PCap}_{\mathcal Q}(F_M)
     -\operatorname {PCap}_{\mathcal Q}(F_0)|
 \le2(s-1)|\mathcal Q|\sum_{j=1}^Mk_j.}               \tag{6.2}
\]

This is an unconditional supply ceiling for the internal architecture.  It
grants every moved occurrence the correct sign and therefore is optimistic
for descent.  Parent-aligned packets instead use their boundary-word bound,
such as (3.24) for the \(D_4\) factor.

### 6.2 Carrier-palette lower bound

Fix a depth \(q\) and an exterior carrier slice \(B=S\setminus J\).
Suppose a specified family of \(L_{q,B}\) protected occurrences remains,
under every legal joint choice, inside a fixed target palette
\(\mathcal R_{q,B}\) of size \(b_{q,B}\).  Then

\[
 \sum_{S\in\mathcal R_{q,B}}(\mu_q(S)-p)_+
       \ge(L_{q,B}-pb_{q,B})_+.                        \tag{6.3}
\]

Indeed, the total load on these \(b_{q,B}\) targets is at least
\(L_{q,B}\), and

\[
                         \sum_{i=1}^b(x_i-p)_+
                           \ge\left(\sum_{i=1}^bx_i-bp\right)_+.
                                                                    \tag{6.4}
\]

Different carrier slices have disjoint target sets.  Therefore every
factor in the library obeys the explicit lower bound

\[
 \boxed{
 \operatorname {PCap}_{\mathcal Q}(F)
 \ge\sum_{q\in\mathcal Q}
   \left[
     \sum_B(L_{q,B}-pb_{q,B})_+-c_q
   \right]_+.}                                         \tag{6.5}
\]

This is the sharp elementary obstruction for a bottom-up palette.

For one single-transposition component library, a common distinguished
target in a fixed carrier slice remains in the two-point orbit
\(\{S,\sigma S\}\).  Hence \(b_{q,B}\le2\), and a plateau of mass \(L\)
forces

\[
              (K_{q,p}-c_q)_+\ge(L-2p-c_q)_+.           \tag{6.6}
\]

No choice of component packets changes this orbit census.  Using several
coordinate frames may enlarge the orbit, but their crossing component
partitions must then be placed in one joint profile atom before (5.4) can
be invoked.

For a rooted pentagon in its first parent, Theorem 3.1 is stronger than a
palette bound: its complete increment is zero.  At higher ancestors the
rooted pentagon may have nonzero action, but its palette is the set of all
gated flag-prefix targets in (1.6)--(1.7), not the set of its two endpoint
labels.  Mixed contexts can enlarge that palette; they do not remove the
coherent-choice condition.

### 6.3 Calibration at \(\operatorname {Cat}_s\asymp p\)

Put

\[
                         d=\operatorname {Cat}_s
                            =\theta p,                  \tag{6.7}
\]

with \(\theta\) bounded above and below by positive constants.  One base
child fibre has only constant cap demand.  The vertical problem appears
when \(a\) such fibres aggregate in one carrier palette.  Their protected
mass is \(L=ad\), so (6.3) requires

\[
                         b\ge\frac{ad-o(ad)}p
                           =a\theta-o(a)                \tag{6.8}
\]

merely to make their cap excess negligible.  Thus the reachable palette
must grow linearly with the number of aggregated child fibres.  A fixed
two-point coordinate orbit stalls immediately.  Any fixed finite rooted
packet palette stalls once \(a\) exceeds its palette size divided by
\(\theta\).  A genuine bottom-up conveyor must continually create new
physical target classes, while carrying one coherent choice of both full
flags through every ancestor.

## 7. Exact remaining theorem

The present atoms establish factor-level composability but not a cap
conveyor.  A sufficient positive statement is the following.

> **Parent-aligned boundary-word conveyor theorem.**  At a scale \(s\) with
> \(\operatorname {Cat}_s\asymp p\), construct a product-compatible atlas
> of joint decorated port factors, obtained from rooted packets,
> coordinate-component packets, or mixed contexts, such that:
>
> 1. every row choice specifies the entire deletion and insertion flags,
>    and every parent-aligned choice specifies all cyclic interval profiles
>    analogous to (3.10);
> 2. every serviced window is assigned to a joint atom containing all
>    choices on which its gates and flags depend;
> 3. for every multidepth weight family \((\gamma_q)\), the expression in
>    (5.4) is \(o(W)\);
> 4. the same fractional choices satisfy the integral fragmentation bound
>    (5.8); and
> 5. equivalently at the elementary-cut level, every aggregated carrier
>    family has palette size satisfying (6.8), up to a total \(o(W)\)
>    exceptional mass.

If these five clauses hold, (5.7) gives one integral factor with

\[
                         \operatorname {PCap}_{\mathcal Q}=o(W).     \tag{7.1}
\]

The first-parent rigidity theorem, the two-point orbit floor, and the
nonlaminarity of successive component partitions show that none of the
currently certified libraries satisfies these clauses by itself.  The new
\(D_4\) factor supplies a nonzero boundary tensor but no weighted routing
sign.  These facts do not rule out a genuinely mixed, growing-context
boundary-word atlas.  What remains is no longer a question of whether a
child label can be moved: it is whether one integral family of complete
boundary words can pass all carrier-weight tests simultaneously with small
joint atoms.
