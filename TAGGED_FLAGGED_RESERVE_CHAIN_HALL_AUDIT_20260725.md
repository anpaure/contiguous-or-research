# Tagged flagged reserve: the exact chain-Hall cut and a weighted-level obstruction

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

This note audits the flagged-reserve gate in
`MATH_ATTACK_H_RAINBOW_CATALOGUE_RESERVE_COMPLETION_20260725.md`.
It gives one positive exact theorem and one sharp obstruction.

Let

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad M=m+H,
 \qquad N=\binom{2m}{M},
 \tag{0.1}
\]

at the calibrated crossing, so that

\[
 MN=W-o(W),\qquad Q=o(H),\qquad Q/\sqrt m\longrightarrow\infty.
 \tag{0.2}
\]

The conclusions are as follows.

1. There is an exact joint Hall theorem for covering holes by independent
   hosted rotor state-columns.  Its cuts couple all protected ranks at
   once.  The separate-rank host Hall inequalities are only a small subset
   of these cuts.
2. In particular, every reserve certificate with (R) base trajectories,
   (S) localized cells, and (E) literal exceptions satisfies
   \[
   \boxed{
   \operatorname{width}({\cal H})
   \le MR+(4Q+4)S+E.}
   \tag{0.3}
   \]
   Here width is taken in the inclusion poset on the union of all protected
   hole rows.
3. Conversely, if
   \[
   \operatorname{width}({\cal H})=o(W/Q),
   \tag{0.4}
   \]
   then the holes can be completed directly by one-state radius-(Q)
   chunks at cost (o(W)).  This is a genuine cross-rank sufficient
   theorem.
4. The catalogue row budgets alone do not imply (0.3) at the desired
   reserve scale.  There is an explicit antichain of
   \((\eta+o(1))W\) protected targets, for an absolute \(\eta>0\), whose
   intersection with
   every protected rank has size (O(W/\sqrt m)).  Taking
   \[
   R=\Theta(N/\sqrt m)=o(N)
   \tag{0.5}
   \]
   makes every row fit inside the exact exceptional budget (c_qR), but
   any bank with (S=O(RM/Q)) then forces (E=\Omega(W)), even if carrier
   hosting is made completely unrestricted.

Thus common priority nesting inside each catalogue trajectory does not by
itself give the needed laminarity of the **complement hole family**.  A
successful near-matching theorem must prove a new global invariant: at a
minimum, its residual hole poset must have width (o(W)), and for a direct
one-state completion it must have width (o(W/Q)).  To exploit the larger
(O(RM)) endpoint allowance of the cell bank, one additionally needs a
routeable braid-block decomposition.

## 1. The protected hole poset

Put

\[
 {\cal P}_Q
 =\binom{[2m]}m
 \cup
 \bigcup_{q=1}^Q
 \left(
 \binom{[2m]}{m-q}\cup\binom{[2m]}{m+q}
 \right),
 \tag{1.1}
\]

ordered by inclusion.  Let

\[
 {\cal H}\subseteq {\cal P}_Q
 \tag{1.2}
\]

be the union of the protected hole families after the core stage.

A radius-(Q) rotor state

\[
 \omega=(A;z_1,\ldots,z_{2Q};B)
 \tag{1.3}
\]

exposes the saturated inclusion chain

\[
 A\subset A+z_1\subset\cdots\subset A+z_1+\cdots+z_{2Q}.
 \tag{1.4}
\]

Consequently one state endpoint can cover at most one member of every
antichain in ({\cal P}_Q).  This elementary observation is the source of
the missing joint cut.

## 2. Exact tagged chain-Hall theorem

Let ({\cal R}\subseteq\binom{[2m]}M) be a family of allowed carrier tags,
and give each (U\in{\cal R}) a nonnegative integral state-column capacity
(b_U).

For ({\cal A}\subseteq{\cal H}), define

\[
 \Gamma_{\cal H}^+({\cal A})
 =\{T\in{\cal H}:\text{ some }S\in{\cal A}
 \text{ satisfies }S\subsetneq T\},
 \tag{2.1}
\]

