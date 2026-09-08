# CCTPF full histories: a physical odd-port prism and an exponential repair radius

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Result

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad N=N_H,\qquad
 M=m+H,
\]

\[
 s=m-H,\qquad L=m-3H+1,
\]

and use the CCTPF quotas

\[
 b_0=L,
\qquad
 b_q=\min\left\{L-1,
 \max\left\{0,\left\lfloor{N_q\over N_H}\right\rfloor-1\right\}
 \right\}
 \quad(1\le q<H).
\tag{0.1}
\]

Because \(N_q\) decreases with \(q\ge0\), the integer sequence
\(b_0,b_1,\ldots,b_{H-1}\) is nonincreasing.

Assume the audited critical regime and calibration

\[
 H=(1+o(1))\sqrt{m\log m},\qquad m>4H,
\tag{0.2}
\]

\[
 L+c_0H\le \Lambda:={W\over N_H}\le m+C_0H
 \qquad(c_0,C_0>0\text{ fixed}).
\tag{0.3}
\]

This note proves the following.

1. For one fixed top, core, and nested tag pattern, the exact fraction of
   literal tail orders using a prescribed compatible target is

   \[
   {L\over\binom{s}{H}}
   \quad\hbox{at the middle,}
   \qquad
   {b_q\over\binom{s}{H-q}},\quad
   {b_q\over\binom{s}{H+q}}
   \quad\hbox{at signed depth }q.
   \tag{0.4}
   \]

   This is a full-history port count, not a rankwise Hall average.

2. Let \(p_*\) be the maximum of the fractions in (0.4), and let

   \[
   k=L+2\sum_{q=1}^{H-1}b_q
   \tag{0.5}
   \]

   be the exact number of protected physical targets in one tagged history.
   Any \(r\) distinct top roots, with arbitrary fixed good cores and arbitrary
   fixed nested phase sets of the prescribed sizes, admit pairwise
   target-disjoint literal full histories whenever

   \[
   (r-1)k p_*<1.
   \tag{0.6}
   \]

3. If

   \[
   t_*=\left\lceil{(m-H+1)\log 2\over 2H-1}\right\rceil,
   \tag{0.7}
   \]

   then, for all sufficiently large \(m\),

   \[
   p_*\le {L\over\binom{s}{t_*}},
   \tag{0.8}
   \]

   and therefore

   \[
   \log {1\over kp_*}
   \ge
   \left({\log 2\over4}-o(1)\right)\sqrt{m\log m}.
   \tag{0.9}
   \]

   Thus every bounded, polynomial, or

   \[
   \exp\{o(\sqrt{m\log m})\}
   \tag{0.10}
   \]

   root-supported closed odd-port subsystem repairs integrally inside the
   actual full-history catalogue.

4. Total unimodularity nevertheless fails in the literal catalogue. There
   is a six-history, three-root **triangular prism** in which assigning weight
   \(1/2\) to every history saturates each of its three root rows and
   respects every physical target capacity, but no integral choice of one of
   the two histories at each root is collision-free. Every column is one actual core-safe tail
   order, and the two options of each root use the same admissible nested tag
   profile. The same three prescribed
   cores can be extended to a global core assignment satisfying all CCTPF
   degree caps.

5. The prism is not a counterexample to CCTPF. By (0.6), the three complete
   root fibres have another integral selection whose entire protected
   histories are disjoint. Hence the physical determinant-two/odd-clique
   minor is a genuine obstruction to a network or TU proof, but it is not a
   closed obstruction to existence.

The exact surviving negative possibility is consequently a
fibre-dense, globally interlocked port mesh supported on at least

\[
 \exp\left\{\left({\log 2\over4}-o(1)\right)
                   \sqrt{m\log m}\right\}
\tag{0.11}
\]

