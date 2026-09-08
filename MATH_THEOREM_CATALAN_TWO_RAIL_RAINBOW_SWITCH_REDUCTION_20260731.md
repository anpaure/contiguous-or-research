# Catalan two-rail rainbow switches for the odd lift

Date: 2026-07-31  
Status: exact hosted local-switch reduction; the rainbow switch matching,
connected fragment permutation, and protected compiler conditions are not
proved in every dimension.  The local-switch class is a strict subclass of
the general two-rail endpoint-complement braid.

## 1. The two parent rails

Let \(m\ge2\) and put

\[
 M=\binom{2m}{m},\qquad
 N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname{Cat}_m,
\]

and add a new coordinate \(z\).

Take a saturating cycle between ranks \(m\) and \(m+1\) of \(Q_{2m}\):

\[
 C_0,U_0,C_1,U_1,\ldots,C_{N-1},U_{N-1},C_0,
 \tag{1.1}
\]

where all \(U_i\in\binom{[2m]}{m+1}\) occur, the \(C_i\) are distinct
\(m\)-sets, and \(C_i,C_{i+1}\subset U_i\). The \(U\)-rail is therefore a
Hamilton cycle of \(J(2m,m+1)\), with edge

\[
 U_{i-1}U_i
\quad\hbox{of lower colour}\quad C_i.
 \tag{1.2}
\]

Let

\[
 {\cal E}=\binom{[2m]}m\setminus\{C_0,\ldots,C_{N-1}\},
 \qquad |{\cal E}|=K.
 \tag{1.3}
\]

Choose an injection \(\phi:{\cal E}\to\binom{[2m]}{m+1}\) with
\(X\subset\phi(X)\), as supplied by the Catalan cap-two theorem. If
\(\phi(X)=U_i\), insert \(X\) in the block \(C_i,C_{i+1}\). This gives the
\(C\)-rail Hamilton cycle \(P\) on all \(M\) middle \(m\)-sets.

## 2. The one-of-two split-switch matching

For \(X\in{\cal E}\) hosted in \(U_i\), its two incident block edges are

\[
 XC_i,\qquad XC_{i+1}.
\]

A **split-switch choice** selects one endpoint to retain,

\[
 R_X\in\{C_i,C_{i+1}\},
\tag{2.1}
\]

and writes \(J_X\) for the other endpoint, whose edge \(XJ_X\) will be
cut. It is **rainbow** when

\[
 \boxed{
 \begin{aligned}
 &J_X\text{ are pairwise distinct},\\
 &\{C_i\cap C_{i+1}:U_i\notin\operatorname{im}\phi\}\\
 &\qquad{}\sqcup
   \{X\cap R_X:X\in{\cal E}\}
   =\binom{[2m]}{m-1}
   \quad\text{as a disjoint union.}
 \end{aligned}}
 \tag{2.2}
\]

The second line is a one-of-two split-repair matching. There are \(N-K\)
fixed colours from unmatched blocks and one of two candidate colours from
each of the \(K\) matched blocks. Together they must form the \(N\) required
lower colours exactly once. The first line is the additional local
noncollision condition on the edges cut from the \(U\)-rail.

This is stronger than merely asking the full \(C\)-rail to have a
positive or integrality-floor lower-colour profile. That marginal property
does not guarantee a valid one-of-two choice.

### Corollary 2.1 (directed repair matching)

A particularly clean sufficient form chooses the same side at every
matched block:

\[
 R_X=C_{i+1},\qquad J_X=C_i
 \quad\text{when }\phi(X)=U_i.
 \tag{2.3}
\]

Because \(\phi\) is injective and the \(C_i\) are distinct, the cut
endpoints \(J_X\) are then automatically distinct. Put

\[
 b_i=C_i\cap C_{i+1}.
\]

The full split-switch condition reduces to the single directed replacement
identity

\[
 \boxed{
 \{b_i:i\notin\operatorname{im}\phi\}
 \ \sqcup\
 \{X\cap C_{i+1}:\phi(X)=U_i\}
 =\binom{[2m]}{m-1}.
 }
 \tag{2.4}
\]

Thus a uniform orientation removes the endpoint-conflict part completely.
The remaining object is a Catalan-sized matching of omitted facets to
distinct host blocks whose directed colour replacements turn the base
colour word \((b_i)\) into a permutation. Reversing the saturating cycle
gives the symmetric all-left version.

## 3. Local switch

Lift the two rails to the child middle level
\(\binom{[2m]\cup\{z\}}{m+1}\):

* keep the \(U\)-rail unmarked;
* replace each \(C\)-rail vertex \(Y\) by \(z+Y\).

