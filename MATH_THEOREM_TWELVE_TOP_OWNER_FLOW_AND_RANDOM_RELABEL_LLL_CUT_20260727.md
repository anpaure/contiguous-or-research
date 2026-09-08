# Twelve-top owner flow: the exact unbundled factor and the random-relabel LLL cut

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\]

and

\[
 N=\binom{2m}{M},\qquad W=\binom{2m}{m},\qquad
 a=\binom M m,\qquad b=\binom mH.
\]

Then

\[
                         \lambda:=\frac ab=\frac WN.       \tag{0.1}
\]

Assume the calibrated regime used by the twelve-top construction:

\[
             d\le\lambda,\qquad dN=(1-o(1))W.              \tag{0.2}
\]

The conclusions are as follows.

1. **The unbundled owner problem has an exact integral solution.** For
   every set \(\mathcal A\subseteq\binom{[2m]}M\), one can give every
   \(U\in\mathcal A\) exactly \(d\) distinct rank-\(m\) owners contained
   in \(U\), with no owner used twice. This holds for every layer
   separately and hence for any prescribed number of layers.

2. This factor theorem does not lift automatically to repaired
   twelve-top packets. For each packet, the twelve assigned \(d\)-sets
   must be the twelve punctured cyclic decks of one common repaired
   decoration. In particular every one-top deck must be a Johnson tight
   path, while all twelve paths must share the common core, the two
   six-cycles, the proper palette colouring, and the filler-column
   matching. This is a colored hypergraph groupability condition, not a
   bipartite Hall condition.

3. Independent random relabeling is quantitatively on the wrong scale.
   Let one near-perfect layer contain \(s\) repaired packets, each using
   \(k=12d\) distinct owners, so

   \[
                            K=ks=(1-o(1))W.                 \tag{0.3}
   \]

   Relabel different packets independently. If

   \[
     \epsilon:=\max_{P,X}\Pr(X\text{ occurs in packet }P)=o(1),          \tag{0.4}
   \]

   then the expected owner pair-collision mass is at least

   \[
                         \left(\frac12-o(1)\right)W,        \tag{0.5}
   \]

   and the expected repeat excess is at least

   \[
                         \left(e^{-1}-o(1)\right)W.         \tag{0.6}
   \]

   The natural uniform core relabeling of a repaired packet satisfies

   \[
        \epsilon\le
        \frac{12d}{\binom{M-2}{H-1}}=o(1).                 \tag{0.7}
   \]

   Thus (0.5)--(0.6) apply to the actual repaired candidate family, not
   merely to arbitrary random owner sets.

4. The atomic owner-equality events do not satisfy the standard
   asymmetric Lovasz local lemma. For one packet, all equality events
   involving it form a dependency clique; averaged over packets, the
   sum of the event probabilities in this clique is at least

   \[
                              (1-o(1))k=\Theta(m).           \tag{0.8}
   \]

   Any asymmetric-LLL witness on a clique forces that sum to be at most
   one. Hence the canonical independent-relabel/LLL route is formally
   unavailable.

5. Over \(L=\Theta(m)\) near-perfect layers, independent packet
   relabeling has expected aggregate repeat excess \(\Omega(mW)\), not
   \(o(W)\). Linearity of expectation makes this conclusion independent
   of whether the random choices in different layers are coupled.

The deterministic boundary is therefore exact. Owner capacity and its
integral bipartite rounding are solved. The remaining theorem is a
**correlated rainbow factor of legal twelve-top decks**, followed by
literal chronological compatibility between consecutive layers. The
random calculation does not disprove such a factor; it proves that it
must be a global capacity-balancing object rather than an independent
relabeling corrected by the usual local lemma.

## 1. The containment graph

Let

\[
 \mathcal U=\binom{[2m]}M,\qquad
 \mathcal X=\binom{[2m]}m,
\]

and join \(U\in\mathcal U\) to \(X\in\mathcal X\) when \(X\subseteq U\).
Every top has degree

\[
                         a=\binom M m=\binom MH,             \tag{1.1}
\]

and every owner has degree

\[
                         b=\binom mH.                       \tag{1.2}
\]