and

\[
 \Gamma_{\cal R}({\cal A})
 =\{U\in{\cal R}:\text{ some }S\in{\cal A}
 \text{ satisfies }S\subseteq U\}.
 \tag{2.2}
\]

### Theorem 2.1 (tagged chain-Hall)

The following statements are equivalent.

1. The hole family ({\cal H}) can be partitioned into inclusion chains,
   each chain can be assigned to a tag containing all its members, and at
   most (b_U) chains are assigned to (U).
2. For every ({\cal A}\subseteq{\cal H}),
   \[
   \boxed{
   |{\cal A}|
   \le
   |\Gamma_{\cal H}^+({\cal A})|
   +\sum_{U\in\Gamma_{\cal R}({\cal A})}b_U.}
   \tag{2.3}
   \]
3. There are at most \(\sum_Ub_U\) hosted radius-\(Q\) state-columns whose
   union covers every member of ({\cal H}).

#### Proof

Make a capacitated bipartite graph.  Its left class is one copy
(S_L) of every (S\in{\cal H}).  Its right class consists of one copy
(T_R) of every (T\in{\cal H}), of capacity one, together with the tags
(U\in{\cal R}), of capacity (b_U).  Put in the edges

\[
 S_L T_R\quad\Longleftrightarrow\quad S\subsetneq T,
 \tag{2.4}
\]

and

\[
 S_L U\quad\Longleftrightarrow\quad S\subseteq U.
 \tag{2.5}
\]

The capacitated Hall condition for a matching saturating every left vertex
is exactly (2.3).

Suppose such a matching is chosen.  Direct an edge (S\to T) whenever
(S_L) is matched to (T_R).  Every hole has outdegree one until its chain
terminates at a tag, and every hole has indegree at most one.  Strict
inclusion forbids directed cycles.  The directed components are therefore
disjoint inclusion chains ending at tags.  A chain ending at (U) is
contained in (U), because its maximal member is contained in (U).
The tag capacities give statement 1.

Conversely, a tagged chain partition matches every nonmaximal member of a
chain to its successor and its maximal member to the assigned tag.  This
gives the saturating capacitated matching, so statements 1 and 2 are
equivalent.

Finally, extend every chain through any omitted ranks to a saturated chain
between ranks (m-Q) and (m+Q).  Since its maximal member lies in its
tag, the extension may be chosen inside that tag.  Ordering the successive
new labels gives a rotor state whose exposed flag column contains the
whole chain.  Conversely, every rotor state-column is an inclusion chain.
This proves the equivalence with statement 3. \(\square\)

### Remarks

1. Literal exceptions can be included exactly by first deleting an
   exception family ({\cal E}\subseteq{\cal H}), applying (2.3) to
   ({\cal H}\setminus{\cal E}), and then patching the members of
   ({\cal E}) individually.  There is no valid shortcut which lets one
   literal endpoint terminate and pay for an entire nontrivial chain.
2. Theorem 2.1 treats independent state-columns.  It deliberately does
   not assert that the chosen states can be ordered into only
   (O((\sum b_U)/Q)) legal localized cells.  That is the additional
   braid-route problem.

## 3. Exact antichain and width cuts for a real reserve

Suppose the reserve uses one length-(M) base trajectory on every one of
(R) reserve tags and (S) localized cells.  A base trajectory has (M)
state endpoints.  A localized cell has at most (4Q+4) state endpoints.

### Proposition 3.1 (joint antichain cut)

For every antichain ({\cal A}\subseteq{\cal H}), every positive reserve
certificate with (E) literal exceptions satisfies

\[
 \boxed{
 |{\cal A}|
 \le MR+(4Q+4)S+E.}
 \tag{3.1}
\]

Consequently

\[
 \boxed{
 \operatorname{width}({\cal H})
 \le MR+(4Q+4)S+E.}
 \tag{3.2}
\]

#### Proof

