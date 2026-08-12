# The \(K=11\) two-token connector automaton

Date: 2026-07-25

Scope: exact \(c=6,d=0\) quotient, pure mathematics only.

## 0. Outcome

The phi-repair choice and the two adjacent lower-shadow choices admit one
exact local cache description.

Fix a central K connector source

\[
 Q=\phi(C),\qquad
 \Omega\setminus Q=C\sqcup\{x,y\}.
\]

Choose distinct quotient ports \(c,d\in C\). The connector joins

\[
 D_c=(C\setminus\{c\})\cup\{x,y\},
 \qquad
 D_d=(C\setminus\{d\})\cup\{x,y\},
\]

and has upper shadow

\[
 Y=(C\setminus\{c,d\})\cup\{x,y\}.                              \tag{0.1}
\]

If the source color immediately before \(Q\) is

\[
 R^-=(Q\setminus\{p\})\cup\{c\}
\]

and the source color immediately after \(Q\) is

\[
 R^+=(Q\setminus\{q\})\cup\{d\},
\]

then the adjacent lower shadows are

\[
 B^-=Q\setminus\{p\},
 \qquad
 B^+=Q\setminus\{q\}.                                          \tag{0.2}
\]

Thus a connector is the five-set braid

\[
 \boxed{
 R^-\,--\,D_c\,--\,Q\,--\,D_d\,--\,R^+.
 }                                                               \tag{0.3}
\]

At the moment the path reaches cache \(Q\), the most recent insertion is
\(p\), and the preceding insertion is another element \(u\in Q\setminus
\{p\}\). The two-token physical rule says exactly

\[
 q\notin\{p,u\}.                                                \tag{0.4}
\]

Hence three of the five cache symbols are locally removable. Independently,
three of the four reservoir symbols in \(C\) remain available for the
outgoing upper port \(d\ne c\).

For every fixed \(d\), exactly two of the five exchange sources

\[
 (Q\setminus\{q\})\cup\{d\},\qquad q\in Q,
\]

are in \(\mathcal H\), and three are in \(\mathcal K\). Since only two
cache symbols are protected, at least one of the three eligible removals
always produces a K continuation.

Therefore:

> **Every incoming two-token state has a simultaneous upper repair,
> two distinct adjacent lower facets, and a physical K continuation at
> every chosen free outgoing port.**

This proves that no purely local Hall or parity obstruction survives the
separate upper and lower matching theorems. The remaining obstruction is
global: fixed H-segment ports may prescribe a protected removal, and all
connectors must be ordered into two acyclic paths while carrying the
two-token memory.

## 1. Derivation of the local braid

Let

\[
 L=C\sqcup\{x,y\}.
\]

The K4 class of source \(Q\) consists of

\[
 D_e=L\setminus\{e\},\qquad e\in C.
\]

Choosing ports \(c,d\) gives

\[
 D_c\cap D_d=L\setminus\{c,d\},
\]

which is (0.1).

The complement of \(D_c\) is

\[
 \Omega\setminus D_c=Q\sqcup\{c\}.
\]

Every source color adjacent through port \(D_c\) is a five-subset of this
six-set. Besides \(Q\), it has the form

\[
 R_p=(Q\setminus\{p\})\cup\{c\},
 \qquad p\in Q.
\]

Its intersection with \(Q\) is \(Q\setminus\{p\}\), proving the left part
of (0.2). The right part is identical.

Conversely, all five sets in (0.3) have the required disjointness:

\[
 R^-\cap D_c=\varnothing,\qquad
 Q\cap D_c=Q\cap D_d=\varnothing,\qquad
 R^+\cap D_d=\varnothing.
\]

Thus the data \(c,d,p,q\) determine one unique local braid.

## 2. The two-token state

Write a source-path transition in the standard form

\[
 S_{i+1}=S_i-b_i+a_i.
\]

The physical inequalities are

\[
 a_i\ne b_{i+1},
 \qquad
 a_i\ne b_{i+2}.                                                \tag{2.1}
\]

Equivalently, before choosing the next deletion \(b_i\), one must avoid
the two most recent inserted symbols:

\[
 b_i\notin\{a_{i-1},a_{i-2}\}.                                 \tag{2.2}
\]

Those symbols really belong to the current cache. The first has just been
inserted; the second was not removed at the intervening step by (2.1).

For the incoming transition

