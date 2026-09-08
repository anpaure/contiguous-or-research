# FIFO rainbow circulation and quota-balanced atom rounding

**Date:** 2026-08-22

## 0. Scope, definitions, and outcome

Let \(\Omega\) be an \(n\)-element set. A word is a finite sequence
\(X=(X_1,\ldots,X_L)\) of subsets of \(\Omega\). It realizes a nonempty
target \(T\subseteq\Omega\) if

\[
T=X_i\cup X_{i+1}\cup\cdots\cup X_j
\]

for some contiguous interval \([i,j]\). Let \(\nu(n)\) be the minimum
length of a word realizing every nonempty subset of \(\Omega\), and put

\[
W(n)=\binom{n}{\lfloor n/2\rfloor}.
\]

For any fixed rank \(s\), the interval unions ending at one position form
a chain under inclusion, so they contain at most one distinct \(s\)-set.
Consequently every universal word has length at least \(\binom ns\), and
in particular

\[
\nu(n)\ge W(n).                                           \tag{0.1}
\]

This note isolates the ordered-state content of Gate C. It proves:

1. The injective FIFO overlap digraph has an exact optimal fractional
   rainbow circulation, with the ideal marginal at every suffix rank.
2. Choosing one ordered representative independently for each middle
   colour fails maximally: the expected number of compatible transitions
   tends to zero in the middle-dimensional regime.
3. Phase-refined product atoms give another exact fractional circulation,
   supported on literal rainbow FIFO cycles of length \(b^2\), again with
   ideal marginals at all controlled ranks.
4. Pairwise-disjoint atom domains are unnecessary. It suffices to choose
   \(\lceil W/b^2\rceil\) atoms whose loads have total **one-sided
   overflow** \(o(W)\) above balanced positive quotas.

The fourth result is a coefficient-one compiler and a strictly weaker
Gate-C target than a disjoint atlas. This note does **not** prove that the
required quota-balanced integral atom selection exists.

## 1. The injective FIFO overlap digraph

Fix integers

\[
1\le k<g\le n.
\]

Let \(\Gamma_{n,g}\) be the directed graph whose vertices are injective
ordered words of length \(g-1\). Every injective word
\(a=(a_1,\ldots,a_g)\) is an arc from
\((a_1,\ldots,a_{g-1})\) to \((a_2,\ldots,a_g)\). Thus one step deletes
the oldest symbol and appends a symbol absent from the current state.

For \(1\le s\le g\), define the rank-\(s\) suffix flag and the middle
colour of \(a\) by

\[
F_s(a)=\{a_{g-s+1},\ldots,a_g\},\qquad c(a)=F_k(a).
\]

Put

\[
W=\binom nk,\qquad N_s=\binom ns,
\qquad R_k=k!(n-k)_{g-k},                                \tag{1.1}
\]

where \((x)_j=x(x-1)\cdots(x-j+1)\).

### Theorem 1.1 (exact optimal fractional rainbow circulation)

Give every arc of \(\Gamma_{n,g}\) weight \(1/R_k\). Then:

1. every middle colour has total weight exactly one;
2. weighted indegree equals weighted outdegree at every ordered state;
3. total arc weight is exactly \(W\), optimal under the middle-colour
   capacity constraints;
4. every rank-\(s\) target has total suffix-flag weight

   \[
   \boxed{\frac{W}{N_s}}.                                \tag{1.2}
   \]

#### Proof

Fix a \(k\)-set \(S\). The last \(k\) arc positions can order \(S\) in
\(k!\) ways. The first \(g-k\) positions are an ordered choice from
\(\Omega\setminus S\), giving \((n-k)_{g-k}\) choices. Thus exactly
\(R_k\) arcs have colour \(S\).

Every state has exactly \(n-g+1\) incoming and \(n-g+1\) outgoing arcs.
All arc weights are equal, so the weighting is balanced. There are
\((n)_g\) arcs, and

\[
\frac{(n)_g}{R_k}
=\frac{n!/(n-g)!}{k!(n-k)!/(n-g)!}
=\binom nk=W.                                             \tag{1.3}
\]

Summing the \(W\) colour-capacity constraints bounds every feasible
weighting's total mass by \(W\), proving optimality.

