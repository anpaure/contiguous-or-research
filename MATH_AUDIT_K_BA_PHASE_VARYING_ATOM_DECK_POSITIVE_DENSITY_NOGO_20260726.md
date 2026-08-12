# Audit of the phase-varying \(BA\) atom-deck no-go

Date: 2026-07-26

Audited file:
MATH_THEOREM_K_BA_PHASE_VARYING_ATOM_DECK_POSITIVE_DENSITY_NOGO_20260726.md.

Method: direct permutation, incidence, and prefix-footprint verification.
No computation, finite search, solver, web input, or external source is
used.

## 0. Final verdict

**PASS after correction.**

The main theorem file now incorporates all four substantive corrections
found in the first audit:

1. it imposes the standing hypothesis \(m\ge 3\);
2. it uses the correct pullback support
   \(\sigma^t\{1,n,p_t\}\) for
   \(D_t=C^{-t}T_{p_t}C^t\);
3. it states that (4.11) rules out partner degree at most seven, not all
   bounded partner degree;
4. its final implication (6.1) explicitly assumes an
   owner-transversal, owner-capacity-one embedding.

The proof of Lemma 3.2 now also treats the one-old/two-new support case.
The connector statement has been scoped as a sharp endpoint-divergence
lower bound rather than a physical sufficiency theorem. No remaining
theorem-level correction was found.

The following formulas pass exactly:

\[
 \Delta(O)=n\mathbf 1_{Z(O)}-m\mathbf 1,
 \qquad
 \sum_O\mathbf 1_{Z(O)}=\frac{mu}{n}\mathbf 1,
 \qquad n\mid u,
\]

\[
 c\ge \rho(n-\rho),
\]

\[
 |\mathcal D(O)\cap\mathcal D(P)|
 \le (r+2-d(O,P))_+(r+3-d(O,P))_+,
\]

and

\[
 M_1^-\ge
 \left(\frac{A_{\rm BA}}2-\frac{2W}{m+2}\right)_+.
\]

## 1. Directed-cut and orbit-design audit

The pullback permutation of \(C=BA\) has cycles

\[
 P=(1,3,\ldots,2m-1),\qquad
 Q=(2,4,\ldots,2m,n)
\]

of coprime lengths \(m\) and \(m+1\). Hence every permutation state has
orbit length

\[
 L=m(m+1).
\]

For a full orbit \(O\), let \(Z(O)\) be the labels on \(P\). The two
phase coordinates range independently by the Chinese remainder theorem.
Thus the endpoint deck is exactly

\[
 \{a\to b:a\in Z(O),\ b\in Z(O)^c\},
\]

with every arc once. Each \(a\in Z(O)\) has outdegree \(m+1\), and each
\(b\notin Z(O)\) has indegree \(m\). Therefore

\[
 \Delta(O)
 =(m+1)\mathbf 1_{Z(O)}-m\mathbf 1_{Z(O)^c}
 =n\mathbf 1_{Z(O)}-m\mathbf 1.
\]

Every canonical atom contributes a directed 3-cycle and has zero
endpoint divergence. For a packet of \(u\) full orbits,

\[
 n\sum_O\mathbf 1_{Z(O)}=mu\mathbf 1.
\]

Since \(\gcd(m,n)=1\), integrality gives \(n\mid u\). The same argument
works in each incidence component because such a component is closed
under whole \(C\)-orbits and whole atom triples. At \(u=n\), every label
has replication \(m\), exactly as claimed.

## 2. Connector residue

Put

\[
 k_x=\#\{O:x\in Z(O)\},
 \qquad
 d_x=nk_x-mu.
\]

If

\[
 mu=nq+\rho,\qquad 0\le \rho<n,
\]

then

\[
 d_x\equiv-\rho\pmod n,
 \qquad
 \sum_xd_x=0.
\]

Writing \(d_x=na_x-\rho\) yields \(\sum_xa_x=\rho\). Integer convexity
minimizes the \(\ell^1\)-norm when \(\rho\) of the \(a_x\)'s equal \(1\)
and the remaining \(n-\rho\) equal \(0\). Consequently

