# Regular incidence factors and private literal port routers

**Date:** 2026-08-03  
**Status:** exact conditional flow theorem, followed by an audit of the
current all-\(k\) premise. No finite computation is used.

## 0. Conclusion

The proposed factor-plus-router argument is correct after its privacy,
state, and terminal hypotheses are stated literally.

After fixing one compensation linkage, a left \(h\)-regular incidence
factor \(B=(G,P;E)\), with right degrees at most \(h\), links every gain
claim provided that:

1. every incidence \(gp\) has a private occurrence-labelled directed prefix
   from claim \(g\) to port \(p\);
2. all ports simultaneously have pairwise vertex-disjoint suffixes to
   distinct unused sinks;
3. prefixes, suffixes, and the fixed compensation linkage are mutually
   private in the precise sense below; and
4. they coexist under one fixed cap/guard/occurrence state and preserve
   terminal type.

The proof sends \(1/h\) units along every incidence prefix and its port
suffix. Every claim emits one unit, and every port/suffix carries at most
\(\deg_B(p)/h\le1\). Integral max flow then links every gain.

At \(h=2\), the small protected-factor theorem for \(ML_m\) supplies the
**abstract incidence factor** \(B\) for any 2-bounded protected bank of at
most \(m-2\) edges. It does not supply either the literal prefix lift or the
private suffix router.

The parent/reference matching in the current all-\(k\) construction does
**not presently supply the literal port router as a proved consequence**.
A matching alone cannot imply it. One clean sufficient certificate is the
full residual active-port rank

\[
 r_{\Gamma_{\mathrm{suf}}^{\mathrm{type}}}(P)=|P|
\tag{0.1}
\]

in the same materialized state, after deleting the fixed compensation
linkage and every prefix interior. This certificate, or an alternative
capacity-faithful router certificate, must remain explicit.

## 1. Residual occurrence network

Fix one fully materialized cap, guard, common-state, and occurrence state
\(c\). Let \({\cal D}^c\) be a finite directed network whose physical
unit-capacity vertices have been node-split.

Fix one compensation linkage \(L_I\). Delete every physical capacity and
sink slot used by \(L_I\), obtaining the residual network

\[
 {\cal D}'={\cal D}^c-\operatorname{cap}(L_I),
 \qquad
 T'=T^c-T(L_I).
\tag{1.1}
\]

This theorem is a fixed-linkage theorem. It does not claim the stronger
matroid-contraction conclusion in which the compensation linkage may
reroute after the gain set changes.

Let \(G\) be a set of gain claims. Every \(g\in G\) has a distinct claim
start \(s_g\), and the arc from a global super-source to \(s_g\) has capacity
one. Let \(P\) be a set of physical occurrence-labelled ports.

A physical port retains a gain-independent record such as

\[
 (p,c,\text{phase},\text{physical row/cell},
   \text{capacity identity},\text{terminal type}).
\tag{1.2}
\]

The incidence \(gp\) separately retains

\[
 (g,p,c,\text{phase},\text{ray},\text{role},\text{flags},
   \text{endpoint},\text{guard footprint},\text{prefix identity}).
\tag{1.3}
\]

Equal values at different physical addresses remain different ports.
Aliases of one physical cell share one capacity vertex. Gain-specific port
copies are legal only when all copies pass through that one shared
capacity-one gate.

## 2. The private factor-router hypotheses

Let \(h\) be a positive integer, and let

\[
 B=(G,P;E)
\tag{2.1}
\]

be a bipartite incidence graph. Replace its right shore by its active
support, so throughout

\[
 P=N_B(G).
\tag{2.2}
\]

Assume

\[
 \deg_B(g)=h\quad(g\in G),
 \qquad
 \deg_B(p)\le h\quad(p\in P).
\tag{2.3}
\]

For every incidence \(e=gp\in E\), fix a directed literal prefix

\[
 Q_e:s_g\leadsto p
\tag{2.4}
\]