Finally, a fixed \(s\)-set \(T\) occurs as a suffix flag in exactly

\[
R_s=s!(n-s)_{g-s}=\frac{s!(n-s)!}{(n-g)!}
\]

arcs. Its weighted load is therefore

\[
\frac{R_s}{R_k}
=\frac{s!(n-s)!}{k!(n-k)!}
=\frac{\binom nk}{\binom ns}
=\frac W{N_s},
\]

which proves (1.2). \(\square\)

For the middle-cube application, take

\[
n=2b,\qquad k=b,\qquad g=b+H+2.                          \tag{1.4}
\]

A directed circuit in \(\Gamma_{n,g}\) spells a cyclic singleton word
whose cyclic blocks of \(g\) letters are injective. Its \(s\)-windows are
the flags \(F_s\) of its arcs. Thus no fractional obstruction comes from
balance, colour capacity, or simultaneous rank marginals.

## 2. Independent representatives destroy adjacency

### Theorem 2.1 (independent transversal has no FIFO transitions)

Independently for each \(S\in\binom{\Omega}{k}\), choose one of its
\(R_k\) arcs uniformly. Let \(Z\) count ordered pairs of chosen arcs in
which the head of the first equals the tail of the second. Then

\[
\boxed{\mathbb E Z=\frac{W(n-g+1)}{R_k}}.                 \tag{2.1}
\]

If \(n\in\{2k,2k+1\}\) and \(g\ge k+1\), then

\[
\Pr(Z>0)=o(1).                                            \tag{2.2}
\]

#### Proof

Condition on the chosen arc of a colour \(S\). Its head state has
\(n-g+1\) legal appended symbols. They give distinct successor colours,
all different from \(S\), and for each such colour exactly one of its
\(R_k\) representatives has the required tail. Its conditional expected
chosen outdegree is therefore \((n-g+1)/R_k\). Summing over the \(W\)
chosen arcs proves (2.1).

In the stated regimes,

\[
W\le 2^{2k+1},\qquad n-g+1\le k+1,\qquad R_k\ge k!.
\]

Thus \(\mathbb EZ\le 2^{2k+1}(k+1)/k!=o(1)\), for example by
Stirling's formula. Markov's inequality proves (2.2). \(\square\)

Hence the factorial representation fibre does not make independent
rounding dense; it makes the selected ordered graph asymptotically
edgeless. Any successful rounding must correlate whole trails or cycles,
or impose an equivalent global coupling.

## 3. Product atoms as literal FIFO cycles

Let

\[
b=2h+1,\qquad \Omega=A\mathbin{\dot\cup}B,
\qquad |A|=|B|=b,\qquad W=\binom{2b}{b}.                 \tag{3.1}
\]

Choose directed cyclic orders \(\alpha\) on \(A\) and \(\beta\) on
\(B\), both modulo rotation. Repeat the length-\(b\) type word

\[
B,A,B,A,\ldots,B,A,B,                                    \tag{3.2}
\]

which has \(h\) events of type \(A\) and \(h+1\) of type \(B\). Choose a
root pair \((r_A,r_B)\in\mathbb Z_b^2\). At successive \(A\)-events emit
successive symbols of \(\alpha\) starting at \(r_A\), and at successive
\(B\)-events do the same in \(\beta\) starting at \(r_B\).

Advancing time by one full type period rotates the resulting cyclic word
by \(b\) letters and changes the root pair by

\[
(r_A,r_B)\longmapsto(r_A+h,r_B+h+1).                    \tag{3.3}
\]

Therefore the relative phases are the cosets

\[
Q=\mathbb Z_b^2/\langle(h,h+1)\rangle .
\]

The vector \((h,h+1)\) has order \(b\), so \(|Q|=b\). Changing index
origins for the two cyclic orders translates \(\mathbb Z_b^2\) and merely
permutes these cosets. For each \(\rho\in Q\), choose a representative
root pair and call the resulting cyclic word
\(w(A,\alpha,\beta;\rho)\). A **phase-refined labelled atom** includes
the label \((A,\alpha,\beta,\rho)\). This quotient definition, rather
than simultaneous \((1,1)\)-rotation of stream roots, is the phase used
below.

