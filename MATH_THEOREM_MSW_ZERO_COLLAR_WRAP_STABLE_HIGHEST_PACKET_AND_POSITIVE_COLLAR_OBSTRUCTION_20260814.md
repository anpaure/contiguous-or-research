# Highest-valley MSW connectivity is zero-collar wrap-stable, while a positive full profile collar is not uniform

**Date:** 2026-08-14  
**Status:** unconditional symbolic wrap-stability theorem for the
highest-valley packet choice, plus exact H100 obstructions to the obvious
positive full-profile collar.

## 0. Outcome

Fix \(d\ge1\) and \(m\ge3d+1\). The four-packet residue proof can be made
deterministic so that its selected area-increasing same-forced edge survives
every primitive wrapping

\[
 u\longmapsto 1u0.
\]

No extra depth profile is needed: the minimal collar depth is \(t=0\).

The obvious positive collar is too strong uniformly. Requiring, at the same
cuts, the complete depth-\(d\) forced profile and one full depth-\(d+1\)
profile destroys highest-packet coverage already at \((m,d)=(7,2)\), and the
resulting graph has 270 components. Requiring profiles through depth
\(d+2\) leaves no transposition edge at \((7,2)\) or \((10,3)\).

Thus the recursive state should remember the zero-collar packet/residue type
and allow cut reselection after wrapping. It should not demand a transported
positive full profile at the same cut.

## 1. Deterministic zero-collar packet

At a chosen highest valley, use the notation \((L,Q,O)\) of the four-packet
theorem, so

\[
 L+Q+O=m-2.
\]

Choose a packet by the following fixed rule:

1. if \(L=Q=0\), choose `01`;
2. if \(L>0,Q=0\), choose `001`;
3. if \(L=0,Q>0\), choose `011`;
4. if \(L,Q>0\) and \((L,Q,O)\ne(d,d,d-1)\), choose `0011`;
5. at \((L,Q,O)=(d,d,d-1)\), choose the exceptional crossed `001`
   witness.

Choose, for instance, the leftmost highest valley when several exist.

### Theorem 1.1 (primitive-wrap stability)

The selected packet has a common depth-\(d\) forced history and strictly
increases area. After every \(h\ge0\) primitive wrappings, the corresponding
wrapped pair still has a common depth-\(d\) forced history and strictly
increases area.

#### Proof

The context-transport lemma for the packet keeps \(L,Q\) fixed and adds the
outer primitive pair to the exterior context. After \(h\) wrappings the local
triple is therefore

\[
 (L,Q,O+h).
\]

The four sufficient residue inequalities are monotone in \(O\):

\[
\begin{array}{c|c}
\text{case}&\text{sufficient inequality}\\ \hline
L=Q=0&O\ge2d\\
L>0,Q=0&L+O\ge2d\\
L=0,Q>0&Q+O\ge2d\\
L,Q>0&L+Q+O\ge3d-1.
\end{array}
\]

Thus a direct packet witness remains available after increasing \(O\), except
that the selected edge at \((d,d,d-1)\) is the crossed `001` edge rather than
the `0011` edge. That same `001` edge also persists. For \(L=Q=d\) and every
\(O\ge d-1\), let \(q_r\) be the old tight position occupying new tight
position \(r\) for the `001` packet. Substitution in the canonical
permutation gives

\[
 q_j=d+1+j,
 \qquad
 q_{3d+O+3+j}=2d+O+3+j
 \qquad(0\le j<d).
\]

Here \(n=4d+2O+5\), \(s-1=d+O+2\), and the cuts

\[
 (a,b)=(d+1,3d+O+3)
\]

are crossed: \(b+s-1\equiv0\pmod n\), while
\(a+s-1=2d+O+3\). The two displayed identities are exactly

\[
 q_{b+j}=a+s-1+j,
 \qquad
 q_{b+s-1+j}=a+j.
\]

At \(O=d-1\) this specializes to the previously proved cut
\((d+1,4d+2)\); increasing \(O\) translates only the second cut. Hence the
same selected `001` parent edge survives every wrapping.

Every packet moves a zero rightward across a one, hence strictly increases
area before and after wrapping. \(\square\)

### Corollary 1.2

For every \(m\ge3d+1\), the zero-collar same-forced graph has a monotone
arborescence whose selected edge descendants remain same-forced under every
number of common primitive wrappings.

This is an edge-existence and connectivity theorem. It does not yet transport
one fixed cut, one common-history word, or a simultaneous separated-port
assignment.