Indeed a top contains \(a\) rank-\(m\) subsets, while an owner is
extended to an \(M\)-top by choosing \(H\) of the remaining \(m\)
coordinates. Double-counting all incidences gives \(Na=Wb\), which is
(0.1).

### Theorem 1.1 (exact unbundled owner factor)

Suppose \(d\le\lambda\). For every
\(\mathcal A\subseteq\mathcal U\), there are sets

\[
                 D_U\subseteq\{X\in\mathcal X:X\subseteq U\},
                 \qquad |D_U|=d,                            \tag{1.3}
\]

such that the \(D_U\), \(U\in\mathcal A\), are pairwise disjoint.

#### Proof

Replace every \(U\in\mathcal A\) by \(d\) left clones, all with the
same owner neighbourhood. Let \(S\) be any set of clones, and let
\(B\subseteq\mathcal A\) be the set of underlying tops represented in
\(S\). Then

\[
                              |S|\le d|B|.                  \tag{1.4}
\]

Write \(\Gamma(B)\) for the owners contained in at least one top of
\(B\). Count containment incidences from \(B\) into \(\Gamma(B)\).
The left count is exactly \(a|B|\), and every owner receives at most
\(b\) such incidences. Hence

\[
       a|B|\le b|\Gamma(B)|,
       \qquad
       |\Gamma(B)|\ge\lambda|B|\ge d|B|\ge|S|.             \tag{1.5}
\]

Thus every clone set satisfies Hall's inequality. A matching saturating
all clones gives (1.3). \(\square\)

### Corollary 1.2 (near-perfect layers)

If \(|\mathcal A|=N-r\), the assignment covers exactly \(d(N-r)\)
owners and leaves

\[
                         W-dN+dr                            \tag{1.6}
\]

owners unused. Hence a layer with \(r=o(N)\) has \(o(W)\) unused
owners under (0.2).

For prescribed layers \(\mathcal A_1,\ldots,\mathcal A_L\), apply
Theorem 1.1 to the disjoint right copies
\(\{\ell\}\times\mathcal X\). This gives one simultaneous integral
flow with no owner repeated inside any layer. An owner may of course be
used once in each of several layers; that is temporal reuse, not a
same-layer collision.

## 2. The exact packet-deck lift that Hall does not supply

Let \(P\) be one top packet from the repaired twelve-top theorem. Its
top set has the form

\[
 \mathcal U(P)=
 \{C\cup e:e\in\tbinom S2\setminus J\},                   \tag{2.1}
\]

where \(|C|=M-2\), \(|S|=6\), and \(J\) is a perfect matching on
\(S\). Let \(\Sigma(P)\) be the set of all legal repaired decorations:
the choice of the two six-cycles, their proper palette colours, ordered
palettes, filler-column factorization, root phases, and all allowed
relabelings. A decoration \(\sigma\in\Sigma(P)\) has a squarefree
owner deck

\[
                \mathcal O(P,\sigma)\subseteq\mathcal X,
                \qquad |\mathcal O(P,\sigma)|=12d.         \tag{2.2}
\]

The two shores of the repaired exchange have this same support.

Theorem 1.1 permits an arbitrary \(d\)-set \(D_U\) below every top.
A legal lift instead requires

\[
       \boxed{
       \bigcup_{U\in\mathcal U(P)}D_U
                  =\mathcal O(P,\sigma_P)
       \quad\text{for one }\sigma_P\in\Sigma(P)}           \tag{2.3}
\]

for every packet \(P\), simultaneously.

Even the one-top projection of (2.3) is restrictive. Its \(d\) owners
can be ordered \(X_1,\ldots,X_d\) so that

\[
                         |X_i\triangle X_{i+1}|=2           \tag{2.4}

\]

and they are consecutive surviving phases of one cyclic rank-\(m\)
window deck after a block of \(4H-1\) phases is removed. Across the
twelve tops, the orders in (2.4) are coupled by the same \(C\), the two
carrier cycles, the palette chart, and the column equalities
\(P_j=Q_j\). None of these conditions appears in (1.5).

For a packet layer \(\mathcal P\), define the multipartite deck
hypergraph whose part at \(P\) is

\[
                         \mathscr D(P)=
             \{\mathcal O(P,\sigma):\sigma\in\Sigma(P)\}.  \tag{2.5}

\]