roots, up to polynomial factors. No such obstruction is constructed here,
and CCTPF is not proved. This support statement concerns a standalone closed
root subsystem. It does not say that fewer than this many roots can always be
rerouted after an arbitrary exterior family has already frozen a large port
set.

## 1. Literal full-history configuration system

Fix a top

\[
 U\in\binom{[2m]}M
\]

and its fixed \(2H\)-core \(Q_U\subset U\). Put

\[
 S_U=U\setminus Q_U,
 \qquad |S_U|=s.
\]

For the exact unrestricted CCTPF program, let \(\mathfrak A_U\) be the
set of all nested phase families

\[
 [L]=A_0\supseteq A_1\supseteq\cdots\supseteq A_{H-1},
 \qquad |A_q|=b_q.
 \tag{1.1a}
\]

Equivalently, the stopping tag is
\(d(j)=\max\{q:j\in A_q\}\); then
\(|\{j:d(j)\ge q\}|=b_q\) exactly.

For a tail order \(w\) and \(A\in\mathfrak A_U\), let
\(\Gamma(U,w,A)\) be the complete typed protected-target set defined
below.  The single full-history integer program is

\[
 \sum_{w,A}x_{U,w,A}=1
 \qquad\left(U\in\binom{[2m]}M\right),
 \tag{1.1b}
\]

\[
 \sum_{U,w,A:T\in\Gamma(U,w,A)}x_{U,w,A}\le1
 \qquad(\text{every typed protected target }T),
 \tag{1.1c}
\]

\[
 x_{U,w,A}\in\{0,1\}.
 \tag{1.1d}
\]

Replacing the root equalities by inequalities gives the rooted matching
form used in the near-perfect CCTPF gate.  Equivalently, make one
conflict-graph vertex for every \((U,w,A)\), joining two vertices when
they have the same root or share a typed target.  CCTPF is an independent
transversal of all root cliques.

Each individual root catalogue is the source--sink path set of a finite
acyclic permutation/tag-state graph, and therefore has an integral
network-flow polytope.  Identifying equal physical targets adds the side
constraints (1.1c) across different root commodities.  A
single-commodity identification would permit a flow to enter a target
port with one root's prefix state and leave through another root's
continuation, violating the diagonal identities of a literal tail order.
Thus (1.1b)--(1.1d), rather than a rankwise flow, is the exact object.

The paired quotient-chain theorem does not remove this coupling.  Once
an integral target-simple family of histories has been selected, its
active paired maps have injective coordinate projections and its
cemetery-valued fibres automatically form a quotient chain.  In the
opposite direction, the quotient-chain representative extension has no
constraint forcing exactly \(b_q\) representatives from every root and
no constraint forcing all representatives of a root to arise from one
tail order.  Adding those constraints crosses the root partition with
the lower- and upper-target partitions—a coloured three-way matching.
Invoking paired quotient integrality before solving (1.1) would therefore
be circular.  The prism in Section 5 gives an exact certificate of this
failure.

For the positive repair theorems it is enough, and stronger, to fix one
member of \(\mathfrak A_U\) in every root.  Henceforth fix nested phase
sets

\[
 [L]=A_{U,0}\supseteq A_{U,1}\supseteq\cdots
 \supseteq A_{U,H-1},
 \qquad |A_{U,q}|=b_q.
\tag{1.1}
\]

This is one admissible stopping-tag pattern.  Fix an arbitrary order of
\(Q_U\), which does not change any protected incidence.  A configuration
is then a permutation \(w=(w_1,\ldots,w_s)\) of \(S_U\), so there are

\[
 D=s!
\tag{1.2}
\]

different tail configurations.

For phase \(1\le j\le L\) and deletion length \(0\le\ell\le2H\), write

\[
 R_{j,\ell}
 =\{j+2H-\ell,\ldots,j+2H-1\}\subseteq[s],
\tag{1.3}
\]

and

