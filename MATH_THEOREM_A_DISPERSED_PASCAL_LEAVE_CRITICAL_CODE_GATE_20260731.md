# Dispersed Pascal leave: critical density, exact code cuts, and the star-cover completion theorem

Date: 2026-07-31  
Lane: A, \(B(k)+O(1)\) dispersed-leave alternative  
Status: exact critical-density ledger, a source-private concentrated obstruction,
and a conditional completion theorem proved; dispersion of the actual reachable
Pascal bank remains open

## 0. Verdict

An \(O(1/m)\)-density leave is at exactly the right **average** scale for

\[
                         N_1=O(1),\qquad N_2=O(m).                 \tag{0.1}
\]

It does not imply either maximum bound.  There are endpoint banks of this
critical cardinality which admit distinct private Pascal facets, but for which
every facet assignment has a one-free code of order \(m\).  Thus neither
task count, distinct endpoints, nor ordinary attachment Hall proves the
dispersed-leave route.

There is nevertheless a precise sufficient theorem.  If the reachable task
bank admits one common representative assignment with bounded upper and lower
Boolean codegrees, and every task has the \(O(d)\) bad-pair star cover for its
entire protected upper bank, then the source atlas has

\[
                  N_0^\times=0,\qquad N_1=O(1),\qquad N_2=O(m),   \tag{0.2}
\]

each list retains \(\Theta(m^2)-O(md)\) choices, and the cross-list conflict
degree is \(O(md)\).  For \(d=o(m)\), Haxell's inequality holds.  This theorem
is independent of the number of tasks once the maximum codegrees are known.

The exact missing statement is therefore a **dispersed Pascal representative
with protected rays**, not a smaller leave count.

## 1. The critical-density identities

Let

\[
 V=[2m-1],\qquad {\cal R}=\binom Vm,\qquad
 M_m=|{\cal R}|=\binom{2m-1}{m}.                                  \tag{1.1}
\]

There are \(H\) Pascal attachment tasks.  Task \(i\) has a distinct endpoint
\(R_i\in{\cal R}\), and an assigned source facet

\[
                         P_i\in\binom V{m-1},\qquad P_i\subset R_i. \tag{1.2}
\]

For a selected facet family \(F=(P_i)_{i=1}^H\), put

\[
 d_+(R)=\#\{i:P_i\subset R\},                                    \tag{1.3}
\]

\[
 d_-(Q)=\#\{i:Q\subset P_i\}
       \quad\left(Q\in\binom V{m-2}\right),                       \tag{1.4}
\]

and

\[
 d_{\rm ext}(R)=\#\{i:P_i\subset R,\ R_i\ne R\}.                  \tag{1.5}
\]

### Theorem 1.1 (exact facet-density ledger)

For every assignment (1.2),

\[
 \sum_{R\in{\cal R}}d_+(R)=mH,\qquad
 \sum_{Q\in\binom V{m-2}}d_-(Q)=(m-1)H,                           \tag{1.6}
\]

and

\[
                         \sum_{R\in{\cal R}}d_{\rm ext}(R)
                              =(m-1)H.                            \tag{1.7}
\]

In particular, if

\[
                         H=\alpha M_m/m,                          \tag{1.8}
\]

then the average upper code is exactly \(\alpha\).  Conversely,
\(\max_Rd_+(R)\le A\) forces

\[
                         H\le A M_m/m.                            \tag{1.9}
\]

#### Proof

Every \((m-1)\)-set in \(V\) has exactly \(m\) rank-\(m\) supersets and
exactly \(m-1\) rank-\((m-2)\) subsets.  This proves (1.6).  Of the \(m\)
rank-\(m\) supersets of \(P_i\), exactly one is its own endpoint \(R_i\), so
task \(i\) contributes \(m-1\) to (1.7).  Averaging gives (1.8)--(1.9).
\(\square\)

Thus a leave of order \(M_m/m\) is count-compatible with (0.1).  It is the
critical scale, not a subcritical scale with automatic maximum-load slack.

There is also a direct weighted-anchor version.  Let

\[
 B_m=\binom{2m+1}{m+1}                                            \tag{1.10}
\]

be the number of rank-\((m+1)\) upper tokens, and let
\(e_i=(C_i,U_i)\), \(U_i=C_i+a_i\), be \(H\) directed incidence anchors
on a \((2m+1)\)-set.  Restrict the code ledger to the upper-vertex shore.

### Proposition 1.2 (exact weighted critical scale)