Writing \(I_\alpha(i,r)\) for the cyclic interval of \(r\) successive
symbols of \(\alpha\) beginning at \(i\), the central deck is

\[
E(A,\alpha,\beta)=
\left\{I_\alpha(i,h)\cup I_\beta(j,h+1):
(i,j)\in\mathbb Z_b^2\right\}.                           \tag{3.4}
\]

### Lemma 3.1 (atom chronology)

Every phase-refined atom has these properties:

1. its \(b^2\) cyclic length-\(b\) windows are exactly the members of
   (3.4), once each, and are pairwise distinct;
2. the forward cyclic gap between consecutive emissions of any fixed
   coordinate is at least \(2b-2\).

#### Proof

Every length-\(b\) type window contains \(h\) \(A\)-events and \(h+1\)
\(B\)-events, yielding consecutive cyclic intervals in the two streams.
If \((i_t,j_t)\) are their stream starts at time \(t\), then
\(i_t+j_t=t+\text{constant}\pmod b\). Advancing by one type period maps

\[
(i,j)\longmapsto(i+h,j+h+1)=(i+h,j-h)\pmod b.
\]

Since \(\gcd(h,b)=1\), the \(b\) advances at a fixed time residue visit
all \(b\) pairs on its diagonal, and the \(b\) time residues give all of
\(\mathbb Z_b^2\). Intersecting a window with \(A\) and \(B\) recovers
its two stream intervals, so the sets are distinct.

Successive \(A\)-events have type gaps \(2,\ldots,2,3\); successive
\(B\)-events have gaps \(2,\ldots,2,1\). A coordinate recurs after
exactly \(b\) events of its own type. Among any \(b\) consecutive
\(B\)-event gaps there are at most two gaps of size one, so their sum is
at least \(2b-2\); the \(A\)-bound is no smaller. \(\square\)

There are, as labelled objects,

\[
\widehat N=bW((b-1)!)^2                                  \tag{3.5}
\]

phase-refined atoms: choose \(A\), the two directed cyclic orders, and
one of the \(b\) cosets in \(Q\). The full labelled family is invariant
under every permutation of \(\Omega\): a permutation transports the
split, cyclic orders, root pairs, and the quotient relation (3.3).
Since each atom has \(b^2\) distinct middle targets, the common number of
labelled atoms through one middle target is

\[
\widehat D=\frac{\widehat N b^2}{W}=b(b!)^2.              \tag{3.6}
\]

### Theorem 3.2 (exact full-rank fractional FIFO atlas)

Assume \(b<g\le 2b-2\). Regard every phase-refined labelled atom as a
directed \(b^2\)-cycle in \(\Gamma_{2b,g}\), and give every atom weight
\(1/\widehat D\). Then:

1. every middle target has atom load one;
2. total atom weight is \(W/b^2\), while total weighted word length is
   \(W\);
3. for every \(1\le s\le g\), every \(s\)-set has weighted cyclic-window
   occurrence load

   \[
   \boxed{\frac{W}{\binom{2b}{s}}}.                       \tag{3.7}
   \]

#### Proof

Lemma 3.1 and \(g\le2b-2\) imply that every cyclic block of length \(g\)
is injective, so each atom is a cycle in the FIFO digraph. Equations
(3.4) and (3.6) give middle load one. Moreover,

\[
\frac{\widehat N}{\widehat D}
=\frac{bW((b-1)!)^2}{b(b!)^2}=\frac W{b^2},
\]

and multiplication by the period \(b^2\) gives total weighted word
length \(W\).

At rank \(s\), every atom has exactly \(b^2\) cyclic window occurrences,
counted with multiplicity. The labelled, phase-refined family and its
weights are invariant under the full symmetric group on \(\Omega\),
which is transitive on \(s\)-sets. Hence every \(s\)-set has equal
weighted load. Total rank-\(s\) occurrence mass is \(W\), so division by
\(\binom{2b}{s}\) proves (3.7). \(\square\)

## 4. Exact holes-versus-overflow accounting

Choose any list \(\mathscr A\) of \(t\) labelled atoms; atoms may repeat
and their target sets may overlap. Put

\[
M=b^2t.                                                   \tag{4.1}
\]

For \(s\le g\) and \(T\in\binom{\Omega}{s}\), let \(a_s(T)\) be the
number of cyclic length-\(s\) window occurrences equal to \(T\) among
all selected atom words. Thus

