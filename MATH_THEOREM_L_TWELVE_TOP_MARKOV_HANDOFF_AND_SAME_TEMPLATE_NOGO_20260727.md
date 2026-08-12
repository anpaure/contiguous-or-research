# Twelve-top Markov handoff: a bounded open fusion and the same-template no-go

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\tag{0.1}
\]

and assume \(H\ge3\), \(M\ge18H-10\). Fix one repaired twelve-top
bidirectional recharge template from
MATH_THEOREM_TWELVE_TOP_HISTOGRAM_NEUTRAL_BIDIRECTIONAL_RECHARGE_20260727.md.
Write its two shores as

\[
 S_0={\bf p}\sqcup r{\bf q},
 \qquad
 S_1=r{\bf p}\sqcup{\bf q}.
\tag{0.2}
\]

The requested fusion has one positive and one negative conclusion.

### Theorem A (certified fifteen-top open fusion)

Starting from \(S_0\), one may:

1. apply the repaired twelve-top recharge \(S_0\to S_1\);
2. apply one two-top collar-neutral rectangle to a chosen row of
   \(S_1\); and
3. apply one three-top collar-neutral reroot to that changed row.

With all auxiliary tops chosen outside the twelve-top carrier, this is
a literal chronology on at most fifteen tops. Its complete ledger is

\[
 \boxed{
 \Delta_h=0\quad(h\ne H),\qquad
 \Delta_H=R,}
\tag{0.3}
\]

where \(R\) is the nonzero elementary hypersimplex rectangle used in
Step 2. The reroot changes the boundary direction available on the
focal row.

At the endpoint, eleven of the twelve carrier rows remain exact rows of
the inverse source \(S_1\). The focal carrier row is not an \(S_1\)
row: it lies in a new boundary component after the rectangle and
three-top reroot. Thus the fusion advances the direction but leaves one
literal carrier-state defect.

### Theorem B (same-template Markov handoff is impossible)

Consider any chronological macro built from:

- repaired twelve-top recharge packets;
- collar-neutral two-top rectangles; and
- full-trace-neutral three-top reroot packets.

Suppose it starts at \(S_\epsilon\), ends at either
\(S_0\) or \(S_1\) of the **same repaired template**, and restores every
top outside this twelve-top carrier. Then its net protected derivative
is zero at every length:

\[
                         \boxed{\Delta_h=0
                         \quad(0\le h\le2H).}
\tag{0.4}
\]

In particular its net sum of middle rectangle directions is zero. No
bounded macro can both

1. advance a nonzero middle rectangle direction, and
2. leave all helpers in a certified source shore of the same twelve-top
   template.

This is not a rank or histogram argument. It follows from the literal
endpoint deck equality

\[
                         {\cal D}(S_0)={\cal D}(S_1)
\tag{0.5}
\]

proved by the repaired recharge theorem.

### Exact Markov gate

A successful bounded Markov macro must therefore do at least one of the
following:

1. hand off to a **different** twelve-top template, with a different
   carrier decomposition, core, palette chart, or filler matching;
2. leave an open helper-state defect which is consumed by the next
   macro; or
3. use a new nonneutral primitive beyond the present three-move library.

The target is no longer a closed conjugation of one repaired packet.
It is a transition between distinct certified twelve-top source shores
inside the same position--label histogram fibre. That is precisely the
nonnegative seam-Markov problem left open by the position-label fibre
theorems.

## 1. The repaired twelve-top state graph is a two-cycle

Fix the common core \(C\), the two edge-disjoint six-cycles \(P,Q\),
the repaired proper edge-colouring of their \(F\)- and \(G\)-palettes,
and the columnwise filler matching. These data determine the word
tables

\[
                         {\bf p}=(p_0,\ldots,p_5),
 \qquad
                         {\bf q}=(q_0,\ldots,q_5).
\tag{1.1}
\]

The repaired packet has old and new shores (0.2). Its inverse has old
shore \(S_1\) and new shore \(S_0\).

### Lemma 1.1 (certified same-template source graph)

Within one fixed repaired template, the certified recharge source graph
is exactly

\[
                         S_0\longleftrightarrow S_1.
\tag{1.2}
\]

Repeated certified uses alternate and cancel.

#### Proof

The forward packet left-rotates the six \(P\)-rows and right-rotates
the six \(Q\)-rows:

\[
 {\bf p}\sqcup r{\bf q}
 \longmapsto
 r{\bf p}\sqcup{\bf q}.
\tag{1.3}
\]

The target is literally the inverse source. Applying the inverse
returns every row. No third source shore is part of the fixed repaired
template. \(\square\)

The point is not that another repaired template cannot use some of the
same physical rows. It is that doing so requires a new cycle/palette
interpretation and an exact source compatibility theorem not contained
in the repaired packet itself.

## 2. The open fifteen-top fusion