Suppose \(X\) is hosted in \(U_i\).

* If \(J_X=C_i\) (so \(R_X=C_{i+1}\)), replace
  \[
  U_{i-1}U_i,\quad (z+C_i)(z+X)
  \]
  by
  \[
  U_{i-1}(z+C_i),\quad (z+X)U_i.
  \tag{3.1}
  \]
* If \(J_X=C_{i+1}\) (so \(R_X=C_i\)), replace
  \[
  U_iU_{i+1},\quad (z+X)(z+C_{i+1})
  \]
  by
  \[
  U_i(z+X),\quad (z+C_{i+1})U_{i+1}.
  \tag{3.2}
  \]

All displayed cross edges are Johnson edges because the marked
\(m\)-set is contained in the incident unmarked \((m+1)\)-set.

### Theorem 3.1 (exact lower-rainbow switch theorem)

If (2.2) holds, performing all \(K\) switches produces a spanning
degree-two factor on the complete child middle level whose lower
edge-colour multiset is exactly

\[
 \binom{[2m]}m
 \ \sqcup\
 \bigl(z+\binom{[2m]}{m-1}\bigr),
 \tag{3.3}
\]

each colour once.

#### Proof

Before switching, the unmarked \(U\)-rail has the \(N\) distinct lower
colours \(C_i\), and misses precisely \({\cal E}\).

At the switch for \(X\), the removed unmarked rail edge has lower colour
\(J_X\), and the removed marked rail edge has lower colour
\(z+(X\cap J_X)\). The two new cross edges have lower colours \(J_X\)
and \(X\), respectively. Thus the switch:

1. restores the removed colour \(J_X\);
2. adds the formerly missing colour \(X\); and
3. leaves, from the matched block, only the retained marked lower colour
   \(z+(X\cap R_X)\).

Unmatched blocks retain their sole marked edge, of colour
\(z+(C_i\cap C_{i+1})\). The disjoint-union identity (2.2) therefore says
that the marked lower colours remaining after all switches are exactly
the required \(N\) colours, once each. The switches add all \(K\) missing
unmarked colours and restore every cut \(J_X\), so the unmarked lower
palette is also exact.

Pairwise distinct \(J_X\) makes the selected \(U\)-rail edges distinct;
the selected \(C\)-rail edges are distinct because every one has its own
vertex \(X\). Hence the switches are simultaneously degree preserving.
Every vertex still has degree two, proving the theorem. \(\square\)

## 4. Connectivity is a finite permutation condition

Cutting the selected \(K\) edges on either rail produces \(K\) path
fragments on each side. The cross edges (3.1)--(3.2) give a perfect
pairing of their \(4K\) endpoint occurrences.  Occurrence labels matter:
adjacent U-rail cuts give two port tokens at the same physical owner.  Let
\(P\) pair the two tokens belonging to each retained fragment and let \(M_0\)
be the cross-edge matching.  Contract every retained path fragment.
The resulting graph is a two-regular bipartite multigraph on the \(2K\)
fragments.

### Corollary 4.1

The switched factor is one Hamilton cycle if and only if the
occurrence-labelled graph \(P\cup M_0\) is one cycle, equivalently if this
contracted fragment graph is one \(2K\)-cycle.

Equivalently, decompose the contracted bipartite graph into its two perfect
matchings on the **fragment** vertices.  After fixing cyclic labels on one
shore, their product is a single-cycle permutation.  This convention is on
contracted fragments, not on the raw port involutions (which have two
orientation orbits on each alternating cycle).

This separates existence of the exact lower palette from connectivity.
If the permutation has several cycles, a later protected circuit or
colour-recycling conveyor is still required.

The existence of such a circuit is not automatic.  The fixed-fragment
extension is characterized exactly in
`MATH_THEOREM_R_CATALAN_TWO_RAIL_PORT_MATCHING_AND_C8_CONNECTIVITY_OBSTRUCTION_20260731.md`:
one needs a compatible perfect matching \(M\) for which \(P\cup M\) is one
cycle.  A valid `m=2` rainbow split-switch factor has a port graph which is
one C8, but both of its perfect matchings give two factor cycles.

## 5. Upper cut kernels, residence, and the compiler

Every unmatched marked block retains an edge of lifted union \(z+U_i\),
and every matched block retains \((z+X)(z+R_X)\), again of union
\(z+U_i\).  The removed marked edge has the same union, and the inner new
cross edge \((z+X)U_i\) also has union \(z+U_i\).  Thus the cyclic switch
preserves every marked immediate-upper target blockwise.