## 2. Same-cut transport is stronger and false

The theorem deliberately permits cut reselection after wrapping. Even when
an edge remains in the same-forced graph, the old cut transported through the
tight-order embedding need not remain a witness.

At \((10,3)\), the complete equality-only transposition graph has 221,021
edges. Of these, 220,895 have some equality witness after one wrapping, but
only 123,516 have a witness whose old cut maps directly to a wrapped witness.
Hence graph edge survival is not a port-state transition rule.

For the one-collar containment graph at \((10,3)\), all 91,083 edges survive
wrapping after cut reselection, while only 47,245 transport the same cut. For
the equality one-collar graph the corresponding counts are 67,709 and 27,885.

## 3. Positive full-profile collars

For an oriented row \(w\), cut \(a\), and depth \(q\), write

\[
 \Phi_q(w,a)=\bigl((F^{(q)}_j(w,a),P^{(q)}_j(w,a))\bigr)_{0\le j<q}.
\]

Two natural \(t=1\) collar graphs were audited:

- equality of the complete forced profile at depth \(d\), followed by full
  common-history compatibility at depth \(d+1\); and
- equality of the complete forced profiles at both depths \(d,d+1\).

The finite census is:

| \((m,d)\) | collar | edges | components | edges surviving one wrap after cut reselection |
|---:|---|---:|---:|---:|
| \((7,2)\) | \(t=0\) forced equality | 3,172 | 1 | 3,172 |
| \((7,2)\) | \(t=1\) final containment | 191 | 270 | 191 |
| \((7,2)\) | \(t=1\) equality | 191 | 270 | 191 |
| \((10,3)\) | \(t=0\) forced equality | 221,021 | 1 | 220,895 |
| \((10,3)\) | \(t=1\) final containment | 91,083 | 1 | 91,083 |
| \((10,3)\) | \(t=1\) equality | 67,709 | 1 | 67,709 |

At \((7,2)\) and \((10,3)\), requiring the next complete profile as well
(\(t=2\)) gives zero transposition edges in both the containment and equality
versions.

The source-level highest-valley packet coverage is even sharper:

| \((m,d)\) | zero-collar uncovered roots | \(t=1\) containment uncovered roots | \(t=1\) equality uncovered roots |
|---:|---:|---:|---:|
| \((7,2)\) | 0 | 428 | 428 |
| \((10,3)\) | 0 | 69 | not needed for the obstruction |
| \((13,4)\) | 0 | 217 | 2,628 |

Consequently no positive full-profile collar of this obvious form gives a
uniform highest-packet recursion from the first threshold onward. The least
uniform collar is the zero-collar state of Theorem 1.1.

## 4. Repeated-wrap audit

The H100 chain verifier reselected cuts after every wrap. It found:

```text
(7,2), t=0 equality: 3172 edges survive h=0,1,2,3,4,5;
(7,2), t=1 containment/equality: all 191 edges survive h=0,...,5;
(10,3), t=0 equality: 221021 at h=0, then 220895 through h=1,2,3;
(10,3), t=1 containment: 91083 through h=0,1,2,3;
(10,3), t=1 equality: 67709 through h=0,1,2,3.
```

The targeted highest-packet verifier found a wrap-stable zero-collar parent
for every nonmountain root at \((7,2),(10,3),(13,4)\), through respectively
three, two, and two explicit wraps. These finite checks support, but are not
needed for, the symbolic monotonicity proof.

## 5. Exact remaining recursive gate

Theorem 1.1 supplies a context-stable **edge family**, not a recursively
packable port assignment. A completed induction still must choose cuts and
literal history classes so that:

1. inherited internal ports remain separated after the circumference grows;
2. cut reselection is consistent at both endpoints of every selected edge;
3. same-start coalescence classes pass the transitive multiway
   union-forced/intersection-maximal test; and
4. only bounded boundary state is needed at cross-branch seams.

The positive-collar obstruction shows that simply freezing the next complete
depth profile is not this state.

## 6. Reproducibility

All compilation, enumeration, execution, and hashing use SSH on H100. The
verifiers are:

- `scratch/audit_msw_one_collar_graph_and_wrapping_20260814.cpp`;
- `scratch/audit_msw_collar_chain_wrapping_20260814.cpp`; and
- `scratch/audit_msw_highest_packet_collar_wrapping_20260814.cpp`.

No signed lattice identity is interpreted as a positive decomposition.
