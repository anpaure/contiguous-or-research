# Audit of flat continuation gauges, Coxeter holonomy, and the odd two-router front end

**Date:** 2026-08-03  
**Status:** independent proof audit plus two unconditional refinements.  The
flat-gauge theorem is correct.  A cyclic word of adjacent Coxeter swaps is
shown to have nontrivial full-state holonomy despite zero aligned birail
current.  The odd coatom incidence graph supplies an exact left-two-regular
front-end router; its entire remaining supplier defect is the corank of one
suffix-port gammoid.  No all-dimensional physical suffix router is
constructed.

## 0. Verdict

Theorem 2.1 of
`MATH_THEOREM_FLAT_CONTINUATION_GAUGE_AND_LOCAL_HOLONOMY_CERTIFICATE_20260803.md`
is correct with its stated hypotheses:

* every oriented edge carries a **total bijection**;
* the reverse edge carries its inverse; and
* the checked fundamental loops, or the normal closure of the checked face
  loops, generate the full fundamental group.

The Cayley/Schreier qualification is load-bearing.  Translated defining
relators normally generate every closed word in a Cayley graph.  In a
Schreier graph they generate only the presentation kernel; nonidentity
stabilizer words give additional closed walks and require their own checks.

Two further conclusions follow.

1. A closed active-label walk can have zero additive birail current and
   still have nonidentity continuation holonomy.  For the most natural
   Coxeter cycle this failure is exact and explicit.
2. On the odd central owner/coatom incidence graph, two disjoint perfect
   matchings give every gain two edge-private ports with zero front-end Hall
   defect.  If the suffix-port strict gammoid has corank \(C\), all but at
   most \(C\) gains route integrally.  Thus the combinatorial owner front end
   is not the obstruction; the one remaining row is a complete-state suffix
   router of bounded corank.

## 1. Directed-edge and local-face audit

Let \(e:u\to v\) carry \(R_e:\Omega_u\to\Omega_v\).  The reverse edge must
literally carry \(R_e^{-1}\).  With this convention, backtracking cancels
and the transport defines a fundamental-groupoid representation.  For a
root \(o\), tree paths \(P_v:o\to v\), and a chord \(e:u\to v\), identity
of

\[
                         P_u eP_v^{-1}                 \tag{1.1}
\]

is exactly

\[
 R_{P_v}^{-1}R_eR_{P_u}=I,
 \qquad
 R_e=R_{P_v}R_{P_u}^{-1}.                             \tag{1.2}
\]

Putting \(g_v=R_{P_v}^{-1}\) gives

\[
                         R_e=g_v^{-1}g_u.             \tag{1.3}
\]

Conversely (1.3) telescopes on every walk.  This confirms the proof and its
composition order.

For a Coxeter generator \(s=s^{-1}\), the involution face is not the
untyped assertion that one same-fibre map squares to the identity.  At a
Cayley vertex \(g\), it is the translated two-edge identity

\[
            R_{gs,s}\,R_{g,s}=I_{\Omega_g}.          \tag{1.4}
\]

The commutation and braid checks are likewise equalities between the two
complete translated path transports with common endpoints.  Once local
gauges have identified all fibres, they may be written in the familiar
same-fibre notation; before that identification, the typed endpoints in
(1.4) are mandatory.

## 2. A closed Coxeter packet cycle is not flat

Let the active labels be \(0,1,\ldots,n-1\), and put

\[
 s_i=(i\ i+1)\quad(0\le i<n-1),
 \qquad s_{n-1}=(n-1\ 0).                             \tag{2.1}
\]

The aligned birail packet current for the active walk

\[
             0\to1\to\cdots\to n-1\to0              \tag{2.2}
\]

telescopes to zero in every audited additive profile.  Suppose, however,
that the complete continuation action of packet \(i\) contains the raw
label transposition \(s_i\).  Traversing (2.2) applies

\[
                         H=s_{n-1}s_{n-2}\cdots s_0. \tag{2.3}
\]

### Theorem 2.1 (cyclic adjacent-swap holonomy)

For \(n\ge3\),

\[
                         H=(1\ n-1\ n-2\ \cdots\ 2), \tag{2.4}
\]

with \(0\) fixed.  In particular \(H\ne I\).  For \(n=2\), the two
displayed generators are the same transposition and their product is the
identity.

### Proof

Apply the swaps in the order \(s_0,s_1,\ldots,s_{n-1}\).  The label zero
walks successively through \(1,2,\ldots,n-1\) and is returned to zero by
the last swap.  Label one first moves to zero and is then carried to
\(n-1\) only by the closing swap.  For \(2\le j<n\), the swap
\(s_{j-1}\) sends \(j\) to \(j-1\), and no later swap moves it again.
This is exactly (2.4). \(\square\)

Now allow vertex-dependent conjugacies \(c_i\), so the typed packet map is

\[
                         R_i=c_{i+1}^{-1}s_i c_i.     \tag{2.5}
\]

Their closed product is

\[
 R_{n-1}\cdots R_0=c_0^{-1}Hc_0,                    \tag{2.6}
\]