Choose one focal row \(w\) in the target shore \(S_1\).

### Step 1: twelve-top recharge

Apply

\[
                         S_0\longrightarrow S_1.
\tag{2.1}
\]

This preserves every protected trace, every position--label histogram,
and the exact middle-owner support.

### Step 2: one rectangle

Write the current focal word as

\[
                         w=(a,b,x,\ldots).
\tag{2.2}
\]

Choose a fresh label \(y\) outside its top, install the exact companion
word on

\[
                         V=U-\{x\}+\{y\},
\tag{2.3}
\]

and apply the two-top boundary rectangle. The focal word becomes
\(sw\), where \(s\) swaps its first two letters. The aggregate
derivative of this step is

\[
                         \Delta_h=0\quad(h\ne H),
 \qquad
                         \Delta_H=R.
\tag{2.4}
\]

### Step 3: one three-top reroot

Choose a remote label in \(sw\) and a fresh catalyst label. Apply the
three-top collar-neutral reroot with focal word \(sw\) and two fresh
companion tops. This has

\[
                         \Delta_h=0
 \qquad(0\le h\le2H)
\tag{2.5}
\]

and changes the focal boundary-swap trace.

### Theorem 2.1 (one-defect normal form)

The three steps above prove Theorem A. More precisely:

1. the twelve-top carrier contributes eleven exact rows of \(S_1\) at
   the endpoint;
2. the focal carrier top contains the rerooted version of \(sw\);
3. the rectangle companion and two reroot companions contain their
   respective target words; and
4. the only nonzero protected derivative is the middle rectangle
   \(R\).

#### Proof

Equations (2.1), (2.4), and (2.5) add to (0.3). Every step replaces one
literal word by one literal word on each touched top. Fresh auxiliary
tops make all top incidences distinct. The rectangle changes the focal
first-two state, and the reroot changes its position-three/remote
chart, so the focal endpoint is not its unchanged row in \(S_1\).
All other carrier rows are untouched after Step 1. \(\square\)

The macro is already chronological and bounded. Its failure is exactly
one Markov handoff defect on the twelve-top carrier, plus the three open
auxiliary target states.

## 3. Proof of the same-template no-go

For a table \(T\), write

\[
 {\cal D}(T)=
 \bigl({\cal D}_h(T)\bigr)_{0\le h\le2H}
\tag{3.1}
\]

for its complete protected deck vector.

The repaired theorem gives

\[
                         {\cal D}(S_0)={\cal D}(S_1).
\tag{3.2}
\]

Every three-top reroot has zero complete derivative. Every twelve-top
recharge has zero complete derivative. A two-top rectangle has zero
nonmiddle derivative and contributes its hypersimplex rectangle at the
middle.

### Theorem 3.1 (closed same-template handoff has zero payload)