Every state endpoint exposes one inclusion chain, which meets
({\cal A}) in at most one target.  There are at most (MR) base
endpoints and at most ((4Q+4)S) cell endpoints.  Each literal patch
covers at most one further member of ({\cal A}).  This proves (3.1), and
maximizing over antichains proves (3.2). \(\square\)

Under the desired bank scale

\[
 S=O(RM/Q),
 \tag{3.3}
\]

Proposition 3.1 becomes

\[
 \operatorname{width}({\cal H})=O(RM)+E.
 \tag{3.4}
\]

In particular, if (R=o(N)) and (E=o(W)), then

\[
 \boxed{\operatorname{width}({\cal H})=o(W)}.
 \tag{3.5}
\]

This is a necessary cross-rank invariant which is absent from the row
ledger (0.6) of the reserve note.

### Theorem 3.2 (low-width positive completion)

If

\[
 \operatorname{width}({\cal H})=w,
 \tag{3.6}
\]

then the protected holes have a literal positive radius-(Q) reserve word
of length at most

\[
 \boxed{(2Q+2)w.}
 \tag{3.7}
\]

Hence

\[
 w=o(W/Q)
 \quad\Longrightarrow\quad
 \operatorname{RCov}_Q({\cal H})=o(W).
 \tag{3.8}
\]

#### Proof

By Dilworth's theorem, partition ({\cal H}) into (w) inclusion chains.
Extend every chain to a saturated segment through the protected ranks.
Its rank-((m+Q)) member can be extended further to some (M)-carrier,
because (m+Q<M).  The saturated protected segment is therefore the flag
column of a legal state in that carrier.  Compile each state as a
one-state chunk.  Formula (1.6) of the truncated-reserve note gives exact
cost

\[
 1+(2Q+1)=2Q+2

\]

per chunk.  Every hole is covered positively. \(\square\)

Theorem 3.2 is stronger than literal target-by-target repair whenever many
holes are nested.  It is not strong enough for a generic (O(RM))-width
leave: achieving the cell-bank scale then requires grouping about (Q)
state-columns per (O(Q))-cost localized object, with the exact braid
chronology retained.

## 4. A weighted Boolean level

We now give an explicit hole profile which passes every scalar row budget
but violates (3.2).  It is enough to work along the subsequence on which
(m) is even.

Partition

\[
 [2m]=B\sqcup C,
 \qquad |B|=|C|=m,
 \tag{4.1}
\]

and define the strictly increasing set weight

\[
 \operatorname{wt}(S)=2|S\cap B|+|S\cap C|.
 \tag{4.2}
\]

Put

\[
 {\cal A}
 =\left\{S\subseteq[2m]:
 \operatorname{wt}(S)=\frac{3m}{2}\right\}.
 \tag{4.3}
\]

### Lemma 4.1 (weighted-level antichain and slices)

The family ({\cal A}) is an antichain.  Its rank-((m+q)) slice has
exact size

\[
 \boxed{
 a_q
 =\binom m{m/2-q}\binom m{m/2+2q}.}
 \tag{4.4}
\]

Uniformly for (|q|\le A\sqrt m), where (A) is fixed,

\[
 \boxed{
 a_q
 =\left(\frac{2}{\sqrt{\pi m}}+o(m^{-1/2})\right)
 W\,e^{-10q^2/m}.}
 \tag{4.5}
\]

Moreover, for

\[
 {\cal A}^{(1)}
 ={\cal A}\cap
 \bigcup_{|q|\le\sqrt m}\binom{[2m]}{m+q},
 \tag{4.6}
\]

there is an absolute constant \(\eta>0\) such that

\[
 \boxed{|{\cal A}^{(1)}|=(\eta+o(1))W.}
 \tag{4.7}
\]

One may take

\[
 \eta
 =\frac{2}{\sqrt\pi}\int_{-1}^{1}e^{-10x^2}\,dx>0.
 \tag{4.8}
\]

#### Proof