Each anchor has exactly \(m\) distinct one-free upper tokens \(C_i+c\) and
exactly \(m^2\) distinct zero-free upper tokens \(U_i-b+c\).  Therefore

\[
 \sum_{W\in\binom\Omega{m+1}}N_1^+(W)=mH,\qquad
 \sum_{W\in\binom\Omega{m+1}}N_2^+(W)=m^2H.                       \tag{1.11}
\]

Consequently \(N_1^+\le A\) and \(N_2^+\le Bm\) force

\[
                         H\le\min\{A,B\}\,B_m/m.                  \tag{1.12}
\]

At \(H=\alpha B_m/m\), the averages are exactly \(\alpha\) and
\(\alpha m\).

#### Proof

There are \(m\) choices \(c\notin U_i\).  There are \(m^2\) pairs
\((b,c)\in C_i\times(\Omega\setminus U_i)\), and \(U_i-b+c\) determines
the removed and added coordinates, so these tokens are distinct.  Sum over
anchors and average. \(\square\)

The density in Proposition 1.2 is relative to the \(B_m\) resource shore.
There are \(B_m(m+1)\) directed incidences, so the same \(H\) has density
\(\Theta(1/m^2)\) in the incidence atlas.  These two normalizations must not
be conflated.

## 2. Exact Boolean-interval cuts

The maximum code has a local obstruction which the global average does not
see.

### Theorem 2.1 (upper interval cut)

Let \(W\subseteq V\), \(|W|=m+s\), and let

\[
                         h(W)=\#\{i:R_i\subseteq W\}.              \tag{2.1}
\]

Every representative assignment satisfies

\[
 (s+1)h(W)
       \le \sum_{R\in\binom Wm}d_+(R).                            \tag{2.2}
\]

Consequently, \(\max_Rd_+(R)\le A\) requires the exact cut

\[
                         (s+1)h(W)\le A\binom{m+s}{m}             \tag{2.3}
\]

for every \(W\).  Likewise,

\[
                         s h(W)
       \le\sum_{R\in\binom Wm}d_{\rm ext}(R),                     \tag{2.4}
\]

so \(\max_Rd_{\rm ext}(R)\le A\) requires

\[
                         s h(W)\le A\binom{m+s}{m}.               \tag{2.5}
\]

#### Proof

If \(R_i\subseteq W\), then \(P_i\subseteq W\).  Inside \(W\), that facet
has exactly \(s+1\) rank-\(m\) supersets, proving (2.2).  Exactly one is
\(R_i\), leaving \(s\) external supersets and proving (2.4).  The maximum
bounds give (2.3) and (2.5). \(\square\)

### Proposition 2.2 (lower-shadow capacity cut)

If \(\max_Qd_-(Q)\le A\), then every task subfamily \(X\) satisfies

\[
 (m-1)|X|
   \le A\left|\bigcup_{i\in X}\binom{R_i}{m-2}\right|.            \tag{2.6}
\]

#### Proof

The chosen \(P_i\subset R_i\) has \(m-1\) rank-\((m-2)\) faces.  Count the
pairs \((i,Q)\) with \(Q\subset P_i\).  Each \(Q\) in the displayed union is
used at most \(A\) times. \(\square\)

For the complete endpoint bank in one \(W\) of order \(m+s\), (2.6) forces

\[
                         A\ge\frac{(s+1)(s+2)}m.                  \tag{2.7}
\]

These are necessary cuts, not a claimed integral description.  The upper
and lower code rows overlap and are not a laminar or matroid system.

## 3. A critical-density, source-private obstruction

The interval cuts can fail maximally at the same \(M_m/m\) scale.

### Theorem 3.1 (concentrated bank with an injective facet SDR)

For \(m\ge4\), set

\[
 t=\left\lceil\log_2\frac{m+1}{2}\right\rceil,\qquad
 s=m-1-t,                                                        \tag{3.1}
\]

choose \(W\subseteq V\) with \(|W|=m+s=2m-1-t\), and take one task for
every endpoint

\[
                              R_i\in\binom Wm.                    \tag{3.2}
\]

Then:

1. the task count has \(O(1/m)\) density:
   \[
     H=\binom{2m-1-t}{m}
       \le \frac{2}{m+1}\binom{2m-1}{m}=O(M_m/m);                 \tag{3.3}
   \]
2. the endpoints admit pairwise-distinct facets \(P_i\subset R_i\);
3. for **every** facet assignment, injective or not,
   \[
                         \max_Rd_{\rm ext}(R)\ge s
                            =m-O(\log m).                         \tag{3.4}
   \]

