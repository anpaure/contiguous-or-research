# Balanced pruning of a sparse bad-overlap graph

Date: 2026-07-25

Method: pure mathematics only.

## 0. Purpose

For the return-free geodesic catalogue, call two candidate chunks **bad**
when their full two-chain grids share a prescribed forbidden rectangle.
The point of this note is to separate two issues which had been mixed:

1. deleting all bad pairs while retaining useful degree in the tag and
   target fibres;
2. proving a matching theorem in the retained catalogue.

The first issue has the following elementary weighted solution.  It does
not prove the second issue, and therefore does not prove coefficient one.

## 1. Abstract pruning theorem

Let \(\mathcal C\) be a finite catalogue and let \(B\) be a graph on
\(\mathcal C\), of maximum degree at most \(\Delta\).  Let
\(\mathscr F\) be any finite family of nonempty subsets of \(\mathcal C\),
called fibres.  Give every fibre \(F\) a nonnegative weight \(w_F\), and
suppose

\[
 |F|\ge d\qquad(F\in\mathscr F).
 \tag{1.1}
\]

### Theorem 1.1 (weighted balanced independent pruning)

Let \(L\ge8\), put

\[
 p={1\over L(\Delta+1)},
 \qquad
 \mu_F=p|F|,
 \tag{1.2}
\]

and define

\[
 \varepsilon=
 \exp\!\left(-{pd\over8}\right)+{4\over L}.
 \tag{1.3}
\]

There is an independent set \(\mathcal I\) in \(B\) for which

\[
 \boxed{
 \sum_{F:\ |\mathcal I\cap F|<\mu_F/4}w_F
 \le
 \varepsilon\sum_{F\in\mathscr F}w_F.}
 \tag{1.4}
\]

Thus, outside a set of fibres of weighted proportion at most
\(\varepsilon\), the pruned degree satisfies

\[
 \boxed{
 |\mathcal I\cap F|
 \ge { |F|\over4L(\Delta+1)}.}
 \tag{1.5}
\]

#### Proof

Mark every \(P\in\mathcal C\) independently with probability \(p\).
Retain a marked vertex precisely when none of its neighbours in \(B\) is
marked.  The retained family \(\mathcal I\) is independent.

Fix a fibre \(F\).  Let \(Y_F\) be the number of marked members of \(F\),
and let \(Z_F\) be the number of marked members of \(F\) which are deleted.
Then

\[
 Y_F\sim {\rm Bin}(|F|,p),
 \qquad \mathbb EY_F=\mu_F,
\]

so the Chernoff bound gives

\[
 \Pr(Y_F<\mu_F/2)\le e^{-\mu_F/8}.
 \tag{1.6}
\]

For a fixed \(P\in F\), the probability that \(P\) is marked and has a
marked neighbour is at most

\[
 p^2\deg_B(P)\le p^2\Delta.
\]

Consequently

\[
 \mathbb EZ_F
 \le |F|p^2\Delta
 =\mu_F p\Delta
 \le {\mu_F\over L}.
 \tag{1.7}
\]

Markov's inequality gives

\[
 \Pr(Z_F>\mu_F/4)\le {4\over L}.
 \tag{1.8}
\]

If neither exceptional event in (1.6) and (1.8) occurs, then

\[
 |\mathcal I\cap F|=Y_F-Z_F\ge\mu_F/4.
\]

Because \(\mu_F\ge pd\), the probability that \(F\) is bad is at most
\(\varepsilon\).  Hence the expected left side of (1.4) is at most its
right side.  Some marking outcome satisfies (1.4). \(\square\)

### Corollary 1.2 (relative-degree pruning)

In the setting of Theorem 1.1, fix \(0<\delta\le1\).  There is an
independent set \({\cal I}\) for which

\[
 \sum_{F:\ ||{\cal I}\cap F|-p|F||>\delta p|F|}w_F
 \le
 \left[
 2e^{-\delta^2pd/12}+{2\over L\delta}
 \right]
 \sum_Fw_F.
 \tag{1.9}
\]

#### Proof

Use the same marked count \(Y_F\) and deletion count \(Z_F\).  Chernoff
gives