which is still nonidentity for \(n\ge3\).  Thus conjugating the packet
templates cannot turn the Coxeter element into a pure gauge.  It only
conjugates its holonomy.

This obstruction is compatible with a completely clean additive q1
ledger.  Fix two profiles \(P,S\), and take distinct active labels
\(x_0,\ldots,x_{n-1}\), cyclically indexed.  The signed q1 change of the
step \(x_i\to x_{i+1}\) can have the birail form

\[
 [P\cup\{x_{i+1}\}]+[S\cup\{x_i\}]
 -[P\cup\{x_i\}]-[S\cup\{x_{i+1}\}].               \tag{2.7}
\]

Summing (2.7) around the cycle is identically zero.  Within each rail the
values are pairwise distinct; barring a separately checkable equality
between a \(P\)-value and an \(S\)-value, the literal q1 palette is clean as
well.  Thus zero value current—even literal q1 cleanliness—does not imply
identity continuation holonomy.  The missing datum is genuinely the action
on the enlarged state fibre.

There are two formal repairs, neither free on a one-copy physical host.

* Repeat the cycle \(n-1\) times, the order of the permutation (2.4).
* Append the inverse Coxeter word.

Both reuse generator/socket types.  They preserve one-copy q1 resources
only if distinct physical occurrences and all corresponding capacities have
been supplied.  Additive birail cancellation alone does not supply them.

The appropriate flat packets are instead **relator faces**: involution,
commutation, braid, or another word whose complete continuation product is
already the identity.  A Coxeter element is a transport actuator, not a
flat reset.

## 3. Can residence and addresses satisfy the bijection premise?

Not in their currently projected forms.

### 3.1 Residence ages are relations, not total bijections

For one coordinate in a positive run, its age lies in
\(\{0,\ldots,d-1\}\).  At a survival transition it either refreshes to age
zero or advances by one.  If the macro record declares a refresh, multiple
old ages map to zero; the map is not injective.  If it declares no refresh,
age \(d-1\) has no legal image; the map is partial.  Therefore the projected
age update is not a total bijection of one fixed fibre and cannot satisfy
the flat-gauge theorem.

There are two proof-safe ways it could be made bijective.

1. Restrict every incident edge to a fully scheduled state fibre on which
   the update is one-to-one, then prove that all such edge-conditioned
   fibres agree at vertices.
2. Enlarge the state by the discarded refresh provenance, or by one complete
   cyclic refresh schedule, so shifting the schedule is reversible.

Either enlargement must itself return around every macro cycle.  Merely
remembering the current age does not.

There is one useful positive criterion for the second route.  Here take
\(C\) to be the rank-\(r\) **owner carrier** whose owners are windows of
\(d+1\) source letters, and let \({\cal R}(C)\) be its
occurrence-labelled positive coordinate runs.  For a run
\([s,t]\) of \(L=t-s+1\ge d+1\) owner vertices, the possible source
supplier positions lie in \([s+d,t]\).  The two endpoints are forced, and
successive suppliers may be at distance at most \(d+1\).  Thus its legal
supplier schedules are naturally indexed by compositions of

\[
                         L-d-1                              \tag{3.1}
\]

into parts in \(\{1,\ldots,d+1\}\), with the empty composition when this
integer is zero.  Hence the complete residence-schedule fibre is

\[
 \Omega_{\rm res}(C)=
 \prod_{R\in{\cal R}(C)}
       \operatorname{Comp}_{\le d+1}(|R|-d-1).        \tag{3.2}
\]

### Lemma 3.1 (run-isometric residence transport)

