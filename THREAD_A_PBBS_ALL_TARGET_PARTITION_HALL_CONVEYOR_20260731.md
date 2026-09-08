# All-target protected PBBS conveyors: exact partition--Hall and the conserved-key obstruction

Date: 2026-07-31  
Lane: A, pure mathematics  
Status: theorem and sharp obstruction.  This is exact for the stated
one-cut/full-fragment colour-back/key-forward catalogue.  It does not prove
that the catalogue is nonempty in every dimension, and therefore does not
by itself prove `nu(k)=B(k)`.

## 1. Setting and exact casualty set

Let

\[
                 F=C_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup} C_b
\tag{1.1}
\]

be a lower-\(q_1\)-rainbow Johnson factor on rank-\(r\) owners.  Assume that
\({\cal U}\) is the complete required proper upper-target universe.  Let
\({\cal U}_F\subseteq{\cal U}\) be the targets having an interval-union
witness in \(F\), and put

\[
                         {\cal H}_F={\cal U}\setminus{\cal U}_F.
\tag{1.2}
\]

Thus \({\cal H}_F\) is the source-hole set (the 1,838-target set in the
frozen K17 calibration).  Choose one directed cut edge on every component,

\[
             e_i=t_i s_i,
\tag{1.3}
\]

and orient the resulting whole-component fragment as

\[
             P_i=(s_i,\ldots,t_i).
\tag{1.4}
\]

Write

\[
 c_i=t_i\cap s_i,\qquad \kappa_i=t_i\setminus s_i.
\tag{1.5}
\]

The cut colours \(c_i\) are pairwise distinct because the source factor is
lower-rainbow.

For an upper target \(Y\), let \({\cal I}_{C_i}(Y)\) be its
occurrence-labelled cyclic witness intervals on \(C_i\), and let

\[
 K_{C_i}(Y)=\bigcap_{I\in{\cal I}_{C_i}(Y)}\operatorname{span}(I)
\tag{1.6}
\]

when \(C_i\) supports \(Y\in{\cal U}_F\).  Define the exact seam-debt set

\[
 {\cal D}({\bf e})={\cal H}_F\cup
 \left\{Y\in{\cal U}_F:
     e_i\in K_{C_i}(Y)
     \text{ for every component }C_i\text{ supporting }Y
 \right\}.
\tag{1.7}
\]

Thus \(Y\notin{\cal D}({\bf e})\) if and only if \(Y\) was already covered
and at least one old witness remains inside a cut fragment.  The debt set
contains both the original holes and every newly created casualty.  This is
a global condition over all supporting components, not the list of targets
assigned to one chosen provider.

Assume henceforth that every \(P_i\) has full OR \([k]\).  This holds for a
one-cut canonical PBBS component by site homomesy.  It follows from the
suffix/full-fragments/prefix formula that every proper upper target newly
created by a braid crosses exactly one seam.

For an ordered physical seam \(i\to j\), put

\[
 {\cal S}(i,j)=
 \left\{Y:\ Y=S\cup Q
   \text{ for some }S\in\operatorname{Suf}(P_i),\ 
                         Q\in\operatorname{Pre}(P_j)\right\}.
\tag{1.8}
\]

This is the exact occurrence-labelled one-seam service set.

## 2. Exact residence states

Fix the desired deadline-staircase specification.  There is a deterministic
finite transducer for it at fixed \((k,W)\): its state stores the current
position, the coordinatewise boundary-run data, and the completed short-run
event list; at the terminal state one applies the exact threshold optimizer.
Call its state set \(\Sigma\), its initial state \(\sigma_0\), and its
accepting set \(A\).  This is an exact state representation, not a local
run heuristic.

A **state-labelled opening option** on \(C_i\) consists of the physical
cut/orientation (1.3)--(1.4), an input state \(\alpha_i\), and the forced
output state

\[
                  \beta_i=\Phi_{P_i}(\alpha_i).
\tag{2.1}
\]