\[
 \sum_x|d_x|\ge 2\rho(n-\rho).
\]

Every exceptional endpoint arc has \(\ell^1\)-norm two, so

\[
 c\ge \rho(n-\rho).
\]

This is the sharp divergence-residue bound. It does not imply that the
remaining zero-divergence arcs admit a marked directed-triangle factor;
the corrected theorem does not claim such sufficiency.

## 3. Positional atoms and the common-gauge obstruction

For \(2\le p\le m\), the positions \(1,n,p\) lie outside

\[
 J=\{m+2,\ldots,2m\},
\]

while \(m+1\) is fixed. If

\[
 a=x_1,\qquad b=x_n,\qquad c=x_p,
\]

then the endpoint pairs of \(x,T_px,T_p^2x\) are

\[
 (a,b),\qquad(b,c),\qquad(c,a).
\]

Their ordered suffixes agree, and the fixed label at \(m+1\) is distinct
from \(a,b,c\). Hence all three last-middle exclusions hold. Thus
\(T_p=(1\ n\ p)\) partitions all permutation states into literal
canonical atoms.

Lemma 3.2 is now complete. If a new supported triple adds one vertex,
the usual two-old/one-new argument adjoins it to \(A(U)\). If it adds two
vertices \(x,y\), conjugation supplies

\[
 (a\ x\ y),\qquad(b\ x\ y),
\]

and their product with one inverse gives a 3-cycle on
\(\{a,b,x\}\). These cycles first generate \(A(U\cup\{x\})\), after
which the original cycle adjoins \(y\). Induction along a support
spanning tree proves that connected 3-cycle supports generate \(A(V)\).

For the conjugation sign, let

\[
 (Cx)_j=x_{\sigma(j)}.
\]

Because state-operator composition reverses pullback composition,

\[
 D_t=C^{-t}T_{p_t}C^t
\]

has pullback

\[
 \sigma^t(1\ n\ p_t)\sigma^{-t}
\]

and support

\[
 \sigma^t\{1,n,p_t\}.
\]

The first two support points range through all of \(P\times Q\) by CRT,
so the support hypergraph is connected and the generated group is
\(A_n\). A nonempty invariant representative set would contain an
entire parity class of \(n!/2\) states. Since \(C\) is odd, each
\(C\)-orbit meets that class in \(L/2>1\) states, contradicting one
representative per orbit.

For fixed \(T_2\), adjoining the odd permutation \(C\) gives \(S_n\).
Hence a set invariant under both maps is empty or the full \(n!\)-state
space. A fixed middle owner occurs in

\[
 m!(m+1)!
\]

source states, and the \(A\)-successor catalogue is another full copy.
The exact combined load is therefore

\[
 2m!(m+1)!.
\]

## 4. Suffix fibres and partner capacity

Under the corrected standing hypothesis \(m\ge3\), \(J\) meets both
position cycles. Equality of an ordered suffix word at two phases of one
orbit fixes the phase modulo \(m\) and modulo \(m+1\), hence modulo \(L\).
Thus each suffix fibre contains at most one state from each orbit.

A canonical atom is exactly a triple of arcs with common suffix \(K\),

\[
 a\to b,\qquad b\to c,\qquad c\to a,
\]

with

\[
 \rho(a,b)\ne c,\qquad
 \rho(b,c)\ne a,\qquad
 \rho(c,a)\ne b.
\]

Encoding the next arc by \(\beta_K\) gives precisely

\[
 h(e)=t(\beta_Ke),\qquad
 \beta_K^3e=e,
\]

with every \(\beta_K\)-cycle of length three and the displayed marked
exclusion. Conversely, every such cycle reconstructs a legal atom.
Therefore local allowed head-to-tail Hall matchings give only a directed
cycle cover; the order-three condition is genuinely additional.

For the partner estimate, let \(m=2r+1\) and

