# Identical common-history incidences coalesce before the separated-port test

**Date:** 2026-08-14  
**Status:** unconditional extension of the separated multi-port Euler
theorem.  It permits arbitrarily many component-graph incidences to reuse
one literal history occurrence on a source circuit.  The occurrence-level
successor-swap argument was independently audited on 2026-08-14.

## 1. Setup

Let (G=(V,E)) be connected.  For each (v\in V), let (T^v) be a
cyclic simple resident Johnson trace of length (L_v\ge d+1), with one
fixed global traversal orientation.  Write (P^v_j) and (F^v_j) for
its maximal and forced depth-(d) antecedent letters.

For every incidence ((v,e)), choose a cyclic start (b_{v,e}) and a
literal length-(d) word

[
H^{v,e}=(H^{v,e}_0,\ldots,H^{v,e}_{d-1})
]

satisfying

[
F^v_{b_{v,e}+j}\subseteq H^{v,e}_j
\subseteq P^v_{b_{v,e}+j}\qquad(0\le j<d).
]

For (e=uv), require literal equality

[
H^{u,e}=H^{v,e}.
]

At one component (v), declare two incidences equivalent when both their
starts and their literal history words agree:

[
e\sim_v f
\quad\Longleftrightarrow\quad
b_{v,e}=b_{v,f}\ \,\text{and}\ \,H^{v,e}=H^{v,f}.
]

Assume the length-(d) port blocks belonging to distinct equivalence
classes are pairwise disjoint and separated cyclically by at least one
unaltered source position.  No bound is placed on the number of incidences
inside one class.

## 2. Coalesced-port theorem

### Theorem 2.1

Under the setup above, all component source circuits serialize into one
cyclic source word, with zero added positions, preserving the complete
occurrence-labelled literal subword deck through width (d+1).

In particular, the complete owner ledger and every strict-lower compiler
cell supported on a source word of width at most (d) transport exactly.

### Proof

On one component, replace the maximal antecedent word once for every
equivalence class.  Repeated incidences in that class request the same
replacement on the same positions, so they introduce no additional
alteration.  The distinct altered blocks are separated.  The simultaneous
multi-block freedom theorem therefore proves that the resulting word is
still an antecedent of precisely (T^v).

View every resulting component word as an occurrence-labelled closed walk
in the order-(d) de Bruijn multigraph.  For every edge (e=uv), literal
history equality says the two walks share the vertex (H^e).  Several
edges may identify the same history vertex and may even reuse the same
incoming occurrence on the accumulated component; this does not identify
or delete a de Bruijn edge occurrence.  The union of the component walks
is balanced and weakly connected because (G) is connected.  Hence it
has an Euler circuit.

Equivalently, process a spanning tree of (G).  At an edge joining a new
child cycle to the accumulated cycle at (H^e), swap their successors
after incoming occurrence edges ending at (H^e).  The swap merges two
permutation cycles.  If a later edge reuses the same incoming occurrence,
that occurrence now lies in the accumulated cycle.  Swap its **current**
successor with the successor of an incoming occurrence in the genuinely
new child cycle.  The first successor need not be the occurrence that
followed it in the original component.  Both successors still leave the
same history vertex, so this is a legal de Bruijn successor permutation
and again merges two distinct permutation cycles.  Thus reuse is legal.

Algebraically, if \(p\) is the reused incoming occurrence and
\(q_1,\ldots,q_t\) are incoming occurrences from successive child cycles,
the swaps

\[
 (p,q_1),\ (p,q_2),\ \ldots,\ (p,q_t)
\]

are ordinary transpositions of successor values.  After the \(i\)-th
swap, \(p\) remains one labelled occurrence with one successor; the
displaced successor is transferred to \(q_i\).  No edge occurrence is
copied, identified, or deleted.

Every labelled order-(d) de Bruijn edge retains its literal
((d+1))-letter context.  An Euler circuit uses every such labelled edge
once, preserving the width-(d+1) deck; shorter words are its literal
suffixes.  This proves the theorem.  (square)

## 3. Exact MSW incidence formulation

For a tight MSW row (w), define its forced-history signature at start
(a) by

[
\Sigma_w(a)=
\bigl(F_0(w,a),F_1(w,a),\ldots,F_{d-1}(w,a)\bigr).
]

An incidence option on an edge (uv) is a pair of oriented starts
((a,b)) satisfying

[
\Sigma_u(a)=\Sigma_v(b).
]

At a fixed oriented row, all incidences using the same start automatically
have the same signature and hence form one coalesced class.  Therefore the
exact proof-safe global gate is:

1. choose one parent incidence option for every nonroot MSW component;
2. choose one global orientation for every component; and
3. require only the **distinct used starts** at a component to have cyclic
   distance at least (d+1).

This is weaker than demanding every incidence use a different separated
port, but it is not a relaxation of the source equations: it is precisely
the idempotence of making the same literal antecedent replacement twice.

## 4. Scope

The theorem says nothing about existence of such a coalesced incidence
assignment in an infinite MSW family.  It also transports no source
interval longer than (d+1), no proper-upper current, and no final opening
cap.  Those remain separate gates.