An arc \(i\to j\) is state-compatible when

\[
                         \beta_i=\alpha_j.
\tag{2.2}
\]

If the root option has \(\alpha_a=\sigma_0\), the terminal option has
\(\beta_t\in A\), and all arcs of an \(a\)-to-\(t\) path satisfy (2.2),
then the literal concatenation passes the exact residence/staircase test.
This formulation also explains why separately run-safe seams do not
compose in general.

## 3. Colour-back/key-forward arcs conserve one global key

Call a physical Johnson seam \(i\to j\) a **conveyor arc** when, in addition
to (2.2),

\[
             t_i\cap s_j=c_i,
             \qquad
             \kappa_j\in t_i.
\tag{3.1}
\]

The first equality pays the source cut colour backward.  The second carries
the departure key needed to replace the canonical outward-ray casualties
at the destination.

### Lemma 3.1 (conserved-key law)

Every conveyor arc \(i\to j\) satisfies

\[
                         \kappa_i=\kappa_j.
\tag{3.2}
\]

Consequently every connected colour-back/key-forward conveyor has one
global key \(\kappa\).

#### Proof

By (1.5),

\[
                         t_i=c_i\mathbin{\dot\cup}\{\kappa_i\}.
\]

The first equality in (3.1) says that the unique element of \(t_i\) absent
from \(s_j\) is \(\kappa_i\).  But \(\kappa_j\notin s_j\), while the second
condition in (3.1) says \(\kappa_j\in t_i\).  Hence
\(\kappa_j=\kappa_i\).  Connectivity propagates the equality. \(\square\)

For a fixed global key \(\kappa\), write

\[
                  t_i=c_i\cup\{\kappa\}.
\tag{3.3}
\]

Then the colour-back part of (3.1) is equivalent to

\[
                  c_i\subset s_j\subset [k]\setminus\{\kappa\}.
\tag{3.4}
\]

The destination cut colour \(c_j\) is another rank-\((r-1)\) subset of
\(s_j\).  Exactness of the old lower palette gives \(c_i\ne c_j\), and
therefore

\[
             |c_i\cap c_j|=r-2,
             \qquad s_j=c_i\cup c_j.
\tag{3.5}
\]

Thus, before any target or residence guard is imposed, the conveyor graph
is the physical lift of the Johnson graph
\(J([k]\setminus\{\kappa\},r-1)\) on the selected cut colours.  A connected
linear conveyor requires a component-transversal simple Johnson path in
this quotient; a cyclic conveyor requires a component-transversal Johnson
cycle.

### Corollary 3.2 (first exact obstruction)

For component \(C_i\), let \(K_i^{\rm prot}\) be the set of keys occurring
among its admissible protected opening options.  A necessary condition for
a connected all-component conveyor is

\[
                         \bigcap_{i=1}^b K_i^{\rm prot}\ne\varnothing.
\tag{3.6}
\]

This obstruction is invisible to target-wise provider degrees.  Site
homomesy guarantees raw deletion transitions for every coordinate, but it
does not guarantee that a transition remains after wedge, witness, and
residence guards.

## 4. Exact all-target partition--Hall theorem

Fix now:

* a common-key state-labelled option on every component;
* a root \(a\) and terminal \(t\);
* an acyclic directed component skeleton \(D\).

Require the fixed root option to have \(\alpha_a=\sigma_0\) and the fixed
terminal option to have \(\beta_t\in A\).

Put

\[
                  L=[b]\setminus\{t\},\qquad
                  R=[b]\setminus\{a\}.
\tag{4.1}
\]

Let \(G\subseteq L\times R\) consist of the conveyor arcs lying in \(D\).
For a map

\[
                    \psi:{\cal D}({\bf e})\longrightarrow R,
\tag{4.2}
\]

define \(G_\psi\) by retaining \(i\to j\in G\) precisely when