\[
 R^-=(Q\setminus\{p\})\cup\{c\}
 \longrightarrow Q,
\]

the removed symbol is \(c\) and the inserted symbol is \(p\). Let \(u\)
be the preceding insertion. At cache \(Q\), the protected ordered pair is

\[
 (p,u),\qquad p,u\in Q,\quad p\ne u.                            \tag{2.3}
\]

The outgoing transition

\[
 Q\longrightarrow
 R^+=(Q\setminus\{q\})\cup\{d\}
\]

removes \(q\) and inserts \(d\). Rule (2.2) becomes exactly (0.4).
Afterward the protected pair updates to

\[
 (d,p).                                                         \tag{2.4}
\]

The complete automaton update is therefore

\[
 \boxed{
 (Q;p,u)
 \xrightarrow[\text{port }d]{\text{remove }q,\ \text{insert }d}
 ((Q-q)+d;\ d,p),
 \quad q\in Q\setminus\{p,u\}.
 }                                                               \tag{2.5}
\]

This is the promised cache/recent-symbol form.

## 3. Simultaneous local realization

### Theorem 3.1

Fix an incoming physical state

\[
 (Q;p,u;c),
\]

where \(Q=\phi(C)\), \(p,u\in Q\) are distinct protected symbols, and
\(c\in C\) is the incoming quotient port. Fix any free outgoing port

\[
 d\in C\setminus\{c\}.
\]

Then there exists

\[
 q\in Q\setminus\{p,u\}
\]

such that

\[
 R^+=(Q\setminus\{q\})\cup\{d\}\in\mathcal K.
\]

For that choice:

1. the connector upper shadow is (0.1);
2. its adjacent lower shadows are (0.2);
3. \(B^-\ne B^+\);
4. both physical constraints visible at the current cache hold;
5. the next source is again a K color.

#### Proof

Because \(D_d\in\mathcal K\), among the six five-subsets of
\(\Omega\setminus D_d=Q\sqcup\{d\}\), exactly two are in \(\mathcal H\)
and four are in \(\mathcal K\). One K facet is \(Q\) itself. Thus among
the five candidates \(R_q\), exactly two are H and three are K.

The protected set \(\{p,u\}\) removes only two candidates. The three
eligible values of \(q\) therefore cannot all be H; at least one gives a K
source. For every eligible \(q\), \(q\ne p\), so (0.2) gives
\(B^-\ne B^+\). Equation (0.4) is precisely the two-token physical rule.
All other assertions follow from Section 1. \(\square\)

There are in fact at least

\[
 3\cdot3=9
\]

raw pairs \((d,q)\) before imposing the H/K type at the outgoing source,
and Theorem 3.1 leaves at least one K choice for each of the three outgoing
ports.

## 4. Fixed H ports

The theorem deliberately concerns a free K continuation. If \(D_d\) is
the endpoint of a prescribed H-star segment, then its other source color
is fixed. Equivalently, \(q\) is fixed to one of the two H values in the
five-candidate list.

Such a port is locally physical exactly when

\[
 q\notin\{p,u\}.                                                \tag{4.1}
\]

There is no counting guarantee for (4.1): a prescribed H value may be one
of the protected symbols. Reversing the orientation of the connector
exchanges the incoming and outgoing tests but does not remove the global
memory.

Thus all local failures are concentrated at fixed H ports. Singleton
continuations are never locally dead.

## 5. What remains global

The local choices separate into two disjoint coordinate reservoirs:

* \(c,d\in C\) determine the quotient endpoints and upper repair;
* \(p,q\in Q\) determine the adjacent lower facets;
* the only local coupling is the two-token exclusion \(q\notin\{p,u\}\)
  and the H/K type of \(R_q\).

Therefore neither the 74-upper-repair matching nor the 252-lower-facet SDR
loses feasibility at an isolated free connector.

What remains is one global automaton problem:

> orient and order the 202 connectors into two paths so that every fixed
> H-segment port sees an unprotected prescribed deletion, while each
> connector color and quotient port is used once and the selected upper
> and lower supports remain large.

The unresolved constraints are precisely:

1. pairing two compatible ports by the same connector \(Q\);
2. degree two and acyclicity on the 204 contracted nodes;
3. the protected-pair update (2.5) around the whole two-path forest;
4. simultaneous realization of the chosen 74 upper repairs and 252 lower
   facet representatives.

There is no additional local parity or cache-capacity obstruction.