\[
 \Pr(|Y_F-\mu_F|>\delta\mu_F/2)
 \le2e^{-\delta^2\mu_F/12},
\]

while (1.7) and Markov give

\[
 \Pr(Z_F>\delta\mu_F/2)\le {2\over L\delta}.
\]

Outside these events,

\[
 \bigl||{\cal I}\cap F|-\mu_F\bigr|
 \le|Y_F-\mu_F|+Z_F\le\delta\mu_F.
\]

Average the weighted exceptional indicator and fix one outcome. \(\square\)

## 2. A form adapted to tag and flag fibres

Suppose now that the fibres are divided into strata

\[
 \mathscr F=\mathscr F_{\rm tag}
 \dot\cup\mathscr F_{1,-}\dot\cup\mathscr F_{1,+}
 \dot\cup\cdots\dot\cup
 \mathscr F_{Q,-}\dot\cup\mathscr F_{Q,+}.
\]

Weights may be chosen so that a bad tag fibre costs one carrier tag and a
bad signed-target fibre costs one scalar repair.  Theorem 1.1 allows these
two ledgers to be handled in one experiment; no union bound over the
exponentially many fibres is needed.

### Corollary 2.1 (coefficient-scale exceptional ledger)

Assume the total weight of all controlled fibres is at most \(CQW\), and
choose \(L=L_m\) so that

\[
 {L\over Q}\longrightarrow\infty,
 \qquad
 {d\over 8L(\Delta+1)}-\log Q\longrightarrow\infty.
 \tag{2.1}
\]

Then there is a bad-pair-free subcatalogue for which

\[
 \sum_{F:\ |\mathcal I\cap F|<|F|/[4L(\Delta+1)]}w_F=o(W).
 \tag{2.2}
\]

#### Proof

The second hypothesis in (2.1) makes the exponential term in (1.3)
\(o(1/Q)\).
The first hypothesis gives \(4/L=o(1/Q)\).  Therefore
\(\varepsilon=o(1/Q)\), and (1.4) is \(o(W)\). \(\square\)

It is often convenient to state the hypotheses through the relative bad
degree

\[
 \xi={\Delta+1\over d}.
\]

Then the retained degree is at least \(1/(4L\xi)\) in every good fibre,
and (2.1) asks for

\[
 L/Q\to\infty,
 \qquad {1\over 8L\xi}-\log Q\to\infty.
 \tag{2.3}
\]

Thus any superpolynomially small rectangle-conflict ratio leaves enormous
room: one may take, for example, \(L=Q\log m\), provided
\(Q\log m\log Q\,\xi=o(1)\).

## 3. What this proves and what it does not

If an exact census proves

\[
 {\Delta_{\square(s)}+1\over d}
 =o\!\left({1\over Q^2\log m}\right),
 \tag{3.1}
\]

then Theorem 1.1 with \(L=Q\log m\) deletes every shared compressed
\(s\times s\) rectangle while losing only \(o(W)\) weighted tag/target
fibres, and every surviving good fibre still has degree tending to
infinity.

For a length-\(g\) chunk, a tag fibre must be assigned weight \(g\), not
weight one: losing that tag loses \(g\) physical middle owners.  Protected
target fibres have weight one.  Their total weighted mass is \(O(QW)\),
so the conclusion remains coefficient-safe.  The concrete protected-strip
three-antichain application, including the exact ratio
\(m^{-3+o(1)}\), is recorded in
`PROTECTED_STRIP_WIDTH_TWO_PRUNING_AND_DUAL_GATE_20260725.md`.

This is only a **catalogue pruning theorem**.  Three further statements
would still be required for coefficient one:

1. an exact upper bound such as (3.1) for the geodesic grid orbit;
2. a summable census of the intersection shapes left after rectangle
   pruning;
3. hereditary propagation of the resulting degrees and links through
   \(O(m)\) owner-scale matching bites.

The theorem removes the concern that an exponentially large number of
fibres forces a uniform union bound.  Weighted exceptional mass, which is
the quantity appearing in the literal repair ledger, is enough.
