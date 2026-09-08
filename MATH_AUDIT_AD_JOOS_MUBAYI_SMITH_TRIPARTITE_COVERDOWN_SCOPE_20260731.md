# Joos--Mubayi--Smith tripartite cover-down: exact scope and the planted-state obstruction

Date: 2026-07-31  
Status: primary-source theorem audit and exact contracted-macro forcing
lemma.  The proposed `C6` cleanup has a sound `P`-perfect encoding, but the
direct Boolean application is ruled out by the theorem's ambient-size
hypothesis.  No exact side factor or cover-down theorem is claimed.

## 0. Verdict

The tripartite theorem of Joos--Mubayi--Smith has exactly the **formal**
constant-uniformity shape suggested for the side host:

\[
  H_1:\quad 1P+3Q,\qquad H_2:\quad 1P+3R.              \tag{0.1}
\]

It also permits bounded mixed conflicts involving old and cleanup edges.
This does not make it a black box for the present Boolean cover-down.
There are two prior failures.

1. With host degree \(d=\Theta(n^2)\), the theorem requires

   \[
       |P\cup Q|\le \exp(d^{\varepsilon^3}),           \tag{0.2}
   \]

   whereas the Boolean side host has

   \[
       |P|={2n\choose n-2}=\exp(\Theta(n)).             \tag{0.3}
   \]

   The allowed \(\varepsilon\) is a fixed sufficiently small constant; in
   the proof it may be taken below \(1/(2(k-1))=1/6\) for the four-uniform
   first-stage host.  Hence
   \(d^{\varepsilon^3}=n^{2\varepsilon^3+o(1)}=o(n)\),
   contradicting (0.2).  Increasing `d` is impossible because the same
   theorem requires the first-stage minimum and maximum degrees to be
   asymptotic to `d`.

2. A selected suspended-hex cleanup is not literally an added atom.  If its
   off and on states are \(B^-_\gamma\) and \(B^+_\gamma\), it decodes as

   \[
        M\longmapsto (M\setminus B^-_\gamma)\cup B^+_\gamma,
        \qquad
        \operatorname{res}(B^+_\gamma)
        =\operatorname{res}(B^-_\gamma)\dot\cup
          \operatorname{res}(t_\gamma).                \tag{0.4}
   \]

   Thus \(B^-_\gamma\subseteq M\) is mandatory.  This condition **can** be
   encoded, because the final abstract matching is `P`-perfect: conflict the
   macro with every alternative cover of the two lower tokens belonging to
   its off atoms.  Selecting the macro then forces those two off atoms.
   This exact dynamic planting uses mixed conflicts with one and two cleanup
   edges; their boundedness is a new quantitative row, not a consequence of
   the formal local catalogue.

Even after repairing the scale row and verifying those conflicts, the theorem gives bounded-conflict
high girth, not an exact physical forest; it neither chooses a common basis
nor preserves a pointwise common cap.  Its stated cleanup bound is also much
larger than the desired Catalan-scale `O(P/n)` bank.

## 1. Primary-source statement

The source audited here is Felix Joos, Dhruv Mubayi and Zak Smith,
*Conflict-free Hypergraph Matchings and Coverings*, arXiv:2407.18144v2,
24 June 2026, Theorems 1.1 and 3.1 and Section 4.3:

<https://arxiv.org/html/2407.18144>.

The theorem fixes integers

\[
  \ell\ge2,\quad p\ge1,\quad q\ge0,\quad r\ge1,
  \quad p+q\ge2,                                      \tag{1.1}
\]

before taking \(d\to\infty\).  For sufficiently small fixed
\(\varepsilon>0\), there are disjoint vertex classes \(P,Q,R\), a
hypergraph \(H_1\) whose edges contain `p` vertices of `P` and `q` vertices
of `Q`, and a hypergraph \(H_2\) whose edges contain one vertex of `P` and
`r` vertices of `R`.  The size hypothesis is

\[
 d^\varepsilon\le |P|\le |P\cup Q|
                  \le \exp(d^{\varepsilon^3}).          \tag{1.2}
\]