Hence this bank can satisfy private source ownership while violating
\(N_1=O(1)\).  In the suspended C6 source atlas, some auxiliary slot has
external menu load at least

\[
                              2ms=\Omega(m^2).                    \tag{3.5}
\]

#### Proof

For (3.3),

\[
 \frac{\binom{2m-1-t}{m}}{\binom{2m-1}{m}}
   =\prod_{j=0}^{t-1}\frac{m-1-j}{2m-1-j}
   \le2^{-t}\le\frac2{m+1}.                                      \tag{3.6}
\]

For Item 2, consider the inclusion graph from \(\binom Wm\) to
\(\binom W{m-1}\).  Every left vertex has degree \(m\); every right vertex
has degree \(s+1\le m\).  For any left set \(X\), edge counting gives

\[
                         m|X|\le(s+1)|N(X)|\le m|N(X)|.           \tag{3.7}
\]

Hall therefore supplies distinct facets.

For Item 3, every selected \(P_i\subset W\) has \(s+1\) rank-\(m\)
supersets in \(W\), one of which is \(R_i\).  Hence

\[
 \sum_{R\in\binom Wm}d_{\rm ext}(R)
      =s\binom{m+s}{m}.                                          \tag{3.8}
\]

There are \(\binom{m+s}{m}\) summands, so (3.4) follows.  The exact
auxiliary-slot role contributes \(2m\,d_{\rm ext}(R)\), which proves
(3.5). \(\square\)

This is a theorem about the exact Pascal endpoint/facet interface.  It does
not claim that this concentrated bank is already the leave of a complete
physical old-colour-exact forest.  It proves that cardinality, distinct
endpoints and private-facet Hall alone cannot establish dispersion for an
actual leave.

## 4. The sufficient dispersed-code plus star-cover theorem

We now state the positive implication at the level needed by the buffered
packet selector.

### Definition 4.1 (DPR--SCPR state)

A task bank is an \((A,K,d)\)-DPR--SCPR state if it has an assignment
\(P_i\subset R_i\) such that:

1. the \(P_i\) and \(R_i\) are separately pairwise distinct;
2. \(\max_Rd_+(R)\le A\) and \(\max_Qd_-(Q)\le A\);
3. at each assigned anchor, the union bad graph of **all** protected upper
   targets is on parameter shores of order at most \(m\), has one menu
   candidate per parameter edge, and has vertex-cover number at most \(Kd\);
4. every nonanchor colour, physical, witness, topology and common-cap token
   used by the declared packet has weighted-code bounds
   \(N_1\le A_1\), \(N_2\le A_2m\), for constants \(A_1,A_2\), and every
   source-fixed token is private across lists; and
5. the token support of a packet is at most \(s_0d+s_1\), with every
   physical condition needed for literal composition represented among
   these tokens.

Item 4 is stated separately because the Pascal incidence table proves it
for its ordinary auxiliary colour/owner roles from Item 2, but not for a
complete common-cap ticket or a global topology witness.

### Theorem 4.2 (dispersed-leave completion)

For an \((A,K,d)\)-DPR--SCPR state, the ordinary Pascal incidence roles
satisfy

\[
                  N_0^\times=0,\qquad N_1\le A,\qquad N_2\le Am. \tag{4.1}
\]

More generally, let \(C_{\rm load}=A_1+A_2\) after summing the finitely many
declared token types.  Every task list retains at least

\[
                         L\ge L_0-Kmd,                            \tag{4.2}
\]

where \(L_0=\Theta(m^2)\) is its unguarded list size, and every retained
packet has cross-list conflict degree at most

\[
                         \Delta\le
                         C_{\rm load}(s_0d+s_1)m.                 \tag{4.3}
\]

Consequently, whenever

\[
 L_0-Kmd\ge2C_{\rm load}(s_0d+s_1)m,                             \tag{4.4}
\]

there is an independent choice of one literal packet for every task.  In
particular, (4.4) holds for all sufficiently large \(m\) when \(d=o(m)\)
and all displayed constants are dimension-independent.

#### Proof

Distinct \(P_i\) and \(R_i\) prevent fixed--fixed repetition.  Item 4 of
Definition 4.1 additionally prevents a source-fixed core from occurring
auxiliarily in another list, so its **external** fixed-role code is
\(N_0^\times=0\).  The exact Pascal role table has one-free fibres
\(d_-(Q)\) and \(d_+(R)\).  Its zero-free swapped fibre is