\[
\sum_T a_s(T)=M.                                         \tag{4.2}
\]

Let

\[
h_s=|\{T:a_s(T)=0\}|,
\qquad C_s=\sum_T(a_s(T)-1)_+ .                          \tag{4.3}
\]

### Lemma 4.1 (exact collision identity)

For every \(s\le g\),

\[
\boxed{h_s=\binom{2b}{s}-M+C_s}.                         \tag{4.4}
\]

#### Proof

Writing \(N_s=\binom{2b}{s}\), the number of positive-load targets is
\(N_s-h_s\), and

\[
M=\sum_Ta_s(T)=(N_s-h_s)+\sum_T(a_s(T)-1)_+
=N_s-h_s+C_s.
\]

Rearrange. \(\square\)

For off-middle ranks, \(M-N_s\) is unavoidable repeated mass, so raw
collision mass is the wrong error quantity. Assume \(M\ge W\). Since the
middle layer is largest, \(M\ge N_s\) for every \(s\). For each rank
choose balanced integer quotas

\[
q_s(T)\in
\left\{\left\lfloor\frac{M}{N_s}\right\rfloor,
       \left\lceil\frac{M}{N_s}\right\rceil\right\},
\qquad \sum_Tq_s(T)=M.                                   \tag{4.5}
\]

Such quotas exist by assigning the ceiling to exactly
\(M-N_s\lfloor M/N_s\rfloor\) targets. Every quota is at least one. Define
the one-sided overflow

\[
V_s=\sum_T(a_s(T)-q_s(T))_+.                             \tag{4.6}
\]

### Lemma 4.2 (overflow pays for holes)

For every \(s\),

\[
\boxed{h_s\le V_s}.                                      \tag{4.7}
\]

#### Proof

The load and quota vectors both have total \(M\), hence

\[
\sum_T(a_s(T)-q_s(T))_+
=\sum_T(q_s(T)-a_s(T))_+.                                \tag{4.8}
\]

Every hole has \(a_s(T)=0\) and \(q_s(T)\ge1\), so it contributes at
least one to the right side. \(\square\)

Thus only **overflow**, not absolute deviation, is required. Repetitions
up to quota are harmless only in the following precise accounting sense:
they consume part of the fixed mass \(M\), but create no excess above the
unavoidable balanced baseline. Equality of total mass converts every
quota deficit, including every hole, into equal aggregate overflow. The
compiler below additionally requires \(M=W+o(W)\), so this fixed repeated
mass does not itself inflate the final word beyond coefficient one.

## 5. Quota-balanced atom selection implies coefficient one

Let

\[
H=\left\lceil\sqrt{2b\log(2b)}\right\rceil,
\qquad g=b+H+2,
\qquad \mathcal B=\{b-H,\ldots,b+H\}.                    \tag{5.1}
\]

For all sufficiently large \(b\), \(g\le2b-2\). Set

\[
t=\left\lceil\frac W{b^2}\right\rceil,
\qquad M=b^2t,
\qquad W\le M<W+b^2.                                    \tag{5.2}
\]

### Theorem 5.1 (quota-balanced FIFO atom compiler)

Suppose that for every sufficiently large odd \(b\), one can choose
\(t\) phase-refined labelled product atoms and balanced quotas (4.5) such
that

\[
\boxed{\sum_{s\in\mathcal B}V_s=o(W)}.                   \tag{5.3}
\]

Then

\[
\nu(2b)=(1+o(1))\binom{2b}{b}.                           \tag{5.4}
\]

The same conclusion follows in every dimension using at most three
top-bit splices.

#### Proof

For each selected cyclic atom \(u_0,\ldots,u_{b^2-1}\), write the linear
singleton block

\[
u_0,\ldots,u_{b^2-1},u_0,\ldots,u_{g-2}.
\]

It has length \(b^2+g-1\) and contains every cyclic window of that atom
of every length at most \(g\). Concatenate the \(t\) blocks. Atom domains
and target decks need not be disjoint: every counted witness remains
wholly inside its own block, and concatenation cannot destroy an internal
interval union. Crossing intervals can only add witnesses. Thus target
overlap causes no physical incompatibility beyond the load/coverage ledger.