\[
 I_{j,\ell}(w)=\{w_t:t\in R_{j,\ell}\},
 \qquad
 T_{j,\ell}(w)=U\setminus I_{j,\ell}(w).
\tag{1.4}
\]

For an arbitrary phase family \(A\in\mathfrak A_U\), the target set used in
(1.1c) is exactly

\[
 \Gamma(U,w,A)
 =\{T_{j,H}(w):j\in[L]\}
 \cup
 \bigcup_{q=1}^{H-1}
 \{T_{j,H-q}(w),T_{j,H+q}(w):j\in A_q\}.
\tag{1.5}
\]

Thus \(\ell=H\) is middle rank, \(\ell=H-q\) is upper depth \(q\), and
\(\ell=H+q\) is lower depth \(q\). The full protected edge of \(w\) consists
of

* the root marker \(U\);
* all \(T_{j,H}(w)\), for \(j\in[L]\); and
* \(T_{j,H-q}(w)\) and \(T_{j,H+q}(w)\) for
  \(j\in A_{U,q}\), \(1\le q<H\).

These are exactly the literal CCTPF traces. No target incidence is inserted
independently of the tail order.

## 2. Exact single-port exposure

### Theorem 2.1 (literal port count)

Let \(T\subseteq[2m]\) have rank \(m+r\), where

\[
 -H<r<H.
\]

If \(T\) is not compatible with the root, meaning

\[
 Q_U\nsubseteq T\quad\hbox{or}\quad T\nsubseteq U,
\tag{2.1}
\]

then no configuration over \(U\) uses \(T\). If it is compatible, put

\[
 \ell=H-r.
\tag{2.2}
\]

The number of tail orders whose protected edge contains \(T\) is exactly

\[
 \begin{cases}
 \displaystyle D{L\over\binom{s}{H}},&r=0,\\[3mm]
 \displaystyle D{b_{|r|}\over\binom{s}{H-r}},&r\ne0.
 \end{cases}
\tag{2.3}
\]

#### Proof

Compatibility is necessary because every protected target has the form
\(U\setminus I\) with \(I\subseteq S_U\).

Assume compatibility and set \(I=U\setminus T\), so \(|I|=\ell\). At one
fixed phase \(j\), the number of permutations satisfying

\[
 I_{j,\ell}(w)=I
\]

is

\[
 \ell!(s-\ell)!={D\over\binom{s}{\ell}}.
\tag{2.4}
\]

For two distinct phase positions, the equal-length positional intervals
cannot contain the same set in one injective word. Indeed, if the intervals
overlap, shifting from one to the other removes at least one position and
adds the same number of new positions; equality of the two sets would force
a repeated letter. If they are disjoint, equality would again repeat every
letter. Hence the phase events in (2.4) are disjoint.

There are \(L\) displayed middle phases and \(b_{|r|}\) displayed phases at
nonzero signed depth. Summing the disjoint counts proves (2.3). \(□\)

Define the exact maximal port exposure

\[
 p_*=\max\left\{
 {L\over\binom{s}{H}},
 \max_{\substack{1\le q<H\\b_q>0}}
 \left\{
 {b_q\over\binom{s}{H-q}},
 {b_q\over\binom{s}{H+q}}
 \right\}
 \right\}.
\tag{2.5}
\]

### Corollary 2.2 (exact forbidden-port avoidance)

Let \(\mathcal B\) be any family of protected physical targets, of arbitrary
ranks. Define