in \({\cal D}'\). For every \(p\in P\), fix a directed suffix

\[
 R_p:p\leadsto t_p,
\qquad t_p\in T'.
\tag{2.5}
\]

The family is a **private literal factor-router** when:

1. the sinks \(t_p\) are pairwise distinct;
2. the suffixes \(R_p\) are pairwise vertex-disjoint;
3. two different prefixes share no physical capacity except that the
   \(h\) prefixes belonging to one claim may share their start \(s_g\), and
   the \(\deg_B(p)\) prefixes ending at one port may share that endpoint
   \(p\);
4. a prefix has no vertex on any suffix except its own terminal port;
5. no prefix or suffix uses a capacity or sink deleted in (1.1);
6. every prefix and suffix is present in the same fixed state \(c\);
   candidate-created ports cannot appear before their activating candidate
   is included in that state; and
7. for every \(gp\in E\), \(t_p\) is a legal sink for \(g\); equivalently,
   all neighbours of one port accept its terminal type. Either all gains in
   the block have one interchangeable exact terminal type, or a separately
   verified type/identity gadget forbids every illegal terminal assignment.

Conditions 3 and 4 can be weakened to a direct congestion calculation, but
the private form is the clean reusable premise. Saying only that prefixes
are named, or that suffixes exist one at a time, is insufficient.

## 3. Exact factor-router theorem

### Theorem 3.1

Under Sections 1 and 2, all claims in \(G\) have pairwise vertex-disjoint
directed paths in \({\cal D}'\) to distinct legal sinks in \(T'\).
Consequently, adjoining those paths to \(L_I\) gives a simultaneous
compensation-plus-gain linkage in \({\cal D}^c\).

### Proof

Work in the directed subnetwork consisting only of the displayed prefixes
and suffixes. Add a super-source \(\alpha\), an arc

\[
 \alpha\to s_g
\]

of capacity one for every \(g\in G\), a super-sink \(\omega\), and an arc

\[
 t_p\to\omega
\]

of capacity one for every \(p\in P\).

For every incidence \(e=gp\), concatenate the paths \(Q_eR_p\) and send
\(1/h\) units along that concatenation. The resulting flow has the following
loads.

- At claim \(g\), exactly \(h\) incidence paths carry \(1/h\), so the
  source arc \(\alpha\to s_g\) has load one.
- A private prefix interior belongs to one incidence path and has load
  \(1/h\).
- Port \(p\), every vertex of \(R_p\), and the sink arc
  \(t_p\to\omega\) have load

  \[
  \frac{\deg_B(p)}h\le1.
  \tag{3.1}
  \]

- Different suffixes share no vertex, and the prefix-suffix exclusions
  account for every remaining possible overlap.

Thus this is a feasible flow of value

\[
 \sum_{g\in G}\frac{\deg_B(g)}h=|G|.
\tag{3.2}
\]

All capacities in the node-split augmented network are integral. The
integral max-flow theorem therefore supplies an integral flow of value
\(|G|\). Since the total capacity of the arcs
\(\{\alpha\to s_g:g\in G\}\) is exactly \(|G|\), every one of them is
saturated. Since every sink arc has capacity one, flow decomposition gives
one path from each distinct claim to a distinct legal sink. Node splitting
turns integral capacity-disjointness back into vertex-disjointness.
\(\square\)

### Remarks

1. The integral flow chooses one displayed incidence-prefix/port-suffix
   concatenation per gain, but need not preserve the fractional mixture.
   The uniform fractional construction is the certificate that such an
   integral choice exists.
2. The theorem fails if prefix interiors meet other suffixes: the load at
   such a shared vertex can exceed one.
3. The theorem fails if the suffixes are only individually available.
   They must form one simultaneous linkage of the full port set.
4. Integrality may choose a different incident port for a gain, but every
   neighbour port has a legal sink by condition 7. Without that
   type-coherence, ordinary single-commodity flow could make an illegal
   terminal assignment.

## 4. Strict-gammoid form of the router premise

Delete from \({\cal D}'\) every prefix vertex other than its terminal port,
retaining all active ports and all unused typed sinks. Let \(T(g,p)\)
denote the unused sinks legal for incidence \(gp\). For an active port,
define its common legal sink set

\[
 T(p)=\bigcap_{g:gp\in E}T(g,p).
\tag{4.1}
\]

Partition the factor and suffix network into type-homogeneous blocks whose
sink bank lies in \(T(p)\) for every port in the block, or install a
separately proved type/identity-safe gadget. Call the resulting suffix network
\({\cal D}_{\mathrm{suf}}^{\mathrm{type}}\), and let

\[
 \Gamma_{\mathrm{suf}}^{\mathrm{type}}
 =\bigoplus_\tau
   L({\cal D}_{\mathrm{suf},\tau},T'_\tau)
\tag{4.2}
\]

be its strict gammoid direct sum restricted to the active port vertices.
For prescribed, noninterchangeable sink identities, (4.2) is asserted only
after the identity gadget is proved exact; an ordinary common sink bank is
not enough. If \(T(p)=\varnothing\) although different incidences at \(p\)
have nonempty legal sink sets, a gammoid on the physical ports alone is
insufficient; incidence-labelled copies must share one physical
capacity-one port gate, or a different joint-flow model is required.

The private suffix-router premise is exactly

\[
 P\text{ is independent in }\Gamma_{\mathrm{suf}}^{\mathrm{type}},
\quad\text{equivalently}\quad
 r_{\Gamma_{\mathrm{suf}}^{\mathrm{type}}}(P)=|P|.
\tag{4.3}
\]

By heredity, one full-set linkage certifies every port subset. Precisely,
write \(\kappa_{\cal D}(X,T)\) for the minimum capacity of an
\(X\)-to-\(T\) separator in the node-split network. Menger gives

\[
 r_{\Gamma_{\mathrm{suf}}^{\mathrm{type}}}(P)=|P|
 \quad\Longleftrightarrow\quad
 \kappa_{{\cal D}_{\mathrm{suf}}^{\mathrm{type}}}(X,T')
 \ge |X|
 \quad\text{for every }X\subseteq P.
\tag{4.4}
\]

Equivalently, after adding a super-source with one unit arc to every active
port, every super-source-to-\(T'\) cut has capacity at least \(|P|\).
This is the all-cut statement that an abstract factor or a parent matching
does not automatically provide.

If the reference matching is to prove (4.3), one must show that, after
orienting the supplier graph relative to that matching and deleting
\(L_I\), all ports have simultaneous vertex-disjoint alternating suffixes
to distinct unmatched legal sinks. The mere facts that the matching is
maximum, that it saturates its parent shore, or that each port has some
individual augmenting suffix do not imply the simultaneous statement.
Full active-port rank is a clean sufficient certificate used by Theorem
3.1; a smaller port transversal or a different direct congestion
certificate can also link all gains, so (4.3) is not claimed necessary for
every possible router proof.

## 5. The \(h=2\) Middle Levels input

Theorem 2.1 of
[MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md](MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md)
states:

> If \(H\subseteq ML_m\), \(\Delta(H)\le2\), and
> \(|E(H)|\le m-2\), then \(ML_m\) has a spanning two-factor containing
> every edge of \(H\).

To use this as the factor \(B\), first inject the logical gain tickets into
chosen vertices of the left Middle Levels shore and interpret the right
shore as abstract ports. Let \(\Phi\) be the spanning two-factor supplied
by the theorem. It has

\[
 \deg_\Phi(x)=2
 \qquad(x\in V(ML_m)).
\tag{5.1}
\]

For the chosen gain image \(G\), put

\[
 P=N_\Phi(G),\qquad
 B=(G,P;\{gp\in E(\Phi):g\in G\}).
\tag{5.2}
\]

Then every gain has degree two and every active port has degree at most two,
so \(B\) satisfies (2.3) with \(h=2\). It retains literally every protected
incidence whose left endpoint belongs to the chosen gain image. If the
whole left shore is used, \(B=\Phi\). This closes the **abstract factor**
row of Theorem 3.1.

It does not close the physical rows:

- Section 6.1 of that theorem explicitly does not produce a literal
  compiler pull cell or bounded intersection with the reference matching;
- the arbitrary two-factor completion has no proved common cap, occurrence
  address, terminal supplier route, or private prefix expansion; and
- a two-factor can have many components, whereas no private supplier suffix
  linkage follows from its component structure.

Thus the correct \(h=2\) implication is

\[
\begin{array}{c}
\text{2-bounded protected bank of at most }m-2\text{ edges}\\
\Downarrow\\
\text{abstract left-2-regular/right-at-most-2 incidence factor }B\\
\Downarrow\quad\text{only with literal prefixes and (4.3)}\\
\text{full gain linkage after the fixed compensation linkage}.
\end{array}
\tag{5.3}
\]

## 6. Why the parent/reference matching is insufficient by itself

The logical gap is sharp. For any \(m\ge2\), take a 2-regular bipartite
factor on gain claims \(g_1,\ldots,g_m\) and ports
\(p_1,\ldots,p_m\), with private literal prefixes for its incidences.
Let the residual gain gadget consist only of those prefixes followed by
arcs from every port through one common unit-capacity vertex \(v\) to
distinct interchangeable sinks. Thus \(v\) is a cut separating every gain
start, not merely every port, from the sink bank. Put an exact
parent/reference matching and its transported background on capacities
disjoint from this gadget.

Then:

- the protected spanning two-factor exists;
- the parent/reference matching is exact and private;
- every gain and every port is individually nonzero; but
- \(r_{\Gamma_{\mathrm{suf}}^{\mathrm{type}}}(P)=1\), because the cut
  \(\{v\}\) separates every port from every sink.

Only one gain can be linked. The deficiency is \(m-1\). Therefore no
theorem whose hypotheses mention only the abstract two-factor and the
existence of a parent/reference matching can imply a literal router with
bounded deficiency.

## 7. Audit of the current all-\(k\) construction

The current proof inventory separates the two rows rather than closing
them.

1. The small protected-factor theorem proves the owner/q1 two-factor only.
   Its Section 6.1 expressly leaves literal pull cells and bounded damage
   against a reference compiler matching open.
2. Definition 2.2(7) of
   [MATH_THEOREM_BOUNDED_DEPTH_RESCUE_CHAIN_ANCHORED_GAMMOID_CONTRACTION_20260803.md](MATH_THEOREM_BOUNDED_DEPTH_RESCUE_CHAIN_ANCHORED_GAMMOID_CONTRACTION_20260803.md)
   assumes the capacity-faithful linkage relation at the exposed ports.
   Corollary 6.2 assumes the residual trapped-menu cut inequalities after a
   fixed compensation linkage. Neither derives them from the parent
   matching.
3. [MATHEMATICAL_HANDOFF.md](MATHEMATICAL_HANDOFF.md) explicitly records
   that physical provider nesting does not imply supplier-port nesting and
   that the trapped-menu/prefix supplier cuts remain unproved.

Accordingly, the strongest correct present statement is conditional:

> If the all-\(k\) parent/reference matching, after one fixed compensation
> linkage and one common materialization, yields (4.3) for the complete
> active occurrence-labelled port set and is private from the literal prefixes,
> then Theorem 3.1 links every gain. No current theorem establishes that
> premise.

This is an open premise, not a proved failure of every possible
parent/reference router. The counterexample in Section 6 proves only that
the matching and factor hypotheses alone are insufficient. Nor does the
current inventory prove a smaller active-port transversal or another
capacity-faithful direct-flow certificate that could replace (4.3).

## 8. Interface with the two-coordinate common-cap theorem

Let

\[
 F=F^{0+}\mathbin{\dot\cup}F^{+0},
\qquad I=E(F).
\tag{8.1}
\]

The two canonical cross matchings determine the logical ticket set \(I\).
For the common compiler, the index \(q\in\{0,1\}\) denotes the two physical
occurrence coordinates required of every ticket in this union; \(q\) does
not denote the two factor matchings.

For each coordinate, applying the Middle Levels factor theorem requires a
specified injection

\[
 \iota_q:I\hookrightarrow L(ML_m)
\tag{8.2}
\]

and a capacity-faithful identification of the neighbours
\(N_{\Phi_q}(\iota_q(I))\) in a chosen factor \(\Phi_q\) with physical
occurrence ports. If two abstract
right vertices name one physical cell, both must pass through one common
capacity-one gate; the abstract degree bound alone then does not prove the
physical congestion bound. Neither \(\iota_q\) nor this literal lift is
supplied by the Middle Levels factor theorem.

Apply Theorem 3.1 separately to each occurrence coordinate only after:

1. fixing the same cap/common-state assignment in both coordinates;
2. resolving every cross-coordinate shared capacity;
3. proving global product closure, so every pair of marginal representative
   linkages combines legally with no residual cross-ticket coupling, or
   exhibiting one jointly compatible pair of the complete linkages used in
   the conclusion; and
4. using correctly typed, occurrence-labelled prefixes and suffixes.

If both coordinates have exact routers, there are no structural-zero gains,
and the transported background is exact, the residual gain deficiency is
zero. With named exceptional sets \(E_0,E_1\), structural-zero set \(Z\),
and \(\beta\) omitted background targets, the exact Rado/Edmonds formula
gives

\[
 \operatorname{def}_{\mathrm{terminal}}
 \le \beta+|Z|+|E_0\cup E_1|.
\tag{8.3}
\]

Transported phase 1 remains theorem input. Neither this theorem nor the
factor theorem authenticates it as a native or private phase.