The concatenated length is

\[
\begin{aligned}
t(b^2+g-1)
&=M+t(g-1)\\
&=W+O(b^2)+O\!\left(\frac{Wg}{b^2}\right)
=W+o(W),                                                 \tag{5.5}
\end{aligned}
\]

because \(g=O(b)\), \(t=O(W/b^2)\), and \(W\) is exponential in \(b\).
By Lemma 4.2 and (5.3), the aggregate number of band targets absent from
the internal atom windows is \(o(W)\). Append each missing band target as
one set-valued letter; that singleton interval realizes the target.

It remains to count ranks outside \(\mathcal B\). For
\(X\sim\operatorname{Bin}(2b,1/2)\), the exponential-moment estimate

\[
\Pr(|X-b|\ge H)\le2e^{-H^2/b}                            \tag{5.6}
\]

follows from
\(\mathbb E e^{\lambda(X-b)}=(\cosh(\lambda/2))^{2b}
\le e^{b\lambda^2/4}\) and optimization in \(\lambda\). Also
\(W\ge2^{2b}/(2b+1)\). Since \(H^2\ge2b\log(2b)\), the total number of
outside-band targets is at most

\[
2^{2b+1}e^{-H^2/b}
\le \frac{2(2b+1)}{(2b)^2}\,W=o(W).                      \tag{5.7}
\]

Append every nonempty missing outside-band target as one set-valued
letter. Equations (5.3), (5.5), and (5.7) give a universal word of length
\(W+o(W)\). The self-contained lower bound (0.1) proves (5.4).

For completeness, if \(X=(X_1,\ldots,X_L)\) is universal on \(k-1\)
coordinates and \(z\) is new, then

\[
X_1,\ldots,X_L,\{z\},
X_1\cup\{z\},\ldots,X_{L-1}\cup\{z\}                    \tag{5.8}
\]

is universal on \(k\) coordinates and has length \(2L\). Targets avoiding
\(z\) use the first copy. If \(T\) is witnessed by
\(X_i,\ldots,X_j\), then \(T\cup\{z\}\) uses the lifted copy when
\(j<L\), and \(X_i,\ldots,X_L,\{z\}\) when \(j=L\); the target
\(\{z\}\) uses the bridge.

The base dimensions \(2b\) with odd \(b\) are congruent to \(2\pmod4\).
Every sufficiently large dimension is exactly \(2b+j\) for such an odd
\(b\) and some \(0\le j\le3\). For each fixed \(j\),

\[
\frac{2^j\binom{2b}{b}}
     {\binom{2b+j}{\lfloor(2b+j)/2\rfloor}}
=1+O(1/b).                                               \tag{5.9}
\]

Apply (5.8) \(j\) times and combine (5.9) with (0.1). \(\square\)

### Corollary 5.2 (exact remaining Gate-C selection statement)

For the product-atom/FIFO route, it suffices to select exactly
\(\lceil W/b^2\rceil\) phase-refined labelled atom cycles so that their
rank-\(s\) occurrence loads have aggregate overflow \(o(W)\) above some
balanced floor/ceiling quotas, summed over
\(b-H\le s\le b+H\).

This is strictly weaker than selecting pairwise-disjoint atom target
domains. At the middle rank, the quotas are one except for fewer than
\(b^2\) quota-two targets, so (5.3) still forces an almost-packing. At
off-middle ranks, it permits exactly the repetitions forced by the smaller
layer sizes. No support-disjointness, connector-disjointness, or cross-atom
chronology condition is needed: every atom is separately linearized, and
the total serialization overhead is
\(t(g-1)=O(W/b)=o(W)\), irrespective of domain overlap.

## 6. Logical boundary

The proved implication is

\[
\boxed{
\text{quota-balanced integral atom selection (5.3)}
\Longrightarrow \nu(n)=(1+o(1))W(n).
}
\]

Unconditionally proved here are the exact optimal fractional FIFO
circulation, its simultaneous rank marginals, a fractional circulation on
literal rainbow product-atom cycles, the exact overflow-to-hole accounting,
and the absence of any serialization obstruction from overlapping atom
domains. The sole missing theorem on this route is the dependent integral
rounding assertion (5.3).