Proper inclusion strictly increases (4.2), so one weight level is an
antichain.  If (j=|S\cap B|), the equations

\[
 j+|S\cap C|=m+q,
 \qquad
 2j+|S\cap C|=3m/2

\]

give

\[
 j=m/2-q,
 \qquad
 |S\cap C|=m/2+2q,

\]

which proves (4.4).

The uniform central-binomial estimate

\[
 \binom m{m/2+x}
 =2^m\sqrt{\frac{2}{\pi m}}
 \exp\!\left(-\frac{2x^2}{m}+o(1)\right)
 \tag{4.9}
\]

for (x=O(\sqrt m)), together with

\[
 W=(1+o(1))\frac{4^m}{\sqrt{\pi m}},

\]

gives (4.5).  Summing (4.5) over (|q|\le\sqrt m) and taking a Riemann
sum gives (4.7)--(4.8). \(\square\)

For reference, summing over all (q) gives

\[
 |{\cal A}|=(\sqrt{2/5}+o(1))W,
 \tag{4.10}
\]

but only the protected subfamily (4.6) is needed.

## 5. The weighted level fits all H-catalogue row budgets

Recall

\[
 c_0=M,
 \qquad
 c_q=\min\left\{M,
 \left\lfloor\frac{R_q}{N}\right\rfloor\right\},
 \qquad
 R_q=\binom{2m}{m-q}.
 \tag{5.1}
\]

### Lemma 5.1 (uniform shallow quota lower bound)

There is an absolute (kappa>0) such that, for all sufficiently large
(m),

\[
 \boxed{c_q\ge\kappa m
 \qquad(0\le q\le\sqrt m).}
 \tag{5.2}
\]

#### Proof

At the calibrated crossing, (W/N\ge M).  Uniformly for
(q\le\sqrt m),

\[
 \frac{R_q}{W}
 =\exp\!\left(-\frac{q^2}{m}+o(1)\right)
 \ge e^{-2}
 \tag{5.3}
\]

for all sufficiently large (m).  Hence

\[
 \frac{R_q}{N}\ge e^{-2}M.

\]

Taking the floor and the cap at (M) proves (5.2), for example with
(kappa=e^{-2}/2). \(\square\)

Choose a sufficiently large absolute constant (K), and put

\[
 \boxed{R=\left\lceil K\frac{N}{\sqrt m}\right\rceil.}
 \tag{5.4}
\]

Then (R=o(N)), while Lemmas 4.1 and 5.1 give, for every
(|q|\le\sqrt m),

\[
 a_q\le c_{|q|}R.
 \tag{5.5}
\]

Indeed (a_q=O(W/\sqrt m)), (c_{|q|}R=\Omega(mN/\sqrt m)), and
(mN=(1+o(1))W).  Choose (K) to absorb the absolute constants.

Define the hypothetical protected leave by

\[
 {\cal H}_{m+q}
 ={\cal A}\cap\binom{[2m]}{m+q}
 \quad(|q|\le\sqrt m),
 \tag{5.6}
\]

and take all other protected hole rows empty.  Then

\[
 \boxed{
 h_{q,\pm}\le c_qR\le\delta_q+c_qR,}
 \tag{5.7}
\]

and the middle row also obeys (h_0\le MR\).  Thus (5.6) passes the exact
row ledger (2.2)--(2.3) of the H-catalogue reserve note.  It also lies
inside the actual protected window because (Q/\sqrt m\to\infty).

### Theorem 5.2 (minimal explicit joint-cut obstruction)

For the hole profile (5.6), every reserve with

\[
 S=O(RM/Q)
 \tag{5.8}
\]

has

\[
 \boxed{E=\Omega(W).}
 \tag{5.9}
\]

This remains true if every hole is artificially declared hostable on every
reserve carrier; hence it is independent of all carrier-containment and
separate-rank host Hall issues.

#### Proof

The union of the hole rows is the antichain ({\cal A}^{(1)}).  By
Proposition 3.1,