A collision-free repaired layer is exactly a rainbow matching choosing
one \(12d\)-edge from every part. Thus the smallest static missing
statement is

\[
 \boxed{
 \text{Every near-perfect top-packet layer admits a rainbow matching
 in the deck hypergraph (2.5), up to }o(W)\text{ owner mass}.}             \tag{2.6}

\]

Chronology imposes one further condition: on a top reused in the next
layer, the target word selected in the first packet must literally be
the source word selected in the next. This word-state handoff is not
encoded by (2.6).

## 3. Exact collision identities for random packet relabeling

Fix one layer \(\mathcal P\). Independently for each packet \(P\),
choose a random \(\sigma_P\in\Sigma(P)\), under any prescribed
distribution. Put

\[
 p_{P,X}=\Pr(X\in\mathcal O(P,\sigma_P)),\qquad
 \mu_X=\sum_{P\in\mathcal P}p_{P,X}.                       \tag{3.1}
\]

Let

\[
 L_X=|\{P:X\in\mathcal O(P,\sigma_P)\}|                   \tag{3.2}
\]

be the resulting owner load. Since each packet deck is squarefree,
\(L_X\) is a sum of independent Bernoulli variables with parameters
\((p_{P,X})_P\). Moreover

\[
 \sum_X\mu_X=\sum_{P,X}p_{P,X}=12d|\mathcal P|=K.          \tag{3.3}
\]

Define the pair-collision mass and repeat excess by

\[
 C_2=\sum_X\binom{L_X}{2},\qquad
 R=\sum_X(L_X-1)_+.                                       \tag{3.4}
\]

### Theorem 3.1 (exact annealed collision formulae)

One has

\[
 \boxed{
 \mathbb EC_2=\frac12\sum_X
       \left(\mu_X^2-\sum_Pp_{P,X}^2\right)}              \tag{3.5}
\]

and

\[
 \boxed{
 \mathbb ER=\sum_X\left(
       \mu_X-1+\prod_P(1-p_{P,X})\right).}                \tag{3.6}
\]

#### Proof

For (3.5), expand

\[
 \mathbb E\binom{L_X}{2}
   =\sum_{P<Q}\Pr(X\in\mathcal O(P),X\in\mathcal O(Q))
   =\sum_{P<Q}p_{P,X}p_{Q,X},                              \tag{3.7}
\]

using independence of different packet relabelings. This is half the
difference displayed in (3.5).

For an integer \(r\ge0\), \((r-1)_+=r-\mathbf1_{\{r\ge1\}}\). Hence

\[
 \mathbb E(L_X-1)_+
 =\mu_X-\Pr(L_X\ge1)
 =\mu_X-1+\Pr(L_X=0).                                     \tag{3.8}
\]

Independence gives
\(\Pr(L_X=0)=\prod_P(1-p_{P,X})\), proving (3.6). \(\square\)

### Theorem 3.2 (diffuse critical relabeling has linear repeats)

Suppose

\[
 K=\alpha W,\qquad \alpha=1-o(1),\qquad
 \epsilon=\max_{P,X}p_{P,X}=o(1).                         \tag{3.9}
\]

Then

\[
 \mathbb EC_2\ge
 \frac W2(\alpha^2-\epsilon\alpha)
       =\left(\frac12-o(1)\right)W,                       \tag{3.10}
\]

and

\[
 \mathbb ER\ge W\left[
     \alpha-1+\exp\left(-\frac{\alpha}{1-\epsilon}\right)
     \right]
       =\left(e^{-1}-o(1)\right)W.                        \tag{3.11}
\]

#### Proof

By Cauchy--Schwarz and (3.3),

\[
                         \sum_X\mu_X^2\ge\frac{K^2}{W}.   \tag{3.12}
\]

Also

\[
                     \sum_{P,X}p_{P,X}^2\le\epsilon K.    \tag{3.13}
\]

Substitution into (3.5) proves (3.10).

For \(0\le p\le\epsilon<1\),

\[
              \log(1-p)\ge-\frac p{1-p}
                            \ge-\frac p{1-\epsilon}.       \tag{3.14}
\]

Therefore