\[
 d_J(P')\le
 \min\{(m-1)\max_Qd_-(Q),\ m\max_Rd_+(R)\}\le Am,                 \tag{4.5}
\]

and the remaining zero-free fibres are bounded by \(d_+(R)\le A\).  This
proves (4.1).

By the star-cover theorem and the parameter-shore/fibre clause in
Definition 4.1, a bad graph with cover number \(Kd\) has at most \(Kmd\)
candidate edges, proving (4.2).  With \(\mu\) candidates over each
parameter edge, the correct loss would instead be \(\mu Kmd\).  The exact
weighted-anchor ledger
assigns load \(mN_1+N_2\le C_{\rm load}m\) to each nonprivate token.
Summing over at most \(s_0d+s_1\) tokens proves (4.3).  Haxell's independent
transversal theorem applies under (4.4).  Because all declared physical
compatibilities are tokenized, an independent transversal is a literal
packet choice, not merely a marginal colour assignment. \(\square\)

The theorem intentionally does not infer connectedness or a common-cap
compiler from colour privacy.  Those properties must either be tokenized in
Item 4 or supplied by a separate composition theorem.

### Corollary 4.3 (partial-Steiner source condition)

If the selected facets \(P_i\) are distinct and no rank-\((m-2)\) set lies
in two of them, then

\[
                         \max_Qd_-(Q)=\max_Rd_+(R)=1.             \tag{4.6}
\]

Thus the ordinary source roles have the optimal raw bounds
\(N_1\le1\), \(N_2\le m\).

#### Proof

The first equality is the hypothesis.  If two distinct selected facets
were contained in one rank-\(m\) set \(R\), their intersection would have
rank \(m-2\) and would lie in both, a contradiction. \(\square\)

Corollary 4.3 identifies a concrete positive design target.  It does not
assert that every reachable endpoint bank has such a transversal.

## 5. What remains for the actual reachable Pascal bank

The current Pascal attachment theorem proves the uncapacitated SDR
\(P_i\subset R_i\).  It does not prove Item 2 of Definition 4.1.  The
per-seam audit also shows that canonical endpoint reuse has the wrong
star-cover polarity: even one outward extreme ray leaves one safe
\(c\)-star and has bad graph \(K_{m,m-1}\).  Thus Item 3 requires a
key-preloaded/noncanonical rail or a packet-private replacement witness.

The minimal live statement is the following.

### Dispersed protected Pascal representative (DPPR)

For every actually reachable leave bank with

\[
                         H\le C M_m/m,                            \tag{5.1}
\]

choose one literal eligible anchor per task so that, for constants depending
only on \(C\),

\[
 \max_Rd_+(R),\ \max_Qd_-(Q)=O_C(1),\qquad
 \tau(G_i^{\rm all\ upper})=O_C(d)                               \tag{5.2}
\]

for every task \(i\), while the common-cap, topology and witness tokens obey
the same weighted code and source-privacy rows.

DPPR plus Theorem 4.2 proves the dispersed-leave packet selection for
\(d=o(m)\).  No current theorem proves DPPR.  Theorem 2.1 supplies an exact
family of necessary Boolean-interval cuts, and Theorem 3.1 shows those cuts
can fail at the critical leave size despite ordinary Hall and source
privacy.

Therefore the dispersed-leave alternative is **count-feasible but not yet
constructively aligned**.  Its smallest missing gate is a bounded-codegree
representative theorem on the actual physical leave, coupled to the
favorable-polarity whole-collar condition; an \(O(1/m)\) cardinality bound
alone is insufficient.

## 6. Scope audit

1. The density normalization is \(H/M_m\), where \(M_m\) is the number of
   rank-\(m\) Pascal endpoints.  Proposition 1.2 gives the corresponding
   rank-\((m+1)\)-resource normalization.  Density in the full directed
   incidence atlas differs by another factor \(m\).
2. The concentrated bank is an exact endpoint/facet obstruction, not a
   materialized regenerative leave.
3. The star-cover row is per task but covers that task's entire protected
   upper bank; targetwise \(O(d)\) covers do not suffice unless their union
   has size \(O(d)\).
4. The weighted source roles do not automatically cover common-cap,
   residence, topology or witness tickets.  Definition 4.1 explicitly
   retains those hypotheses.
5. The result is a sufficient packet-selection theorem.  It does not prove
   \(B(k)+O(1)\), because DPPR and the subsequent regenerative composition
   are open.