\[
                    \psi^{-1}(j)\subseteq {\cal S}(i,j).
\tag{4.3}
\]

Empty fibres impose no condition.

### Theorem 4.1 (all-target partition--Hall equivalence)

Within the fixed option/skeleton catalogue above, there is an
\(a\)-to-\(t\) colour-back/key-forward braid which

1. has lower ledger \(H=1,E=0\);
2. passes the exact residence/staircase transducer; and
3. covers every required upper target, retaining or exactly replacing every
   previously covered target and installing every source hole

if and only if there exists a map \(\psi\) as in (4.2) such that

\[
              |N_{G_\psi}(X)|\ge |X|
              \qquad\text{for every }X\subseteq L.
\tag{4.4}
\]

#### Proof

Suppose first that \(\psi\) and (4.4) exist.  Hall's theorem gives a
matching saturating \(L\).  Since \(|L|=|R|=b-1\), it also saturates
\(R\).  Directing its edges gives outdegree one at every component except
\(t\), indegree one at every component except \(a\), and the complementary
zero degrees at \(a,t\).  It is therefore one \(a\)-to-\(t\) path plus
directed cycles.  All selected arcs lie in the acyclic skeleton \(D\), so
no cycle occurs and the matching is one spanning path.

Every seam leaving component \(i\in L\) has lower colour \(c_i\).  These
colours are distinct and are exactly all deleted cut colours except
\(c_t\).  Hence the lower ledger is \(H=1,E=0\).

Every target outside \({\cal D}({\bf e})\) has an old interval contained in
some fragment by (1.7).  If \(Y\in{\cal D}({\bf e})\), let
\(j=\psi(Y)\).  The selected matching has a unique incoming arc
\(i\to j\), and (4.3) gives \(Y\in{\cal S}(i,j)\).  Thus that literal seam
interval replaces \(Y\).  Finally, state compatibility along the one path,
the initial-state condition, and terminal acceptance prove the exact
residence claim.

Conversely, suppose such a braid exists.  Its seams form a perfect matching
from \(L\) to \(R\).  Every debt \(Y\in{\cal D}({\bf e})\) must have a new
witness.  Because every fragment has full OR, every proper new witness
crosses exactly one seam.  Choose one such seam and define \(\psi(Y)\) to be
its head component.  The braid matching is then contained in \(G_\psi\),
so it witnesses (4.4). \(\square\)

The quantifier over \(\psi\) is essential.  It allows one seam to service a
whole nested ray bundle.  Replacing it by a matching which uses a distinct
seam for every target is sound but can be arbitrarily wasteful.

### Corollary 4.2 (canonical protected-ray form)

Suppose every nonroot option is a wedge-flank option and every assigned
fixed-width old witness destroyed by its cut is the corresponding outward
ray.  Then key-forward in (3.1) reproduces the complete ray bundle,
simultaneously at every depth.  If the root cut leaves one assigned witness
of every root-guarded old target intact, and every source hole belongs to
the service set of its assigned incoming seam, Theorem 4.1 applies.  In
particular this conclusion both protects the complete old upper tower and
installs the source holes.

#### Proof

For a destination cut \(t_js_j\), an outward geodesic casualty has union

\[
 \{\kappa_j\}\cup s_j\cup s_{j,2}\cup\cdots.
\]

A conveyor predecessor \(t_i\) is Johnson adjacent to \(s_j\) and contains
\(\kappa_j\).  Therefore replacing \(t_j\) by \(t_i\) gives the identical
union at every depth.  All nonroot assigned casualties are restored by
their incoming seams, while the root assignment survives internally.  The
assumed seam providers install the source holes.  The rest follows from
Theorem 4.1. \(\square\)

## 5. Aharoni--Haxell bundle sufficient condition

The exact criterion (4.4) is often preferable to a generic
Aharoni--Haxell bound because several targets may share one seam.  The
following is nevertheless a rigorous constructive sufficient condition.