Let a chronology start at \(S_\epsilon\) together with an external
helper table \(A\), and end at \(S_{\epsilon'}\) together with the same
external table \(A\). Then its total protected derivative is zero.

#### Proof

The endpoint derivative is

\[
 \begin{aligned}
 {\cal D}(S_{\epsilon'}\sqcup A)
 -
 {\cal D}(S_\epsilon\sqcup A)
 &=
 {\cal D}(S_{\epsilon'})
 -
 {\cal D}(S_\epsilon)\\
 &=0
 \end{aligned}
\tag{3.3}
\]

by (3.2). Endpoint subtraction is independent of the chosen
intermediate decomposition into moves. \(\square\)

### Corollary 3.2 (rectangle payload cancellation)

Under the hypotheses of Theorem 3.1, the signed sum of all middle
hypersimplex rectangles used by the chronology is zero.

#### Proof

The recharge and reroot moves have zero middle derivative. Thus the
middle component of (3.3) is exactly the sum of the rectangle
derivatives. \(\square\)

This proves Theorem B. Arbitrarily many intermediate moves and
arbitrarily complicated external catalysts do not help if they are all
restored and the carrier returns to a certified source of the same
template.

## 4. Why the obvious conjugation does not give a Markov macro

It is tempting to use

\[
                         S_0
 \xrightarrow{\ R_{12}\ }
                         S_1
 \xrightarrow{\ B\ }
                         B S_1
 \xrightarrow{\ R_{12}^{-1}\ ?\ }
                         B S_0.
\tag{4.1}
\]

The final arrow is not the inverse repaired packet. Its certified source
is \(S_1\), not \(BS_1\). Replacing it by a formally conjugated
exchange requires proving that \(BS_1\) and \(BS_0\) are two repaired,
squarefree shores with matched columns and compatible palettes. That is
a new twelve-top theorem.

Even if such a conjugated packet is supplied, the endpoint is
\(BS_0\), not a new translated source of the original template.
Repeating the same conjugation merely toggles the boundary involution.
It does not create a chain of distinct rectangle directions.

The three-top reroot fixes the trace defect but not this source defect:
it deliberately moves the focal row into a different rooted chart.
That is useful for direction rank and exactly why the resulting row is
not an \(S_0\) or \(S_1\) source row.

## 5. Necessary form of a successful handoff

Let \(\mathfrak T\) be the set of all repaired twelve-top source shores,
over all carriers, cores, cycle decompositions, palette colourings, and
filler matchings. Define the directed **source-handoff graph** whose
vertices are shores in \(\mathfrak T\), and whose edge

\[
                         S\longrightarrow S'
\tag{5.1}
\]

means that a bounded literal chronology of the present move library
starts at \(S\), ends at \(S'\) after restoring all noncarrier helpers,
and has one prescribed nonzero middle rectangle derivative.

### Proposition 5.1 (no loops or same-template edges)

The source-handoff graph has no loop and no edge between the two shores
of one repaired template.

#### Proof

Both cases satisfy the hypotheses of Theorem 3.1, so their endpoint
protected derivative is zero, contradicting the prescribed nonzero
rectangle. \(\square\)

Therefore any successful bounded Markov macro must be a genuinely
cross-template edge in (5.1).

All moves in the present library preserve top multiplicity separately
at every top. Since the noncarrier helpers are restored, one must first
have

\[
                         \mu_U(S)=\mu_U(S')
 \qquad\text{for every rank-\(M\) top }U.
\tag{5.2a}
\]

Thus the next template must use the same twelve physical tops, although
it may use a different cycle decomposition, palette chart, and word
assignment.

In fact its common core and six-label carrier are forced. For a repaired
carrier

\[
 \{C+e:e\in\tbinom S2\setminus J\},
\tag{5.2d}
\]

every outside label in \(S\) is absent from some carrier top, while
every label of \(C\) belongs to all twelve. Hence

\[
                         \bigcap_{U\text{ in the carrier}}U=C.
\tag{5.2e}
\]

Any other repaired template on the same top set therefore has the same
\((M-2)\)-core \(C\), the same six-set \(S\), and the same missing
perfect matching \(J\). Only its decomposition of
\(K_6-J\) into two six-cycles and its positional decorations can change.

The moves also preserve the complete rooted position--label histogram.
Hence a second necessary condition for (5.1) is

\[
                         C_{j,v}(S)=C_{j,v}(S')
 \qquad\text{for every }j,v.
\tag{5.2b}
\]

At the same time, its middle endpoint difference must equal the desired
rectangle:

\[
                         {\cal D}_H(S')-{\cal D}_H(S)=R.
\tag{5.2c}
\]

Equations (5.2a)--(5.2c), literal source membership in
\(\mathfrak T\), and chronological nonnegativity are the exact bounded
Markov handoff conditions.

The saturated Latin/seam lattice theorems prove signed generation in
the relevant marginal fibres. They do not prove that (5.1) has any
edge: induced long-cycle fibres show that bounded signed generators
need not be conformally applicable.

## 6. Independent audit

### 6.1 Endpoint argument

The no-go uses only equality of the complete endpoint deck vectors.
It does not assume that the intermediate recharge packets are
top-disjoint, that their palettes agree, or that their chronological
precedence is acyclic. Therefore there is no hidden locality hypothesis
in Theorem 3.1.

### 6.2 The open fusion ledger

The twelve-top step contributes zero at every length. The rectangle
contributes exactly \(R\) at \(h=H\) and zero elsewhere. The three-top
step contributes zero at every length. Thus (0.3) has no omitted
collar or histogram term.

### 6.3 Why a different template is not covered by the no-go

Two distinct repaired source shores may share the same position--label
histogram while having different seam and middle-owner decks. Endpoint
subtraction can then equal a nonzero rectangle without contradicting
(3.2). Theorem 3.1 deliberately does not rule out such a cross-template
handoff.

## 7. Exact boundary

Proved:

1. a bounded literal fusion of the repaired twelve-top recharge, one
   boundary rectangle, and one three-top reroot;
2. its exact one-rectangle middle payload and zero nonmiddle collateral;
3. the one-defect endpoint normal form;
4. impossibility of a nonzero rectangle payload in every closed
   same-template handoff;
5. failure of the obvious recharge conjugation; and
6. the exact top, column, and middle cross-template equations required
   of a successful bounded
   Markov macro.

Not proved:

1. a cross-template edge satisfying (5.2)--(5.3);
2. a bounded macro whose endpoint helper shore is a source for a
   different repaired packet;
3. a globally squarefree owner realization of a chain of such handoffs;
4. a universal bounded Markov-basis theorem; or
5. coefficient one.

The current deterministic gate has therefore narrowed to one literal
question: find two different repaired twelve-top source templates on
the same twelve physical tops and in the same rooted position--label
histogram fibre whose middle deck
difference is one installable hypersimplex rectangle, and order the
intervening moves without leaving the nonnegative source catalogue.
