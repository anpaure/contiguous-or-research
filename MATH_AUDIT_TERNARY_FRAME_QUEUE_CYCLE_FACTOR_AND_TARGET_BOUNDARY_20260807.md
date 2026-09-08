# Independent audit of the ternary-frame queue cycle factor and target boundary

**Date:** 2026-08-07  
**Audited theorem:**  
MATH_THEOREM_TERNARY_FRAME_QUEUE_CYCLE_FACTOR_AND_TARGET_BOUNDARY_20260807.md  
**Audited theorem SHA-256:**  
\[
\texttt{ce97e1323fbe8efd9913b6312e9fecd3a2978f23c22a7e1762db7aaa809cf1d1}.
\]
**Verdict:** **PASS**, with the scope restrictions stated in Section 4
below. No computation is used in this audit.

## 1. Canonical frames and the quotient cycle factor

For a fixed ordered global triple partition, changing the omitted element
inside any one of the first \(p\) selected two-triples preserves both the
ordered selected-triple list and the outside core. Hence every good owner
belongs to one full \(\mathbb F_3^p\)-frame and the good frames are
pairwise disjoint.

Under the independent \(1/2\)-model, the number of two-triples is
\(\operatorname{Bin}(\lfloor n/3\rfloor,3/8)\), up to the unused
coordinates. Since \(p=O(\sqrt n)\), the probability of having fewer
than \(p\) such triples is \(e^{-\Omega(n)}\). Conditioning on the
central slice costs only a polynomial factor, so the same exponential
bound holds there.

Put \(G=\mathbb F_3^a\), \(a=\lceil\log_3p\rceil\), and
\(q=|G|=3^a\). The affinely spanning points \(g_0,\ldots,g_{p-1}\)
make the difference map

\[
 H(e_i)=g_{i+1}-g_i
\]

surjective. For \(B=\ker H\),

\[
 v=\sum_i e_i\in B,\qquad
 H(w_i)=g_i-g_0,
\]

so the \(p\) cosets \(B+w_i\) are distinct and \(e_i\notin B\).
The phase-\(i\) edge

\[
 x+w_i\longrightarrow x+w_{i+1}
\]

therefore gives indegree and outdegree one on the disjoint union of those
cosets. After one \(p\)-phase round it translates \(x\) by the nonzero
order-three vector \(v\). Thus every component has length exactly \(3p\),
there are \(|B|/3\) components, and the covered fraction is exactly

\[
 \frac{p|B|}{3^p}=\frac pq>\frac13.
\]

The all-frame phase-periodic divisibility boundary is also correct:
every component length is divisible by \(p\), so covering all \(3^p\)
states forces \(p\mid3^p\), equivalently \(p\) is a power of three. When
\(p\) is a power of three, \(q=p\) and the displayed construction covers
the full frame.

## 2. Literal queue checks

At phase \(i\), the inserted source letter is the core \(K\) together
with a two-subset of \(T_i\). Any \(p\) consecutive phases contain each
selected triple exactly once, so their union is exactly the current
rank-\(m\) owner. A transition changes one omitted symbol in one triple,
and hence is a Johnson edge.

After a complete phase round, every omitted symbol advances once.
Accordingly each selected-triple coordinate has owner gap \(p\) and run
\(2p\), while every core coordinate is permanent.

For a phase-\(i\) edge, either immediate colour identifies the active
triple \(i\). Equality of two same-phase upper colours forces their
omission states to agree outside coordinate \(i\); their difference lies
in

\[
 B\cap\langle e_i\rangle=\{0\}.
\]

The same argument applies to lower colours; within the active triple the
retained singleton uniquely determines the directed cyclic omission
change. Thus both q1 palettes are simple across the entire selected
factor **inside one frame**.

A suffix of \(j\le p\) source positions visits \(j\) distinct phase
triples, so its rank is \(c+2j\). For \(j<p\), the target identifies the
proper cyclic phase interval. The three occurrences of that interval in
one \(3p\)-cycle differ by the order-three omission translation, so the
fixed-depth suffix targets are distinct inside that cycle.

## 3. Exact rank-\((c+2)\) target obstruction

Every canonical singleton source in a fixed frame is one of

\[
 K\cup(T_i\setminus\{x\}),
 \qquad i\in[p],\quad x\in T_i.
\]

These \(3p\) sets are pairwise distinct, and no other singleton source
value is possible under the canonical source rule, even with a
nonstationary omission schedule. Therefore a target-clean selection in
one frame has at most \(3p\) source positions. A cyclic bank consequently
uses at most \(3p\) owner vertices, while a path bank with \(C\)
components uses at most \(3p+C\) owner vertices.

The bound is attained locally by any one \(3p\)-cycle: every phase occurs
three times and its omitted symbol rotates through all three choices, so
the cycle uses the whole \(3p\)-element inventory once.

## 4. Exact scope

The following claims are audited and valid:

1. almost all middle owners lie in canonical frames;
2. each frame has an explicit phase-periodic cycle factor covering
   exactly \(p/q>1/3\) of its owners;
3. q1 simplicity holds across all selected cycles within one frame;
4. the literal queue has the asserted flatness, residence, and
   fixed-depth suffix ranks;
5. the canonical singleton-source inventory of one frame has size exactly
   \(3p\), giving the sharp fixed-frame target no-go.

The theorem does **not** prove:

1. q1 palette disjointness between different canonical frames;
2. target disjointness between cycles chosen in different frames;
3. a target-clean positive-density global bank;
4. fusion of the cycles into one chronology;
5. the residual PBBS/compiler gates;
6. a no-go for noncanonical source letters, frame-changing components, or
   constructions correlating many different global triple partitions.

With these boundaries explicit, the theorem is proof-safe and may be
cited as the unconditional owner-only queue packing and the exact
fixed-frame target obstruction.
