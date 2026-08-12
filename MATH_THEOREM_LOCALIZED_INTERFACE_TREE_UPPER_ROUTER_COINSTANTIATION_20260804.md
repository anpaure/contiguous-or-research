# Localized interface-tree co-instantiation of a seam, an upper section,
# and a private router

**Date:** 2026-08-04  
**Status:** exact conditional composition and counting theorem. It does not
construct the required Boolean host and does not prove a new bound for
\(\nu(k)\).

## 0. Result

Write the eligible aperture seams in product-Johnson coordinates as

\[
 \Omega={A\choose h}\times {B\choose\ell},
 \qquad |A|=p,\quad |B|=q.                           \tag{0.1}
\]

Fix total coordinate footprints \(U\subseteq A\), \(V\subseteq B\). A
local profile is \(\lambda=(S,T)\), where \(S\subseteq U\), \(T\subseteq V\).
Its exact extension count is

\[
 n_\lambda=
 {p-|U|\choose h-|S|}
 {q-|V|\choose\ell-|T|}.                            \tag{0.2}
\]

Consider finite occurrence-labelled lower/pivot, all-width upper, and
compensated-router modules. Suppose their internal join trees can be
amalgamated through a tree of complete shared-variable separators. Suppose
also that for every profile in a set \(\Lambda\), one separator certificate
is supported by every module at every physical seam occurrence of that
profile outside a named exceptional bank \(E_\lambda\). Then the number of
seams possessing one common host tuple is at least

\[
 \boxed{\sum_{\lambda\in\Lambda}
        (n_\lambda-|E_\lambda|)_+.}                  \tag{0.3}
\]

This is a profile-refined local-coordinate-plus-occurrence-exception
theorem. Different profiles may use different upper selectors, cap states,
factor cascades, and exception banks.

The audited component theorems plug in literally:

* a pinned nonempty semijoin core of the dual upper target-choice CSP,
  followed by immutable reserve Hall, supplies the upper forest;
* a left-\(h_0\)-regular/right-at-most-\(h_0\) private claim--port factor
  followed by a left-\(q_0\)-regular private port--sink factor supplies the
  router when every sink \(s\) obeys

\[
 \sum_{f=ps}\deg_{B_0}(p)\le h_0q_0;                 \tag{0.4}
\]

* private finite-capacity interiors and certified complete boundary
  interfaces turn the joined abstract tuple into one literal object.

There is also an exact one-cycle extension. After attached trees are
eliminated, let

\[
 K_i\subseteq X_{i-1}\times X_i\quad(1\le i\le m),
 \qquad X_m=X_0                                      \tag{0.5}
\]

be the cycle transfer relations. The common join is nonempty exactly when

\[
 \boxed{(K_1\circ\cdots\circ K_m)\cap\Delta_{X_0}
        \ne\varnothing.}                             \tag{0.6}
\]

Thus the first hidden correlation beyond separator trees is a
three-relation cycle with a no-fixed-point transfer.

## 1. Product-slice profiles

For \(\lambda=(S,T)\), define

\[
 \Omega_\lambda=\{(P,Q)\in\Omega:
                  P\cap U=S,\ Q\cap V=T\}.            \tag{1.1}
\]

Binomial coefficients outside their natural range are zero.

### Lemma 1.1

The nonempty \(\Omega_\lambda\) partition \(\Omega\), and
\(|\Omega_\lambda|=n_\lambda\) as in (0.2).

#### Proof

After fixing \(P\cap U=S\), choose the other \(h-|S|\) holes from \(A-U\).
After fixing \(Q\cap V=T\), choose the other \(\ell-|T|\) entrants from
\(B-V\). Every seam has one such profile. \(\square\)

Let

\[
 \sigma:\Omega\longrightarrow\mathcal E              \tag{1.2}
\]

send a seam colour to its unique physical occurrence in a \(q1\)-exact
carrier. Only injectivity of \(\sigma\) will be used.

## 2. Amalgamating acyclic modules

For each module \(M\), let \(T_M\) be a join tree for its finite relation
scopes. Let \(G\) be a tree on the modules. For every edge \(MN\), choose
attachment nodes in \(T_M,T_N\) containing the complete separator

\[
 I_{MN}=\operatorname{Var}(M)\cap\operatorname{Var}(N).             \tag{2.1}
\]

Assume that modules identify no other variables, that modules containing
any fixed shared variable induce a connected subtree of \(G\), and that
every attachment along that subtree contains the variable.