Let \({\cal D}({\bf e})\) be partitioned into nonempty bundles

\[
                  {\cal B}_1\mathbin{\dot\cup}\cdots
                    \mathbin{\dot\cup}{\cal B}_h.
\tag{5.1}
\]

For each \(\ell\), let \({\cal H}_\ell\) be the bipartite graph on
\(L\dot\cup R\) whose edge \(ij\) is an arc of \(G\) satisfying

\[
                         {\cal B}_\ell\subseteq{\cal S}(i,j).
\tag{5.2}
\]

### Theorem 5.1 (bundle AH plus robust filler)

Assume

\[
 \nu\left(\bigcup_{\ell\in J}{\cal H}_\ell\right)
                   >2(|J|-1)
 \qquad(\varnothing\ne J\subseteq[h])
\tag{5.3}
\]

and the base conveyor graph is \(h\)-robust Hall:

\[
 |N_G(X)|\ge |X|+h
 \quad\text{whenever }X\subseteq L,
                  \ 1\le |X|\le b-1-h.
\tag{5.4}
\]

Then the conclusion of Theorem 4.1 holds.

#### Proof

The rank-two Aharoni--Haxell theorem applied to (5.3) gives pairwise
vertex-disjoint edges \(e_\ell\in{\cal H}_\ell\).  Let \(L_0,R_0\) be
their source and head sets, each of size \(h\).  For
\(X\subseteq L\setminus L_0\), one has \(|X|\le b-1-h\), and hence

\[
 |N_{G-L_0-R_0}(X)|
       \ge |N_G(X)|-|R_0|
       \ge |X|.
\]

Hall supplies a perfect matching between the remaining shores.  Together
with the \(e_\ell\), this is a perfect matching from \(L\) to \(R\).
The acyclic skeleton turns it into one spanning path.  Each bundle is
served by its distinguished edge, and all other conclusions follow as in
Theorem 4.1. \(\square\)

Condition (5.3) is only sufficient.  For \(J=[h]\), its left side is at
most \(b-1\), so it cannot certify a large bundle bank unless

\[
                         b-1>2(h-1).
\tag{5.5}
\]

This is why target-by-target Aharoni--Haxell is the wrong generic theorem
for an all-depth wedge tower: the natural task is a whole outward-ray
bundle, not one depth at a time.

## 6. Variable options and the exact equality obstruction

Theorem 4.1 fixes one state-labelled option on each component.  There is an
exact coupled formulation before that choice.

Fix \(a,t,D\) and a common key \(\kappa\).  For every source component
\(i\ne t\), form a part \({\cal A}_i\) whose elements are candidate arcs

\[
                       A=(i,p_i;j,q_j),
\tag{6.1}
\]

where \(p_i\) and \(q_j\) are protected state-labelled options of key
\(\kappa\), and the physical seam satisfies all colour, service, and state
conditions.  Put a conflict between two candidates when

1. they have the same destination component; or
2. one enters an intermediate component \(j\) with option \(q_j\), while
   the candidate chosen from source part \({\cal A}_j\) leaves with a
   different option \(p_j\ne q_j\).

Restrict root-source options to initial states and terminal-destination
options to accepting states.

Because the old-casualty set depends on the as-yet unchosen cuts, it cannot
be inserted into a preselection Haxell graph without further data.  Fix one
occurrence-labelled old witness \(I_Y\) for every
\(Y\in{\cal U}_F\), and for an option \(q\) define its local assigned
casualty bundle

\[
 {\cal B}(q)=\{Y:\ I_Y\text{ lies on the component of }q
                    \text{ and the cut of }q\text{ meets its span}\}.
\]

Restrict root options to those with \({\cal B}(p_a)=\varnothing\).  For the
fixed source-hole set choose an assignment

\[
                        \psi_H:{\cal H}_F\longrightarrow R.
\]