\[
 E
 \ge |{\cal A}^{(1)}|-MR-(4Q+4)S.
 \tag{5.10}
\]

Equations (0.2), (5.4), and (5.8) give

\[
 MR=O(W/\sqrt m)=o(W),
 \tag{5.11}
\]

and

\[
 (4Q+4)S=O(RM)=o(W).
 \tag{5.12}
\]

Equation (4.7) now gives

\[
 E\ge(\eta-o(1))W,

\]

which proves (5.9).  The argument used no host restriction at all.
\(\square\)

Theorem 5.2 does **not** assert that this weighted antichain is the leave
of an already-constructed partial common catalogue matching.  It proves
the exact point which the reserve argument was missing: the currently
recorded consequences of such a partial matching--row counts, scalar
capacity, separate-rank Hall, and common priority inside each selected
edge--do not include any inequality excluding (5.6).  A successful
near-matching theorem must establish that its actual residual complement
cannot contain a weighted-level obstruction of this kind.

## 6. What common priority does and does not prove

For one decorated catalogue trajectory, let

\[
 h(j)=\max\{q:j\le c_q\}
 \tag{6.1}
\]

be the claimed height of priority phase (j).  Its claims are a Ferrers
family of literal flag columns: phase (j) claims the lower and upper
flags through depth (h(j)).  This is genuine vertical nesting.

After selecting core trajectories, however, the hole family is the
**complement** of the union of their claimed targets.  Nesting of every
selected edge does not give a chain decomposition of that complement.
The exact condition needed for independent reserve columns is (2.3), not
the (2Q+1) separate row Hall inequalities.  The weighted-level family
in Section 5 is the minimal model of what can go wrong: every row is small,
but the rows are mutually arranged as one macroscopic antichain.

There are now three progressively stronger useful gates.

1. **Chain-width gate.**  If
   \[
   \operatorname{width}({\cal H})=o(W/Q),
   \]
   Theorem 3.2 completes directly.
2. **Tagged state-column gate.**  If (2.3) holds with total tag capacity
   (o(W/Q)), Theorem 2.1 and one-state compilation complete directly.
3. **Braid-block gate.**  At the desired larger endpoint scale
   (O(RM)), prove (2.3) with (b_U=O(M)) and then partition the resulting
   hosted state-columns into (O(RM/Q)) legal localized rotor cells or
   (Q)-long chunks.  This final routeability assertion is strictly
   stronger than chain Hall.

Theorem 5.2 shows that one cannot jump directly from the row ledger to
the braid-block gate.  The cross-rank Hall cut must first be proved for the
actual residual leave.

## 7. Final status

The flagged-reserve lane has gained an exact joint-flow formulation and a
new unconditional sufficient condition:

\[
 \boxed{
 \operatorname{width}({\cal H})=o(W/Q)
 \Longrightarrow
 \operatorname{RCov}_Q({\cal H})=o(W).}
 \tag{7.1}
\]

It has also acquired a sharp no-go for the presently stated rowwise
hypotheses:

\[
 \boxed{
 R=\Theta(N/\sqrt m),\quad
 h_{q,\pm}\le c_qR\ \forall q,
 \quad
 \operatorname{width}({\cal H})=\Theta(W).}
 \tag{7.2}
\]

At this scale, (S=O(RM/Q)) localized cells leave
(E=\Omega(W)).  Therefore the proposed improvement from the old
(R=o(N/\sqrt m)) exceptional-tag threshold to arbitrary (R=o(N))
cannot follow from rowwise capacity and separate-rank Hall alone.

The remaining positive theorem is precise:

> Construct the partial common catalogue matching so that its residual
> hole poset satisfies tagged chain Hall with total endpoint capacity
> (O(RM)), excludes macroscopic weighted antichains, and admits a
> decomposition of those hosted endpoint chains into (O(RM/Q)) legal
> braid blocks, up to (o(W)) literal exceptions.

No such theorem is proved here.  The new obstruction identifies the first
joint cut that any proof must control before rotor chronology is even
considered.