### Lemma 2.1 (join-tree amalgamation)

The union of the module join trees plus the attachment edges is a join
tree for all host relations.

#### Proof

It is a tree because disjoint trees are connected according to \(G\).
Inside a module, relation nodes containing a fixed variable are connected.
Across modules, the displayed assumptions join those internal subtrees
along a connected module subtree. Hence the global running-intersection
property holds. \(\square\)

Choose one assignment on every separator \(I_{MN}\). It is a **separator
certificate** when, in each module, one tuple of the complete internal join
simultaneously has all incident separator restrictions. Individual support
on each separator is not enough.

### Lemma 2.2 (separator gluing)

A separator certificate gives a tuple in the complete natural join.

#### Proof

Choose the supporting tuple in every module. Adjacent tuples agree on
their complete shared-variable set. The tree structure and connectedness
of every shared variable glue them to one global assignment. \(\square\)

The separators may include the seam profile, cap/common state, phase flags,
complete boundary-bundle identity, physical occurrence addresses, and
terminal type. Equal set values at different physical addresses are not
identified unless their address variable is also equal.

## 3. Profiled seam survival

For every \(\lambda\in\Lambda\), fix a separator certificate
\(\theta_\lambda\) and an occurrence bank \(E_\lambda\subseteq\mathcal E\).
Assume:

> For every \((P,Q)\in\Omega_\lambda\) with
> \(\sigma(P,Q)\notin E_\lambda\), every module has one joined tuple
> simultaneously supporting its incident restrictions from
> \(\theta_\lambda\).

The module tuple may vary with the seam; the displayed separator values
are uniform within the profile.

### Theorem 3.1 (localized common-host theorem)

Every seam in

\[
 \Omega_\lambda-\sigma^{-1}(E_\lambda)               \tag{3.1}
\]

has one complete common host tuple, and (0.3) holds.

#### Proof

Fix such a seam. Lemma 2.2 glues its module tuples. Since \(\sigma\) is
injective, at most \(|E_\lambda|\) members of \(\Omega_\lambda\) map into
\(E_\lambda\). Lemma 1.1 gives at least
\((n_\lambda-|E_\lambda|)_+\) accepted seams in this fibre. Sum over the
disjoint fibres. \(\square\)

### Corollary 3.2 (one-profile test)

One common host exists if, for one profile \(\lambda=(S,T)\),

\[
 |E_\lambda|<
 {p-|U|\choose h-|S|}
 {q-|V|\choose\ell-|T|}.                            \tag{3.2}
\]

For the untouched profile this becomes

\[
 p-|U|\ge h,\quad q-|V|\ge\ell,\quad
 |E_{\varnothing,\varnothing}|<
 {p-|U|\choose h}{q-|V|\choose\ell}.                 \tag{3.3}
\]

If \(|U|,|V|,|E_\lambda|\) are bounded while
\(h,p-h,\ell,q-\ell\to\infty\), every nonempty fixed profile has unbounded
extension multiplicity. This uses bounded **total** footprint, not bounded
scope per constraint.

## 4. The upper and router modules

Fix one profile and separator certificate.

### Proposition 4.1 (upper certificate)

The upper module supports its pinned separator values if:

1. its dual target-choice relations have a running-intersection tree and a
   nonempty pinned semijoin core; and
2. with \(A_{\rm env}\) equal to the pivot plus every occurrence in the
   restricted witness menus,

\[
 |Y|\le
 \sum_{R:N_R^{\rm res}(A_{\rm env})\cap Y\ne\varnothing}
       (\mu_R-1)
 \qquad(Y\subseteq\mathcal K).                       \tag{4.1}
\]

Then its tuple contains one protected old witness of every target, exactly
one occurrence of every \(q1\) colour, and a deletion in every old
component.

#### Proof

The pinned semijoin core gives a rainbow witness selector. Immutable
reserve Hall (4.1) extends it to an upper-exact path forest while retaining
the protected boundary occurrence. Record those choices in the module
tuple. \(\square\)

For the router, fix in the same certificate one cap/guard/phase/occurrence/
type state and one compensation linkage. Delete its capacities and sinks.
Let

\[
 B_0=(G_0,P_0;E_0),\qquad K_0=(P_0,S_0;F_0)          \tag{4.2}
\]

be physical occurrence factors with

\[
 \deg_{B_0}(g)=h_0,\quad\deg_{B_0}(p)\le h_0,\quad
 \deg_{K_0}(p)=q_0,                                  \tag{4.3}
\]