\[
 \omega_U(\mathcal B)
 =\sum_{T\in\mathcal B}
 {\#\{w:T\hbox{ belongs to the protected edge of }w\}\over D}.
\tag{2.6}
\]

If

\[
 \omega_U(\mathcal B)<1,
\tag{2.7}
\]

then an actual tail order over \(U\), with the already fixed nested tag
sets, avoids every target in \(\mathcal B\). In particular, it is enough that

\[
 |\mathcal B|p_*<1.
\tag{2.8}
\]

#### Proof

By Theorem 2.1 and the union bound, the number of tail orders meeting at
least one member of \(\mathcal B\) is at most

\[
 D\omega_U(\mathcal B)<D.
\]

At least one literal order remains. Equation (2.8) follows from the
definition of \(p_*\). \(□\)

This is not a scalar Hall condition on target cardinalities. It is an exact
statement about the union of the physical port cylinders inside one whole
permutation fibre.

## 3. A global greedy common-history theorem below the port scale

### Theorem 3.1 (root-set integral repair)

Let \(U_1,\ldots,U_r\) be distinct tops. Fix an arbitrary \(2H\)-core in
each top and arbitrary nested phase sets satisfying (1.1). If

\[
 (r-1)kp_*<1,
\tag{3.1}
\]

then one can choose one literal tagged tail order in every root so that all
their protected middle, lower, and upper targets are globally distinct.

#### Proof

Order the roots arbitrarily. Choose any literal configuration in \(U_1\).
Suppose configurations have been chosen in \(U_1,\ldots,U_{a-1}\) and their
protected target sets are pairwise disjoint. Within one history, targets at
different signed ranks have different cardinalities, while targets at the
same rank and distinct phases are different by the interval argument in
Theorem 2.1. Hence each history contains exactly \(k\) distinct targets.
Therefore their union \(\mathcal B_{a-1}\) has size

\[
 |\mathcal B_{a-1}|=(a-1)k.
\]

By (3.1),

\[
 |\mathcal B_{a-1}|p_*<1.
\]

Corollary 2.2 supplies a literal configuration in \(U_a\) avoiding this
whole union. Continue inductively. \(□\)

### Corollary 3.2 (minimum support of a closed obstruction)

Consider the complete CCTPF configuration system on any collection of
roots, with the cores and phase sets fixed. Every inclusion-minimal root
subsystem having no target-simple full-history selection has at least

\[
 1+{1\over kp_*}
\tag{3.2}
\]

roots, with the evident ceiling interpretation.

The same conclusion holds when phase sets are allowed to vary as in the
unrestricted catalogue: first fix any one admissible nested phase family in
each root and apply Theorem 3.1 to that subcatalogue.

In particular, a bounded physical triangle, odd cycle, projective gadget,
or any polynomial union of such gadgets cannot be a closed CCTPF
obstruction.

#### Proof

Every smaller root system satisfies (3.1), hence has a selection by
Theorem 3.1. \(□\)

## 4. Quantitative repair radius at the critical height

### Lemma 4.1 (active depths stay away from the top)

If \(b_q>0\), then

\[
 H-q\ge t_*:=\left\lceil{(m-H+1)\log 2\over2H-1}\right\rceil.
\tag{4.1}
\]

#### Proof

Positivity of \(b_q\) implies

\[
 \left\lfloor{N_q\over N_H}\right\rfloor\ge2,
 \qquad {N_q\over N_H}\ge2.
\tag{4.2}
\]

The exact ratio is

\[
 {N_q\over N_H}
 =\prod_{i=q+1}^{H}{m+i\over m-i+1}.
\tag{4.3}
\]

Since

\[
 \log {m+i\over m-i+1}
 =\log\left(1+{2i-1\over m-i+1}\right)
 \le {2H-1\over m-H+1},
\]

(4.2)--(4.3) give

\[
 \log 2\le(H-q){2H-1\over m-H+1}.
\]

Taking ceilings proves (4.1). \(□\)

### Theorem 4.2 (exponential minor-repair radius)

For all sufficiently large \(m\),

\[
 p_*\le {L\over\binom{s}{t_*}}.
\tag{4.4}
\]

Moreover,

\[
 \log {1\over kp_*}
 \ge
 \left({\log 2\over4}-o(1)\right)\sqrt{m\log m}.
\tag{4.5}
\]

#### Proof

At the critical height, \(H=o(m)\). Hence eventually

\[
 t_*\le H,
 \qquad 2H-1<{s\over2}.
\tag{4.6}
\]

For the middle port, the deletion length is \(H\ge t_*\). At an active
upper depth it is \(H-q\ge t_*\) by Lemma 4.1. At an active lower depth it
is \(H+q\ge H\ge t_*\). Every relevant deletion length is at most \(2H-1\),
so monotonicity of \(\binom{s}{a}\) for \(a<s/2\) gives

\[
 \binom{s}{H},\quad
 \binom{s}{H-q},\quad
 \binom{s}{H+q}
 \ge\binom{s}{t_*}.
\]

Since \(b_q\le L\), this proves (4.4).

Also

\[
 k=L+2\sum_{q=1}^{H-1}b_q\le(2H-1)L.
\tag{4.7}
\]

The critical asymptotics give

\[
 t_*=\left({\log 2\over2}+o(1)\right)
       \sqrt{m\over\log m},
\tag{4.8}
\]

and

\[
 \log {s\over t_*}=\left({1\over2}+o(1)\right)\log m.
\tag{4.9}
\]

Using the elementary bound

\[
 \binom{s}{t_*}\ge\left({s\over t_*}\right)^{t_*},
\tag{4.10}
\]

we obtain

\[
 \log\binom{s}{t_*}
 \ge\left({\log 2\over4}-o(1)\right)\sqrt{m\log m}.
\tag{4.11}
\]

The factors \(kL\) are polynomial in \(m\), so (4.4), (4.7), and (4.11)
prove (4.5). \(□\)

The exponent in (4.5) is a proved lower bound, not asserted sharp. It is
enough to eliminate every local or polynomial odd-port architecture.

## 5. A literal root-saturating odd-port prism

The preceding theorem does not make the full target--configuration matrix
TU. We now give a full-history obstruction to that claim.

Assume \(H\ge5\) and \(m\ge5H\). Choose pairwise
disjoint sets

\[
 |C|=m-H,
 \qquad |B|=H+1,
 \qquad |E_0|=|E_1|=|E_2|=H-1.
\tag{5.1}
\]

Their total size is \(m+3H-2\le2m\). Choose a common core

\[
 Q\in\binom C{2H}.
\tag{5.2}
\]

Inside \(B\), choose six distinct labels

\[
 z_{i,b},\qquad i\in\mathbb Z/3\mathbb Z,\quad b\in\{0,1\}.
\tag{5.3}
\]

Here \(z_{i,b}\) labels the edge \(i(i+1)\) of a root triangle. Define

\[
 K=C\cup B,
 \qquad |K|=m+1,
\tag{5.4}
\]

and the three tops

\[
 U_i=K\cup E_i.
\tag{5.5}
\]

Each has size \(M=m+H\), and \(U_i\cap U_j=K\) for \(i\ne j\). Use the
core \(Q\) in all three tops.

For \(i\in\mathbb Z/3\mathbb Z\) and \(b\in\{0,1\}\), construct a tail
order \(w_i^b\) on \(S_i=U_i\setminus Q\) with the consecutive segment

\[
 z_{i-1,b},\quad E_i,\quad z_{i,b},
\tag{5.6}
\]

where \(E_i\) is written in any fixed order. For both values of \(b\), put
the other four labels from (5.3) in the first \(H\) positions, begin (5.6)
at position \(3H\), and fill the unused positions arbitrarily. Thus the
other four labels are at positional distance at least \(2H\) from the
\(E_i\)-block. The first two length-\(H\) subwords of (5.6) are eligible
middle windows at phases \(2H\) and \(2H+1\), which lie in \([L]\) once
\(m\ge5H\).

Explicitly,

\[
 R_{2H,H}={3H,ldots,4H-1\},\quad
 R_{2H+1,H}={3H+1,ldots,4H\},
\]

and

\[
 R_{2H,H-1}={3H+1,ldots,4H-1\}.
\]

The phase whose middle deletion window is

\[
 \{z_{i-1,b}\}\cup E_i
\tag{5.7}
\]

is therefore the common phase

\[
 a:=2H,
\]

independent of \(i\) and \(b\).

At the CCTPF calibration,

\[
 b_1=L-1
\tag{5.8}
\]

for all sufficiently large \(m\). Indeed,

\[
 {N_1\over N_H}={m\over m+1}{W\over N_H}
 \ge {m\over m+1}(L+c_0H)>L,
\]

so (0.1) gives (5.8). Fix, for each root, one nested phase family with

\[
 A_{i,1}=[L]\setminus\{a\},
\]

and choose nested subsets
\(A_{i,1}\supseteq A_{i,2}\supseteq\cdots\supseteq A_{i,H-1}\) with the
remaining prescribed sizes. This is possible because \((b_q)\) is
nonincreasing. Use this same phase family for both \(w_i^0\) and
\(w_i^1\). Thus phase \(a\) has stopping tag \(0\) and is the unique phase
inactive at depth one. Denote the resulting literal full history by
\(P_i^b\). The determinant certificate below consequently lies even in the
subcatalogue with one nested phase family fixed per root.

For each edge \(i(i+1)\) and bit \(b\), put

\[
 T_{i,b}=K\setminus\{z_{i,b}\}.
\tag{5.9}
\]

These are six distinct middle targets.

### Theorem 5.1 (physical triangular-prism obstruction)

The six literal tagged histories \(P_i^b\) have the following properties.

1. \(P_i^b\) contains exactly the two displayed parity targets

   \[
   T_{i-1,b},\qquad T_{i,b}
   \tag{5.10}
   \]

   among the six targets in (5.9).

2. Every physical protected target, including every active lower and upper
   trace at every depth, belongs to at most two of the six histories.

3. The assignment

   \[
   x(P_i^b)={1\over2}
   \tag{5.11}
   \]

   saturates each of the three root rows and respects every physical target
   capacity.

4. No integral selection of one history from each root is target-simple.

#### Proof

The two consecutive middle deletion windows in (5.6) are

\[
 E_i\cup\{z_{i-1,b}\},
 \qquad
 E_i\cup\{z_{i,b}\}.
\]

Their complements in \(U_i=K\cup E_i\) are (5.10). Since the \(H-1\)
letters of \(E_i\) are consecutive, the only length-\(H\) windows containing
all of \(E_i\) are these two. This proves Item 1.

We prove Item 2. Suppose a target \(T\) occurs in histories belonging to
two different roots. Then

\[
 T\subseteq U_i\cap U_j=K.
\tag{5.12}
\]

If \(|T|\ge m+2\), this is impossible because \(|K|=m+1\). If
\(|T|=m+1\), then \(T=K\). Such an upper depth-one trace in root \(i\)
would have deletion interval exactly \(E_i\). The only phase with that
interval is \(a=2H\), and this phase has tag \(0\).
Thus \(K\) is absent from all six protected histories.

If \(|T|=m\), then \(U_i\setminus T\) is an \(H\)-window containing all
of \(E_i\). By the first paragraph, \(T\) is one of (5.10). A label
\(z_{e,b}\) is adjacent to the \(E\)-block in exactly the two histories at
the endpoints of edge \(e\), with the same bit \(b\). Therefore every
displayed middle target has degree exactly two.

Finally let \(|T|=m-q\), \(1\le q<H\), and write

\[
 Z=K\setminus T,
 \qquad |Z|=q+1.
\tag{5.13}
\]

For \(T\) to occur in root \(i\), its deletion interval must be

\[
 E_i\cup Z.
\tag{5.14}
\]

This interval has length \(H+q\le2H-1\) and contains the consecutive
\(E_i\)-block. It therefore contains at least one of the two immediate
neighbours in (5.6). By the spacing condition, it contains no other label
from the six-element set in (5.3). Consequently

\[
 \varnothing\ne
 Z\cap\{z_{e,c}:e\in\mathbb Z/3\mathbb Z, c\in\{0,1\}\}
 \subseteq\{z_{i-1,b},z_{i,b}\}.
\tag{5.15}
\]

No special label belongs to three of the six adjacent pairs in the right
side of (5.15), and the pairs for the two bits at the same root are
disjoint. Hence one fixed \(Z\), and therefore one fixed lower target, can
occur in at most two histories. This proves Item 2.

Each root is incident with its two bit histories, so (5.11) gives root load
one. Item 2 gives target load at most one. This proves Item 3.

For Item 4, an integral root-saturating selection chooses bits

\[
 b_0,b_1,b_2\in\{0,1\}.
\]

If \(b_i=b_{i+1}=b\), the two chosen histories both contain \(T_{i,b}\).
Avoiding every collision would require

\[
 b_0\ne b_1,\qquad b_1\ne b_2,\qquad b_2\ne b_0,
\]

which is impossible. \(□\)

### Corollary 5.2 (exact odd-clique cuts)

For each fixed bit \(b\), the three histories

\[
 P_0^b,P_1^b,P_2^b
\]

form a conflict triangle, with its three edges witnessed by three distinct
physical middle targets. Hence every integral matching satisfies

\[
 x(P_0^b)+x(P_1^b)+x(P_2^b)\le1.
\tag{5.16}
\]

The ordinary target rows imply only the three pair inequalities and permit
the value \(3/2\) at (5.11). Summing (5.16) over the two bits gives an upper
bound \(2\), while the three root equalities give total selected mass \(3\).
Thus the six-column root-saturating relaxation is nonintegral.

More explicitly, for a fixed bit, order the target rows as
\(T_{0,b},T_{1,b},T_{2,b}\) and the columns as
\(P_0^b,P_1^b,P_2^b\). Their incidence submatrix is

\[
 \begin{pmatrix}
  1&1&0\\
  0&1&1\\
  1&0&1
 \end{pmatrix},
 \qquad \det=2.
\tag{5.17}
\]

This \(3\)-by-\(3\) target--configuration triangle is also the smallest
possible determinant-two \(0\)-\(1\) minor: every \(1\)-by-\(1\) or
\(2\)-by-\(2\) \(0\)-\(1\) determinant has absolute value at most one.

## 6. Compatibility with the common-core degree caps

The prism is not obtained by abandoning the good-core hypotheses.

### Lemma 6.1 (finite prescribed cores can be retained)

Fix a uniformly bounded number of top--core pairs in advance. For all
sufficiently large \(m\),
the remaining top cores can be chosen so that the complete assignment still
satisfies every middle and signed CCTPF maximum-degree cap.

#### Proof

Run the same independent random-core experiment used in the audited global
common-core theorem on all unprescribed tops. A target receives at most
\(C\) deterministic compatible roots from the prescribed part, for one
constant \(C\) independent of \(m\). The mean contribution from the
unprescribed tops is no larger than the original unconditioned mean.

At the middle, the cap-minus-mean margin before this bounded perturbation is

\[
 \binom{s}{H}
 \left({1\over L}-{1\over W/N_H}\right)
 \ge c\binom{s}{H}{H\over m^2},
\tag{6.1}
\]

which tends to infinity superpolynomially. At a signed rank with \(b_q>0\),
write

\[
 d_r=\binom{s}{H-r},
 \qquad \Lambda_r={N_{|r|}\over N_H}.
\]

Since \(\Lambda_r-b_q\ge1\), the cap-minus-mean margin is at least

\[
 {d_r\over b_q}-{d_r\over\Lambda_r}
 ={d_r(\Lambda_r-b_q)\over b_q\Lambda_r}
 \ge {d_r\over\Lambda_r^2}.
\tag{6.2}
\]

For completeness, \(N_{|r|}\le W\) and the calibrated inequality
\(W/N_H\le m+C_0H\) give \(\Lambda_r=O(m)\). Lemma 4.1 and (4.6) give

\[
 d_r=\binom{s}{H-r}\ge\binom{s}{t_*}
\]

at every active signed rank. Equation (4.11) then implies
\(d_r/\Lambda_r^3\gg m\). Consequently (6.2) is much larger than the
bounded prescribed contribution, uniformly over every active rank.
For large \(m\), subtracting \(C\) from each threshold leaves at least half
the displayed cap-minus-mean gap. The standard upper-tail Chernoff bound
therefore gives failure probability at most

\[
 \exp\left\{-c'{d_0H^2\over m^3}\right\}
\]

for a fixed middle target, and at most

\[
 \exp\left\{-c'{d_r\over\Lambda_r^3}\right\}
\]

for a fixed active signed target. Both exponents are \(\gg m\). There are
fewer than \(2H4^m\) target rows over all protected ranks, so the union of
all failure events has probability less than one for all sufficiently large
\(m\).
Thus some completion of the prescribed cores satisfies the original caps.
\(□\)

Apply Lemma 6.1 to the three pairs \((U_i,Q)\) in Section 5. The literal
root-saturating odd-port prism therefore occurs inside a fixed-core atlas
obeying all common-core caps. In particular, its determinant-two
target--configuration submatrix is a submatrix of the globally capped
configuration matrix, so that full matrix is not totally unimodular. The
half-integral point itself saturates only the three displayed root rows; no
claim is made that it extends fractionally over all remaining roots.

## 7. Why the prism is repaired in the complete catalogue

The prism disproves total unimodularity of the natural incidence matrix and
the ordinary single-commodity construction obtained by identifying equal
target ports.
It does not disprove the desired integral selection.

Indeed, Theorem 4.2 gives

\[
 2kp_*<1
\]

for all sufficiently large \(m\). Theorem 3.1, applied to
\(U_0,U_1,U_2\), therefore chooses one other literal tagged tail order in
each of these same roots such that their **entire** protected histories are
pairwise target-disjoint. This changes neither the roots, the fixed cores,
nor the fixed nested phase families.

Thus the correct verdict on the natural odd minors is exact:

* the three-target determinant-two triangle is physically real;
* its six-history root-saturating lift is physically real at every signed
  depth;
* the natural target-node flow or incidence-matrix TU argument cannot be
  correct;
* but the full order fibres repair this prism, and in fact repair every
  closed root subsystem below the exponential radius (0.9).

Any closed CCTPF counterexample must consequently lock an exponential number
of root fibres together. Equivalently, it must block essentially all tail
orders of each participating root by a port family of normalized exposure at
least one. A bounded triangle, a finite blossom, or a polynomial collection
of them cannot do this as a standalone subsystem. As already noted after
(0.11), this says nothing about rerouting a small set of roots against an
arbitrarily frozen exterior.

## 8. Exact proved and unproved boundary

Proved:

1. the exact full-history single-target exposure formula (2.3);
2. the literal forbidden-port avoidance theorem;
3. integral common-history selection on every root set satisfying (3.1);
4. the explicit exponential repair radius (4.5);
5. a six-history physical root-saturating odd-port prism with complete
   signed-target capacity audit;
6. compatibility of that prism with the fixed common-core caps; and
7. integral repair of the prism after restoring the complete root fibres.

Not proved:

1. CCTPF on all \(N_H\) roots;
2. integrality of the complete full-history polytope;
3. absence of a fibre-dense odd mesh above the radius (0.9); or
4. the constant-one theorem from this lane alone.

The sharp surviving interface is therefore not an ordinary Hall cut and
not a bounded odd set. It is a genuinely global common-history contention
problem beyond the exact local repair radius.