\[
              \prod_P(1-p_{P,X})
              \ge\exp\left(-\frac{\mu_X}{1-\epsilon}\right).           \tag{3.15}
\]

The function

\[
                       g(u)=u-1+e^{-u/(1-\epsilon)}         \tag{3.16}
\]

is convex. Jensen's inequality, (3.3), and (3.6) give

\[
 \mathbb ER\ge\sum_Xg(\mu_X)
              \ge Wg(K/W),                                \tag{3.17}
\]

which is (3.11). \(\square\)

## 4. The natural repaired relabeling is diffuse

Fix a repaired packet top set (2.1) and one legal repaired decoration.
Apply a uniformly random permutation of its common core \(C\) to the
entire decoration. This simultaneously relabels all palettes and all
filler entries, so it remains a legal repaired decoration.

### Lemma 4.1 (maximum owner probability)

For this distribution,

\[
                \max_X\Pr(X\in\mathcal O(P,\sigma))
       \le\frac{12d}{\binom{M-2}{H-1}}.                   \tag{4.1}
\]

Under \(H\ge3\) and \(M\ge18H-10\), the right side is \(O(1/m)\),
hence \(o(1)\).

#### Proof

Every one of the \(12d\) owner occurrences belongs to a top
\(C\cup e\), where \(|e|=2\). In the protected path, an \(H\)-deletion
window meets at most one of the two outside placeholders. Hence its
rank-\(m\) owner retains either both elements of \(e\), with a core
part of size \(m-2\), or one element of \(e\), with a core part of size
\(m-1\).

Under a uniform permutation of \(C\), the image of a fixed core part is
uniform among all subsets of the same size. Thus the probability that
one fixed occurrence equals one prescribed owner is either zero or

\[
       \binom{M-2}{m-2}^{-1}=\binom{M-2}{H}^{-1},
       \quad\text{or}\quad
       \binom{M-2}{m-1}^{-1}=\binom{M-2}{H-1}^{-1}.         \tag{4.2}
\]

The second denominator is the smaller one. A union bound over the
\(12d\) occurrences proves (4.1). Since
\(2\le H-1\le(M-2)/2\),

\[
        \binom{M-2}{H-1}\ge\binom{M-2}{2}=\Theta(m^2),     \tag{4.3}
\]

whereas \(d=O(m)\). \(\square\)

Combining Lemma 4.1 with Theorem 3.2 proves (0.5)--(0.7).

### Exact unbundled random benchmark

For comparison, suppose every top independently chooses a uniformly
relabelled \(d\)-deck, without the twelve-top coupling. A fixed contained
owner is selected with probability \(d/a\), and every owner lies below
exactly \(b\) tops. On the full top layer, (3.5)--(3.6) become the exact
closed formulae

\[
 \mathbb EC_2
   =W\binom b2\left(\frac da\right)^2
   =\frac W2\left(\frac d\lambda\right)^2
      \left(1-\frac1b\right),                             \tag{4.4}
\]

and

\[
 \mathbb ER
   =W\left[
       \frac d\lambda-1+\left(1-\frac da\right)^b
       \right].                                           \tag{4.5}
\]

At the critical calibration, (4.4) is
\((1/2-o(1))W\) and (4.5) is \((e^{-1}-o(1))W\). Thus the
constants in Theorem 3.2 are the natural critical occupancy constants.

## 5. The canonical LLL condition fails

For distinct packets \(P,Q\) in one layer and an owner \(X\), let

\[
 A_{P,Q,X}=
 \{X\in\mathcal O(P,\sigma_P)\cap\mathcal O(Q,\sigma_Q)\}.               \tag{5.1}
\]

Its probability is

\[
                         \Pr(A_{P,Q,X})=p_{P,X}p_{Q,X}.     \tag{5.2}
\]

Use the standard variable-dependency graph: two events are adjacent if
they share one packet-relabel variable. For fixed \(P\), all events
involving \(P\) form a clique \(\mathcal C_P\). Put

\[
 S_P=\sum_{Q\ne P}\sum_Xp_{P,X}p_{Q,X}.                  \tag{5.3}
\]

By (3.5),

\[
                         \sum_PS_P=2\mathbb EC_2.           \tag{5.4}
\]