Let \({\cal A}_i^{\psi_H}\subseteq{\cal A}_i\) consist of the candidates
\(A=(i,p_i;j,q_j)\) whose literal seam service set contains

\[
                       {\cal B}(q_j)\cup\psi_H^{-1}(j).
\]

Let \(\Gamma_{\psi_H}\) be the conflict graph induced by these restricted
parts.

### Proposition 6.1 (option-consistent independent transversal)

A conflict-free transversal choosing one member of every restricted part
\({\cal A}_i^{\psi_H}\) gives an option-consistent protected conveyor in
the acyclic skeleton which preserves every assigned old witness or replaces
it, and which installs every source hole.  In particular, if

\[
                         |{\cal A}_i^{\psi_H}|>
                              2\Delta(\Gamma_{\psi_H})
                         \qquad(i\ne t),
\tag{6.2}
\]

then Haxell's independent-transversal theorem supplies the full
option-consistent, all-debt conveyor.

#### Proof

Distinct-destination conflicts and the equality of the two shore sizes
make the selected destinations a permutation of \(R\).  At every
intermediate component, the second conflict rule says that its incoming and
outgoing records use exactly the same physical cut, orientation, and
transducer state.  The acyclic skeleton turns the degree cover into one
path.  Conversely, the outgoing arcs of any such path give a conflict-free
transversal.  Membership in the restricted part says that the selected
incoming arc at every destination services its complete local assigned
casualty bundle and its source-hole fibre.  Hence every previously covered
target retains its assigned witness or receives an exact replacement, and
every source hole is installed.  The
sufficient inequality is the standard independent-transversal bound.
\(\square\)

This equality constraint is not an ordinary matching resource: the
incoming and outgoing records must use the *same* option, whereas a resource
matching would forbid equality.  Thus a marginal endpoint/colour
Aharoni--Haxell theorem cannot replace Proposition 6.1.

The smallest abstract obstruction already has three components
\(a,b,t\).  Suppose the only legal incoming arc \(a\to b\) uses option
\(q_b\), while the only legal outgoing arc \(b\to t\) uses
\(p_b\ne q_b\).  Every endpoint, colour, and target-service marginal is
saturated, but no physical braid exists.  This two-arc example proves that
option consistency is a real extra gate, not bookkeeping.

## 7. Proved boundary

Theorem 4.1 is an exact all-target theorem for fixed one-cut/full-OR
options, not merely a theorem about a pre-existing hole list.  It uses the
complete source-hole-plus-new-casualty debt set (1.7) and complete one-seam
service sets (1.8).  Its Aharoni--Haxell corollary is constructive and residence-safe
because residence is carried by exact transducer states.

What remains unproved for unconditional PBBS is the existence of a common
key, protected state-labelled options, a target partition, and an acyclic
skeleton satisfying (4.4).  The current K17 statement that 1,838 missing
targets have many endpoint providers does not verify this hypothesis: it
treats \({\cal H}_F\) but does not simultaneously impose every new
casualty in \({\cal D}({\bf e})\setminus{\cal H}_F\), the conserved key,
option-equality, or exact residence-state conditions.

The sharpest unconditional obstruction is the conserved-key law (3.2),
followed, for any fixed key/options, by an ordinary Hall cut in (4.4).
The common-key obstruction is exact for this strict catalogue, in which
every destination is key-forward.  If a component's complete assigned
casualty bundle is empty, key-forward may be omitted there and the key may
reset; in that case its incoming seam is already safe for the old tower.
This active/inactive dichotomy is proved in
[MATH_THEOREM_A_ACTIVE_BUNDLE_CONVEYOR_DICHOTOMY_20260731.md](MATH_THEOREM_A_ACTIVE_BUNDLE_CONVEYOR_DICHOTOMY_20260731.md).
Multiple cuts or noncanonical suffix/full/prefix service can evade the
conserved-key law; they are outside the exact scope of this note and require
the full multi-fragment protected-span CSP.