Suppose a macro edge from carrier \(C\) to carrier \(C'\) comes with a
bijection

\[
                 \psi:{\cal R}(C)\longrightarrow{\cal R}(C') \tag{3.3}
\]

preserving every run length.  Transporting the same composition from
\(R\) to \(\psi(R)\) gives a total bijection

\[
              R_\psi:\Omega_{\rm res}(C)\longrightarrow
                         \Omega_{\rm res}(C').        \tag{3.4}
\]

If the run maps themselves have pure-gauge form

\[
                         \psi_e=h_v^{-1}h_u          \tag{3.5}
\]

for vertex run identifications \(h_v\), then the induced residence maps
also have pure-gauge form and every closed macro walk has identity residence
holonomy.

#### Proof

The age-run theorem identifies a legal schedule independently with one
bounded-part composition on each labelled run.  Length preservation makes
the source and target composition sets in each paired factor identical, so
coordinatewise transport is a bijection.  Products of the run maps compose
functorially.  Thus (3.5) telescopes both the run bijections and their
product composition transports. \(\square\)

This provides an exact residence implementation for globally conjugate or
otherwise run-isometric packet copies.  A local packet which splits, merges,
shortens or lengthens runs does not meet it.  There is then an immediate
cardinality obstruction: if

\[
 \prod_{R\in{\cal R}(C)} f_{d+1}(|R|-d-1)
 \ne
 \prod_{R'\in{\cal R}(C')} f_{d+1}(|R'|-d-1),        \tag{3.6}
\]

where \(f_{d+1}\) is the bounded-composition count, no total residence-fibre
bijection can exist.  Equality of these products is only a cardinality
test, not a canonical transport.

If instead \(C\) denotes the contracted coatom-state cycle whose states are
unions of only the last \(d\) letters, the age-run convention shifts by one:
the corresponding formula is
\(\operatorname{Comp}_{\le d}(L-d)\).  These two conventions must not be
mixed.  The owner-carrier formula (3.2) is the one relevant to the
depth-\(d\) factor used in the mandatory-collar theorem.

### 3.2 Address transport is normally partial

An occurrence packet usually rebinds only a subset of the physical
addresses.  Such local partial maps define one global bijection exactly when
they agree on every actual domain intersection and have no cross-image
collision.  Equality of typed value decks does not imply this atomwise
condition.  Consequently the address part fits the pure-gauge premise only
after either:

* one actual global permutation of the complete address universe has been
  exhibited for every generator; or
* every local partial map has been extended compatibly to such a
  permutation and the translated relator identities have been replayed on
  those extensions.

Exterior-fixed use is stronger still: the permitted gauges must belong to
the pointwise stabilizer of the protected exterior.  A coordinate rotation
or reversal which moves that exterior is not a cost-free gauge.

Thus a deliberately equivariant Cayley packet bank could plausibly satisfy
flatness if its complete refresh schedules, histories, addresses and packing
coordinates are all transported by the same free group action.  The current
residence and address projections do not prove that premise.

## 4. The odd coatom layer supplies an exact two-port front end

Put \(k=2r-1\).  Let

\[
 {\cal Q}={{[k]}\choose r-1},
 \qquad
 \Omega={{[k]}\choose r}.                            \tag{4.1}
\]

The containment graph \(B=({\cal Q},\Omega;\subset)\) is \(r\)-regular on
both shores.  By repeated bipartite matching, its edge set decomposes into
\(r\) disjoint perfect matchings.  Choose any two, \(M_0,M_1\).

Treat a coatom role \(Q\in{\cal Q}\) as a gain claim and the two incidences
in \(M_0\cup M_1\) as its two private front-end ports.  The resulting graph
is left-two-regular and right-two-regular, and every gain family has zero
front-end Hall defect.

The downstream suffix network is a strict gammoid \(\Gamma\) on the port
set \(P\).  Put

\[
 D_B=\max_{X\subseteq{\cal Q}}(|X|-|N_B(X)|),
 \qquad
 C_B=|P|-r_\Gamma(P).                                \tag{4.2}
\]

Here \(D_B=0\) for the two-factor front end.

### Theorem 4.1 (front-end defect plus suffix corank)

The maximum number of gain claims which can be linked through one incident
port to pairwise disjoint suffix sinks is at least

\[
                         |{\cal Q}|-D_B-C_B.         \tag{4.3}
\]

In particular, the odd two-matching front end loses at most \(C_B\) gains.
If the complete port bank has a reference suffix matching, then \(C_B=0\)
and every gain links integrally.

### Proof

Rado's rank formula for the matroid induced on a gain family \(X\) is

\[
 r(X)=\min_{Y\subseteq X}
       \bigl(|X-Y|+r_\Gamma(N_B(Y))\bigr).            \tag{4.4}
\]

Matroid rank can fall by at most the number of deleted ground elements, so

\[
 r_\Gamma(N_B(Y))
 \ge r_\Gamma(P)-|P-N_B(Y)|
 =|N_B(Y)|-C_B.                                      \tag{4.5}
\]

The definition of \(D_B\) gives
\(|N_B(Y)|\ge|Y|-D_B\).  Substitution in (4.4) gives

\[
 r(X)\ge |X|-D_B-C_B.                                \tag{4.6}
\]

Apply this to the complete gain shore. \(\square\)

The theorem is exact at the level of the fixed capacity-faithful suffix
network.  It does not say that the two bare containment incidences are
literal complete paths.  Every owner/occurrence, phase, residence, history,
address and supplier resource required after the port must occur in the
same gammoid.  If two phase paths are jointly required to service one claim,
that paired object must first be represented by one capacity-faithful gadget;
two independent gammoids cannot be combined by (4.3).

## 5. Combined mathematical frontier

The two positive abstract pieces now fit exactly:

1. the odd coatom layer gives a zero-defect two-port front end;
2. bounded suffix-port corank gives bounded gain loss;
3. a flat full-state Cayley complex removes continuation holonomy; and
4. a literal value coboundary transports the lower compiler.

The Coxeter calculation shows what cannot be substituted for item 3: a
closed active-label walk with telescoping additive current is generally a
nontrivial continuation actuator.  The remaining uniform theorem is
therefore the following concrete physical statement.

> **Complete-state two-router lemma.**  Realize two disjoint odd-coatom
> incidence matchings as literal private claim-to-port prefixes in one
> child; give their complete suffix-port bank bounded strict-gammoid corank;
> and realize the packet support as a Cayley/relator complex whose translated
> faces act trivially on the enlarged residence/address/history/packing
> state.

If the corank and the exterior/compiler exceptions are uniformly bounded,
the existing contraction theorem yields \(B(k)+O(1)\).  This audit proves
the front-end and holonomy algebra, not that physical complete-state
two-router lemma.