\[
 d=d(O,P)=|Z(O)\setminus Z(P)|.
\]

If \(O\) and \(P\) occur together in an atom, then \(d\ge1\). A common
suffix contains a length-\(r\) cyclic window on the \(m=2r+1\) cycle
avoiding \(d\) forbidden labels, and a length-\(r\) window on the
\(m+1=2r+2\) cycle avoiding the opposite \(d\) labels. The respective
numbers of possible starts are at most

\[
 (r+2-d)_+,\qquad(r+3-d)_+.
\]

CRT multiplies the bounds. One common suffix supports at most one atom
containing a fixed orbit pair. Since each of the \(L\) states of \(O\)
belongs to an atom with two other orbits,

\[
 \sum_{P\ne O}c_{OP}=2L.
\]

It follows that every orbit has at least

\[
 \left\lceil\frac{2L}{(r+1)(r+2)}\right\rceil
 =
 \left\lceil\frac{4(2r+1)}{r+2}\right\rceil
\]

partners. This is at least eight for \(m\ge23\) and tends to eight. The
corrected report therefore states only that partner degree at most seven
is impossible; it does not claim to exclude all bounded partner degree.

## 5. First-shadow obstruction

For even \(m\), the successor owner footprint is the
\(C^{m+1}\)-translate of the source footprint. Every full orbit has
identical source and successor owner multisets, so its owner-incidence
vector is coordinatewise even. No nonempty strict-alternating component
can occur in an owner-capacity-one factor.

For odd \(m=2r+1\), the two lower rank-\((m-1)\) footprints meet both
position cycles in \(r\) positions. They differ by one phase on the
\(m\)-cycle and agree on the \(m+1\)-cycle. Their length-\(L\) target
orbits therefore coincide, and each has support \(L\). Thus the \(2L\)
occurrences in one alternating component support exactly \(L\) targets,
each twice.

In an owner-transversal hybrid, the \(A_{\rm BA}\) alternating
occurrences support at most \(A_{\rm BA}/2\) targets. The remaining
\(W-A_{\rm BA}\) owner occurrences support at most that many further
targets. Total support is at most

\[
 W-\frac{A_{\rm BA}}2.
\]

The target layer has size

\[
 \binom{2m+1}{m-1}
 =\frac{m}{m+2}W
 =W-\frac{2W}{m+2}.
\]

Subtraction gives

\[
 M_1^-\ge
 \left(\frac{A_{\rm BA}}2-\frac{2W}{m+2}\right)_+.
\]

For \(A_{\rm BA}\ge\alpha W\), this is
\((\alpha/2-o(1))W\). At \(A_{\rm BA}=W\), it becomes

\[
 M_1^-\ge\frac{m-2}{2(m+2)}W.
\]

## 6. Final implication and re-audit note

The corrected implication is:

\[
 \boxed{
 \begin{gathered}
 S=BA(S),\\
 S\text{ is the source set of the \(BA\) components inside an
 owner-transversal rotor factor},\\
 M_1^-=o(W)
 \end{gathered}
 \quad\Longrightarrow\quad
 |S|=o(W).}
\]

Indeed \(A_{\rm BA}=2|S|\). For odd \(m\), the hybrid bound gives

\[
 |S|\le M_1^-+\frac{2W}{m+2}=o(W),
\]

while for even \(m\) owner capacity forces \(S=\varnothing\).

The ownership hypothesis is essential: without it, the full permutation
state set is \(C\)-invariant, has complete first-shadow support, and is an
explicit counterexample to the bare implication.

Final re-audit of the patched main theorem confirms:

* the standing \(m\ge3\) hypothesis appears before all later uses;
* (3.8) uses the correct \(\sigma^t\) pullback support;
* Lemma 3.2 contains the missing two-new-vertex induction;
* the partner conclusion is restricted to degree at most seven;
* (6.1) includes owner transversality and explicitly notes the full-state
  counterexample without it.

Accordingly, the corrected main theorem and its quantitative
architecture-specific no-go pass.