The degree hypotheses are

\[
 (1-d^{-\varepsilon})d
   \le\delta_P(H_1)\le\Delta(H_1)\le d,                \tag{1.3}
\]

\[
 \Delta_2(H_1)\le d^{1-\varepsilon},                  \tag{1.4}
\]

\[
 \Delta_R(H_2)\le d^{\varepsilon^4}\delta_P(H_2),
 \qquad
 d_{H_2}(x,v)\le d^{-\varepsilon}\delta_P(H_2)         \tag{1.5}
\]

for \(x\in P,v\in R\).  Section 4.3 permits the weaker normalized form

\[
 \sum_{x\in P}{d_{H_2}(x,v)\over d_{H_2}(x)}
       \le d^{\varepsilon^4},
 \qquad
 d_{H_2}(x,v)\le d^{-\varepsilon}d_{H_2}(x).           \tag{1.6}
\]

The first-stage conflict hypergraph \(\mathcal C\) has conflict sizes in
`[2,ell]` and satisfies, for \(2\le j\le\ell\),

\[
 \Delta(\mathcal C^{(j)})\le\ell d^{j-1},
 \qquad
 \Delta_{j'}(\mathcal C^{(j)})
       \le d^{j-j'-\varepsilon}\quad(2\le j'<j),       \tag{1.7}
\]

together with the two special size-two spread bounds (C4)--(C5).

In the simpler published statement, every mixed conflict contains at least
two `H2` edges.  Section 4.3 also handles conflicts with exactly one `H2`
edge.  It weights a conflict \(E\) by

\[
       A(E)=\prod_{x\in V_P(E)}d_{H_2}(x)^{-1}          \tag{1.8}
\]

and imposes (E1)--(E6).  In particular, if a conflict consists of
\(j_1\) first-stage edges and one cleanup edge, then every fixed cleanup
edge lies in at most

\[
                         \ell d^{j_1}                  \tag{1.9}
\]

such conflicts, and the corresponding fixed-subset codegrees save a factor
\(d^\varepsilon\).  Thus literal `H1--H2` incompatibility pairs are in
scope only through this generalized form, not through the simpler
`D1--D4` statement.

Under all these hypotheses there is a `P`-perfect
\((\mathcal C\cup\mathcal D)\)-free matching in \(H_1\cup H_2\), and at
most

\[
                         d^{-\varepsilon^4}|P|          \tag{1.10}
\]

vertices of `P` are covered by cleanup edges from `H2`.

Two scope points are essential:

* `p,q,r,ell` are fixed.  The theorem does not allow growing atom size or
  conflicts of all cycle lengths.
* The conclusion is an ordinary hypergraph matching.  It contains no
  decoder which deletes previously selected `H1` edges.

## 2. The formal Boolean type map

Fix one common basis and one side.  Write `P_B` for the Catalan quantity
\({2n\choose n-2}\), reserving sans-serif \(\mathsf P,\mathsf Q,\mathsf R\)
for the Joos--Mubayi--Smith vertex classes.

Take

* \(\mathsf P\) to be the `P_B` allowed lower colours;
* \(\mathsf Q\) to be the rank-`n+2` upper colours together with the
  literal owner-slot resources; and
* \(H_1\) to be the ordinary fixed-four side atoms.

Then every `H1` edge has type

\[
                 1\mathsf P+3\mathsf Q,                \tag{2.1}
\]

so `p=1,q=3`.  The exact host ledger supplies

\[
 \Delta(H_1)\le D_0=2(n+1)(n+2),
 \qquad \Delta_2(H_1)\le2(n+1).                        \tag{2.2}
\]

Therefore the codegree exponent would be harmless for, say, any fixed
\(\varepsilon<1/2\).  Short physical cycles of bounded length also have
the required fixed-size conflict counts already used in the
Delcourt--Postle coloring argument.

For `H2`, contract a planted suspended-hex packet to its target lower
colour and three duplicated boundary resources.  Formally this has type

\[
                 1\mathsf P+3\mathsf R,                \tag{2.3}
\]

so `r=3`.  Thus there is no growing-uniformity problem in this proposed
atomization.

This type check is the full positive conclusion.  It does not check size,
minimum degree, planting, or physical decoding.

## 3. First theorem-hypothesis failure: ambient scale

The fixed side host satisfies

\[
 \log|\mathsf P|
 =\log{2n\choose n-2}=2n\log2+O(\log n).              \tag{3.1}
\]

Equations (1.3) and (2.2) force `d=Theta(n^2)` in any direct application:
`d` cannot be made superpolynomial because `H1` must simultaneously have
minimum degree `(1-o(1))d` and maximum degree at most `d`.  Hence

\[
 d^{\varepsilon^3}=n^{2\varepsilon^3+o(1)}.            \tag{3.2}
\]

For the four-uniform first-stage matching theorem, the proof chooses
\(\varepsilon_0<1/(2(k-1))=1/6\).  Thus every allowed
\(\varepsilon<\varepsilon_0\) has \(2\varepsilon^3<1\), and

\[
 d^{\varepsilon^3}=o(n)=o(\log|\mathsf P|).            \tag{3.3}
\]

This contradicts (1.2).

### Theorem 3.1 (direct black-box no-go)

The Joos--Mubayi--Smith tripartite theorem cannot be applied directly to
the full fixed-four Boolean side host with \(d=\Theta(n^2)\).

The same obstruction remains if \(\mathsf P\) is only a Catalan-scale
cleanup bank of order \(\Theta(P_B/n)\): its logarithm is still
\(\Theta(n)\), and the global upper/slot bank in \(\mathsf Q\) is still
exponential.  Applying the theorem to polynomial-size local blocks would
require a new cross-block compatibility and serialization theorem.

## 4. Second theorem-hypothesis gap: first-stage regularity

The arbitrary-common-basis forest theorem deliberately uses a coloring
form needing only maximum degree, global edge count and codegrees.  The
available fixed-`Q` ledger proves that all but an
`O(n^{-2/3})` fraction of host vertices are nearly regular, but it does not
prove the pointwise lower bound (1.3) for every lower colour.

This distinction cannot be repaired by the dummy regularization in the
Joos--Mubayi--Smith proof.  Their dummy edges regularize vertices on the
`Q` shore, whose coverage is irrelevant.  A dummy edge through a deficient
`P` vertex could be selected in the `P`-perfect matching and would have no
physical decode.

Thus, even with the ambient-size row deleted, an arbitrary synchronized
common basis does not currently satisfy the first-stage minimum-degree
hypothesis.  A specially chosen basis might do so, but the one-point
marginal theorem does not prove this uniform pointwise event.

## 5. Exact `P`-perfect forcing of the `C6` off state

For a suspended-hex packet \(\gamma\), let

\[
 B^-_\gamma=\{e_a,e_c\},\qquad
 B^+_\gamma=\{f_a,f_b,f_c\},                         \tag{5.1}
\]

and let \(t_\gamma=e_b\) be its target atom.  The exact identity is

\[
 \operatorname{res}(B^+_\gamma)
 =\operatorname{res}(B^-_\gamma)
    \dot\cup\operatorname{res}(t_\gamma).             \tag{5.2}
\]

Write the two off atoms as \(e_a,e_c\), and let their distinct lower
resources be \(p_a,p_c\).  For a cleanup edge \(h_\gamma\), introduce the
following forcing conflicts:

\[
 \{h_\gamma,g\}\quad
 \text{for every }g\ne e_a\text{ covering }p_a,
 \qquad
 \{h_\gamma,g\}\quad
 \text{for every }g\ne e_c\text{ covering }p_c.        \tag{5.3}
\]

Here `g` ranges over both `H1` edges and other `H2` edges.  Thus the first
family contains mixed conflicts of type `(j1,j2)=(1,1)`, while the second
possibility also creates conflicts of type `(0,2)`.

### Lemma 5.1 (`P`-perfect dynamic planting)

In every `P`-perfect matching containing \(h_\gamma\) and avoiding (5.3),
both \(e_a\) and \(e_c\) are selected.  Hence the replacement (5.2) is
literal.

#### Proof

The lower token \(p_a\) must be covered exactly once.  Every edge covering
it other than \(e_a\) conflicts with \(h_\gamma\), whereas \(e_a\) is
compatible with the local packet.  Therefore \(e_a\) is selected.  The same
argument at \(p_c\) forces \(e_c\).  Equation (5.2) then makes the physical
replacement literal. `square`

The hereditary objection applies to arbitrary conflict-free sets, but not
to their nonhereditary `P`-perfect subfamily.  Thus no preselected off-state
matching is logically necessary.  What is necessary is that the forcing
conflicts (5.3) satisfy the Joos--Mubayi--Smith mixed-boundedness rows and
that the forced atoms remain legal after fixing the common basis and
guards.

There are two possible meanings of “three duplicate `R` resources.”

1. If they are merely one literal copy of the target upper colour and its
   two slots, all absorber embeddings through the same target atom collapse
   to one simple `H2` edge.  The macro identity and its two forced off atoms
   are not determined, so neither (5.3) nor the decoder is well-defined.
2. If they are indexed by the absorber embedding, the formal `H2` degree
   can be large and private `R` tokens make (1.6) easy.  But `R`-matching
   then records no actual upper or slot collision.  Every such collision
   must be reintroduced through mixed conflicts.  This is the sound
   ordinary-hypergraph encoding.

For a fixed macro \(h_\gamma\), the `H1` alternatives in (5.3) number at
most twice the maximum first-stage degree, namely `O(d)`.  Thus they have
exactly the order permitted by (E5),

\[
       \Delta_{0,1}(\mathcal D^{(1,1)}_x)\le\ell d,      \tag{5.4}
\]

provided the constant and the fixed-subset (E6) rows are checked.  The
alternative `H2` covers of \(p_a,p_c\) are `(0,2)` conflicts.  Their raw
number may be large, but (E2)--(E4) use the normalized unavoidability
weights \(d_{H_2}(p)^{-1}\).  Verifying these weighted rows for the
embedding-indexed catalogue is the precise remaining local black-box
audit; the local absorber count alone does not verify them.

The exact count \(2n(n-2)=\Theta(d)\) is per **formal target atom**, before
fixing the common basis or the protected cap.  A lower colour has
\(\Theta(d)\) possible boundary atoms, so the embedding-indexed `H2` menu
may contain \(\Theta(d^2)\) macros.  This is ample for the relative
`P--R` codegree row in principle.  It does not by itself show that the two
forced off atoms survive puncturing and every protected guard, or that the
weighted mixed-conflict rows hold.

The local transversal and cap obstructions make the issue literal: all
formal embeddings through one target can be blocked by protected owner
slots, and every orientation changes its pointwise cap assignment.

## 6. A correct conditional contracted-macro interface

The following is the exact way the tripartite architecture could be used
after a scale theorem and mixed-boundedness audit.

### Proposition 6.1 (conditional contraction decoder)

Let \(\Gamma_0\) be a family of suspended-hex packets.  Give each packet an
embedding-labelled `H2` edge.  Add (5.3), conflicts forbidding a selected
packet from colliding with any retained `H1` atom outside its off state,
and conflicts forbidding two selected packets from overlapping in off or on
support.

If an abstract `P`-perfect matching \(M_1\cup M_2\) is found in this
system, then

\[
 F= M_1
       \setminus\bigcup_{\gamma\in M_2}B^-_\gamma
       \ \cup\bigcup_{\gamma\in M_2}B^+_\gamma          \tag{6.1}
\]

is a literal side matching covering every lower target exactly once.
Moreover its resource multiset is obtained from that of `M1` by adding
exactly the target atoms represented by `M2`.

#### Proof

Lemma 5.1 makes every deletion in (6.1) legal.  The remaining conflicts make
the deletions and additions pairwise compatible and disjoint from the
retained body.  Apply (5.2) independently to every selected packet.  The
abstract matching covers each target lower resource exactly once, so the
resulting literal matching does too. `square`

This proposition preserves literal slots and a local forest whenever the
full off/on supports were guarded accordingly.  It does **not** prove that
the union is globally acyclic or rooted.  Those are additional conditions
on the selected packet family and the retained scaffold.

For \(\mathsf P=\) all lower resources, (5.3) dynamically forces the off
states inside the first-stage body.  For a sparse designated target bank,
the same forcing works only if the two auxiliary lower tokens are also
included in the `P`-perfect ground or are precovered by a separately frozen
body.  The ambient bound (3.3) remains false in either Catalan-scale model.

## 7. Remaining conflict and topology rows

Assume hypothetically that Sections 3--5 have been repaired.

* A direct `H1--H2` upper/slot incompatibility is a mixed conflict with
  `j2=1`; it must satisfy the stronger (E5)--(E6) rows.  Constant packet
  support makes the coarse `O(d)` bound plausible, but no complete
  normalized census has been proved for the embedding-indexed catalogue.
* `H2--H2` physical collisions have `j2=2` and require the weighted
  (E2)--(E4) rows.  Private duplicate `R` tokens do not verify these actual
  conflicts.
* Bounded physical-cycle conflicts fit only for fixed `ell`.  The theorem
  may give a `P`-perfect high-girth degree-two graph, but it cannot forbid
  cycles of unbounded length.  Deleting one edge per long cycle destroys
  the `P`-perfect conclusion and reopens palette resources.  This is exactly
  why the existing Delcourt--Postle argument stops at a `P-o(P)` forest.
* Fixing a common basis before applying a theorem is logically allowed, but
  the required degree and planted-menu hypotheses have not been proved
  uniformly for arbitrary bases.  One-point marginals only control the
  aggregate loss of a prepacked atlas.
* Literal slots enforce ordinary degree capacities.  The suspended hex
  preserves its six slots across the full two phases, but it changes every
  edited pointwise cap assignment.  Protected-cap and compiler guards may
  therefore remove the whole menu unless audited jointly.
* Root/no-empty and contracted-graphic acyclicity are global acceptance
  rows, not consequences of ordinary hypergraph matching.

Finally, (1.10) is not the desired two-scale metric.  With
`d=Theta(n^2)`, it is

\[
 d^{-\varepsilon^4}|P|
       =|P|n^{-2\varepsilon^4+o(1)},                   \tag{7.1}
\]

which is asymptotically much larger than \(|P|/n\) for the allowed small
`epsilon`.  The theorem does not preserve an independently obtained
`O(P/n)` leave or make that leave packet-aligned.

## 8. Sharp boundary

The Joos--Mubayi--Smith result validates the **shape** of a two-family
fixed-uniformity model and supplies a useful checklist for a future local
cover-down theorem.  It does not presently bridge the metric obstruction.
The first false black-box hypothesis is the exponential Boolean ambient
size at polynomial degree.  The apparent semantic obstacle is repairable:
`P`-perfectness plus the forcing conflicts (5.3) dynamically plants the off
state.  The unresolved semantic hypotheses are instead the boundedness of
all those forcing/collision conflicts and survival of the forced atoms under
the common-basis, cap and graphic guards.

A viable replacement must therefore prove one of the following genuinely
new statements:

1. a Boolean-specific tripartite covering theorem with no
   \(\exp(d^{\varepsilon^3})\) ambient restriction, together with an audit
   of the dynamic off-state forcing conflicts;
2. a decomposition into small JMS-admissible blocks with exact cross-block
   palette, slot, graphic and root serialization; or
3. the proposed two-scale theorem directly: prepack a constant-support
   off-state atlas, choose the common basis and body jointly so only
   `O(P/n)` aligned defects remain, then finish them with the existing
   private `Theta(n)` circuits.

None of these follows from arXiv:2407.18144 alone.