There is no analogous automatic statement on the unmarked side.  Every
interval which meets a marked owner contains \(z\), so a cross seam can
never restore a target which avoids \(z\).

### Lemma 5.1 (exact two-rail cut kernel)

Let \(D_U\) be the selected \(U\)-rail cuts and \(D_C\) the selected
\(C\)-rail cuts.  Assume that the switched factor is connected and open it
at a cross seam \(e_\rho\).

1. A required upper target \(Z\) avoiding \(z\) survives if and only if
   some old \(U\)-rail witness interval has edge span disjoint from the
   **whole** set \(D_U\).  Equivalently, it is witnessed wholly inside one
   retained \(U\)-fragment.
2. A required target \(z+Z\) survives if and only if either an old marked
   witness has span disjoint from \(D_C\), or one of the literal
   suffix--whole-fragments--prefix intervals in the final opened order (not
   crossing \(e_\rho\)) has union \(z+Z\).

#### Proof

Internal fragment orders do not change.  An interval avoiding \(z\) cannot
meet a marked fragment, proving the first assertion.  Every other interval
is either internal to one retained fragment or has the unique
suffix--whole-fragments--prefix form, proving the second. \(\square\)

In particular, the cap-two union profile gives no deeper-shadow theorem,
and an upper hole already present on the \(U\)-rail is fatal inside this
architecture.

### Lemma 5.2 (run interface)

In the cyclic switched factor, the maximal positive \(z\)-runs are exactly
the marked \(C\)-fragments.  Thus lower depth-\(d\) residence for \(z\) is
equivalent to every \(C\)-fragment having at least \(d+1\) vertices.  The
dual zero-run condition is the analogous lower bound on the
\(U\)-fragments.

For all coordinates, the following is a sufficient zero-loss reset
condition: every fragment has at least \(d+1\) owners; no internal positive
run has length at most \(d\); and no bounded positive run meeting the seam
inside any allowed two-fragment product has length at most \(d\).  Then any
run crossing at least two seams contains a whole fragment, so the exact
staircase loss is \(\Psi_d=0\).  Without this product condition the exact
requirement is \(\Psi_d\le\operatorname{slack}(2m+1)\), not a bound on the
number of seams.

### Theorem 5.3 (protected hosted-switch lift)

Assume (2.2), the one-cycle condition of Corollary 4.1, the all-depth cut
kernel of Lemma 5.1, and an opening \(e_\rho\) whose omitted lower colour
\(\rho\) has a literal compatible boundary/compiler port.  If the opened
chronology is chain aligned with

\[
                 \Psi_d\le\operatorname{slack}(2m+1)
\]

and its pinned lower atlas has one integral common-cap assignment, then it
satisfies P1--P4 of the global protected-packaging theorem and compiles to
a universal word of length \(B(2m+1)\).  Hence the independent lower bound
gives \(\nu(2m+1)=B(2m+1)\).

#### Proof

Connectivity and opening give P1.  Theorem 3.1 leaves exactly the opened
colour \(\rho\) missing, and its literal boundary port gives P2.  Lemma 5.1
is P3, while the displayed staircase inequality is P4.  The common-cap
compiler then realizes every remaining lower target in the same physical
letters, and the protected windows realize every upper target. \(\square\)

## 6. Relation to the broader Catalan braid

The cap-two theorem supplies the saturating rails and the
integrality-floor **upper-union** profile.  It does not supply the retained
lower-intersection identity (2.2).  For fixed \(\phi\), that identity has a
small exact formulation: first require the \(N-K\) fixed unmatched colours
to be distinct, let \(R\) be the remaining \(K\) colours, and give each
\(X\) one Boolean choosing \(R_X\).  Choices whose retained colour is not in
\(R\) are forbidden; every pair sharing a retained colour or a cut endpoint
\(J_X\) is forbidden.  These are precisely 2-CNF clauses.  Since \(K\)
distinct selected colours lie in the \(K\)-set \(R\), they cover it.

This solves only the hosted one-of-two matching for a fixed injection.  The
general two-rail braid merely requires two path forests whose marked
endpoint labels complement the unmarked internal palette; its deleted
marked edges may join two unused or two already-used facets and need not
decompose into the local hosted squares (3.1)--(3.2).  Thus Theorem 3.1 is a
useful sufficient Catalan atom, not a normalization of every feasible
two-rail braid.

The remaining hosted-switch tasks are to choose \(\phi\) so the 2-SAT
instance is satisfiable, make the fragment permutation connected, satisfy
the all-depth cut kernel and residence product, install the boundary port,
and pass one common-cap compiler.  Consequently this note is an exact
restricted reduction, not a proof that \(\nu(k)=B(k)\).