and (0.4). Assume all displayed prefixes and suffixes coexist in that
state, have legal terminal types, and are private except at endpoints.
The incident separator may pin the residual state, factor records, and
terminal-type data. It may not pin a particular integral route unless that
route has separately been shown to exist; the flow argument chooses the
route inside the router module.

### Proposition 4.2 (router certificate)

Every gain has a capacity-disjoint route to a distinct legal sink.

#### Proof

Give every incidence chain \(g-p-s\) weight \(1/(h_0q_0)\). Each claim
emits one unit; each prefix has load \(1/h_0\); each port has load at most
one; each suffix has load at most \(1/q_0\); and (0.4) bounds each sink
load by one. Privacy accounts for all internal capacities. Integral max
flow gives the stated routes. \(\square\)

At \(h_0=q_0=2\), two private occurrence-lifted factors of right degree at
most two suffice. Two abstract Middle-Levels factors do not: their physical
lifts and common residual state remain hypotheses.

## 5. Literal private gluing

Assume additionally that, after compensation deletion:

1. module interiors are pairwise capacity-disjoint;
2. every shared occurrence is read-only or one complete combined bundle
   which prices its capacity once;
3. the lower boundary, aperture output, and wrap/diamond role share the
   opened seam only through such a complete bundle; and
4. every module uses the state fixed by the separator certificate.

### Corollary 5.1

If the lower/pivot module is literal and complete, Propositions 4.1--4.2
hold in every nonexceptional fibre counted by Theorem 3.1, and the four
private-gluing clauses hold, then every seam counted by (0.3) gives one
literal co-instantiated lower/upper/router pivot host. Gluing creates no
new omitted target or capacity violation.

If the module target ledgers are exhaustive and the pivot is the only new
source position, this local object has charge one. This does not assert
such a host in every dimension.

#### Proof

Theorem 3.1 gives a joined tuple. Proposition 4.1 supplies its protected
upper forest; Proposition 4.2 supplies its typed router. Private gluing
makes their quotient capacity-faithful, while the literal lower/pivot
module supplies the remaining ledger. \(\square\)

## 6. A single cyclic interface

Suppose instead that, after eliminating all attached join trees, the module
incidence graph is one chordless cycle: nonadjacent cycle modules share no
variable. Let \(X_i\) be the assignment set on the complete separator
between cycle modules \(i\) and \(i+1\), and project module \(i\) to

\[
 K_i\subseteq X_{i-1}\times X_i.                    \tag{6.1}
\]

### Theorem 6.1 (unicyclic fixed-point criterion)

The complete join is nonempty if and only if (0.6) holds.

#### Proof

A global tuple gives a closed sequence
\(x_0K_1x_1K_2\cdots K_mx_m\) with \(x_m=x_0\), hence a diagonal pair in
the composition. Conversely, a diagonal pair supplies such a sequence;
the definition of every \(K_i\) supplies an internal module tuple, and
equal separator assignments glue them around the cycle. \(\square\)

Theorem 3.1 remains valid profile by profile when its separator certificate
is replaced by uniform transfer relations satisfying (0.6).

### Proposition 6.2 (minimal hidden cycle)

For binary variables, put

\[
 K_1=\{(x,y):x=y\},\quad
 K_2=\{(y,z):y=z\},\quad
 K_3=\{(z,x):z\ne x\}.                              \tag{6.2}
\]

Every relation is nonempty, every unary projection is full, and every
pairwise join is nonempty. Their cyclic composition is disequality and has
no fixed point, so the triple join is empty.

This is minimal in relation count: one or two relation scopes admit a join
tree after empty relations are removed. It may be read as a cycle among an
upper chosen occurrence, a common cap/phase state, and a router terminal/
boundary state. Private physical interiors do not remove it.

## 7. Exact frontier

The theorem reduces the localized co-instantiation row to four checkable
tasks:

1. find one bounded total seam-coordinate footprint \(U,V\);
2. find one product-slice profile with a separator certificate, or a
   unicyclic fixed point, shared by lower, upper, and router modules;
3. confine residual occurrence-dependent failures in that profile to fewer
   addresses than (0.2); and
4. prove private physical footprints outside certified interfaces.

The current lower all-subset assignment, Boolean upper-menu geometry, and
physical router lift have not been proved to satisfy these rows. Separate
module feasibility, pairwise compatibility, and bounded scope per
constraint are insufficient.

No finite search, solver, random experiment, or computational candidate is
used.