There are \(s=K/k=(1-o(1))W/k\) packets. Theorem 3.2 therefore gives

\[
                \frac1s\sum_PS_P
                =\frac{2\mathbb EC_2}{s}
                \ge(1-o(1))k.                             \tag{5.5}
\]

In particular some packet-star clique has probability sum greater than
one.

### Lemma 5.1 (clique inequality for asymmetric LLL witnesses)

If events in a clique \(\mathcal C\) admit standard asymmetric-LLL
witnesses \(0\le x_A<1\), then

\[
                            \sum_{A\in\mathcal C}\Pr(A)\le1.             \tag{5.6}
\]

#### Proof

The asymmetric criterion gives

\[
 \Pr(A)\le x_A\prod_{B\sim A}(1-x_B)
          \le x_A\prod_{\substack{B\in\mathcal C\\B\ne A}}(1-x_B).
                                                                    \tag{5.7}
\]

Summing (5.7) over \(A\in\mathcal C\), the right side is the
probability that exactly one of a family of independent Bernoulli
variables with success probabilities \((x_A)_{A\in\mathcal C}\) is
one. It is at most one. \(\square\)

Equations (5.5)--(5.6) prove that the atomic owner-equality events do
not admit the standard asymmetric LLL. This statement is deliberately
scoped. It does not exclude a nonproduct distribution, a capacity-star
resampling oracle, or a deterministic alternating-cycle construction.
It proves that such a method must exploit the global negative dependence
which is present in Theorem 1.1 and absent from independent packet
relabeling.

## 6. Several layers and the exact remaining theorem

Let \(\mathcal P_1,\ldots,\mathcal P_L\) be near-perfect repaired
packet layers, with \(L=\Theta(m)\). Apply the random experiment of
Sections 3--4 within each layer. The random choices between different
layers may be independent or arbitrarily coupled. Linearity of
expectation and (3.11) give

\[
 \mathbb E\sum_{\ell=1}^LR_\ell
       \ge(e^{-1}-o(1))LW=\Omega(mW).                      \tag{6.1}
\]

Thus random relabeling is separated from the required \(o(W)\) total
collision loss by a factor of order \(m\).

The exact static replacement lemma is:

> **Correlated repaired-deck factor (unproved).** For the selected
> top-packet layers there are choices
> \(\sigma_P\in\Sigma(P)\) such that
> \[
>       \sum_{\ell=1}^L\sum_X
>       \left(
>       |\{P\in\mathcal P_\ell:X\in\mathcal O(P,\sigma_P)\}|-1
>       \right)_+=o(W).
> \tag{6.2}
> \]

To obtain a literal chronology, (6.2) must be strengthened by the
word-state handoff condition between consecutive uses of a top. Neither
condition follows from the exact unbundled factor of Theorem 1.1.

Theorem 1.1 and (3.5)--(5.6) isolate the boundary: linear owner Hall is
perfect, while local product randomness is linearly colliding. The
missing object is a packet-respecting, globally negatively dependent
edge-colouring/rainbow factor.

## 7. Adversarial audit of the scope

Three tempting stronger conclusions do not follow from the proved
statements.

1. Theorem 1.1 does **not** prove a repaired-packet factor. Its matching
   may assign to one top a \(d\)-set with no Johnson-adjacent pair at
   all, whereas every legal deck has the consecutive adjacencies (2.4).
   The missing implication is exactly (2.3).

2. The lower bounds (3.10)--(3.11) are annealed statements. They do not
   lower-bound the deterministic minimum over all relabel choices. A
   distribution may have linear mean even when a very rare
   collision-free choice exists. Thus this note does not give a
   deterministic owner obstruction to the repaired packet catalogue.

3. Section 5 excludes the canonical atomic-event asymmetric LLL on the
   ordinary variable-dependency graph. Events sharing a packet variable
   may possess additional negative dependence, and a capacity-star
   resampling scheme could use a different lopsidependency structure.
   Such a scheme would need a new theorem proving that structure; it is
   not excluded here.

The strongest unconditional positive result is therefore the exact
unbundled factor. The strongest unconditional negative result is the
linear annealed collision and the failure of the standard LLL witness.
The correlated repaired-deck factor (6.2) remains genuinely open.
