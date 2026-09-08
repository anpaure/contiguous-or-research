# The exceptional rank-five circuit:
# exact chronology, local compatibility, and finite lazy Hall cuts

Date: 2026-07-29

Status: exact two-orbit theorem, exact chronology identities, a global
support-complete near-counterexample, and an exact finite cut scheme.  The
singleton orbit and the exceptional rank-five orbit form a defect-three
forced-port circuit if and only if their two quotient neighborhoods are the
same singleton block.

There is a finite cyclic order-15 equivariant controller with maximal
depth-three erosion, three-residence, complete support at every rank from
five through fifteen, exactly one exceptional rank-five block orbit, and
exactly the same one singleton-port orbit.  It has a common equivariant
one-core making every target orbit positive, but no one-core can pass Hall.
The construction is FIFO except for one explicit queue-reversal hourglass.

The near-counterexample does not have length 6435 and its rank-eight row
does not enumerate the middle deck exactly once.  Thus it is not a strict
exact-factor carrier and is not a counterexample to the requested theorem.
It proves that the exact middle/q1 factor-injectivity package is the first
remaining hypothesis capable of excluding the circuit; support completeness,
residence, erosion, equivariance, and forced-port chronology do not.

The note also gives an exact carrier-level lazy Hall cut.  For the
exceptional circuit it is a six-middle-state marked-path cut.  For an
arbitrary weighted shore it is the usual Hall inequality reified through
forced-port eligibility.  Adding the physical assignment variables and the
pairwise orbit-closed omission conflicts gives a finite necessary-and-
sufficient formulation of the common-core compiler.

## 1. Setup

Put

\[
 k=15,\qquad r=8,\qquad d=3,\qquad h=5,
\]
\[
 W={15\choose8}=6435,\qquad N=W/15=429.
\tag{1.1}
\]

Let \(T=(T_i)_{i\in\mathbb Z_W}\) be a cyclic strict rank-eight Johnson
chronology with unit-voltage equivariance

\[
                         T_{i+N}=\rho^vT_i,
\qquad (v,15)=1,
\tag{1.2}
\]

where \(\rho(x)=x+1\).  Assume three-residence and let its maximal erosion be

\[
                         P_i=T_i\cap T_{i-1}\cap T_{i-2}\cap T_{i-3}.
\tag{1.3}
\]

Then \(P_i\) has rank five, consecutive \(P\)-states are Johnson adjacent,
and

\[
                         D^3P=T,\qquad (DX)_i=X_i\cup X_{i+1}.
\tag{1.4}
\]

Define the forced port

\[
 F_i=(P_i\setminus P_{i-1})\cup(P_i\setminus P_{i+1}).
\tag{1.5}
\]

Every one-core \(C\subseteq P\) with \(DC=DP\) satisfies

\[
                         F_i\subseteq C_i\subseteq P_i.
\tag{1.6}
\]

The physical position orbit through \(j\in\mathbb Z_N\) is

\[
                         J_j=\{j+tN:t\in\mathbb Z_{15}\},
\tag{1.7}
\]

with the twisted predecessor and successor used at the quotient seam.

Let

\[
                         Q=\{0,3,6,9,12\}.
\tag{1.8}
\]

Its translation orbit

\[
                         E_5=\{Q,Q+1,Q+2\}
\tag{1.9}
\]

has physical weight three.  Let \(U\) be the unique singleton target orbit;
it has physical weight fifteen.

## 2. The middle-row chronology of a forced port

Write the middle transition as

\[
                         T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.
\tag{2.1}
\]

### Theorem 2.1 (four-step return identity)

For every position,

\[
 P_i\setminus P_{i-1}=\{\beta_{i-4}\},
\qquad
 P_i\setminus P_{i+1}=\{\alpha_i\},
\tag{2.2}
\]

and hence

\[
                         F_i=\{\beta_{i-4},\alpha_i\}.
\tag{2.3}
\]

Consequently

\[
 |F_i|=1
 \quad\Longleftrightarrow\quad
 \beta_{i-4}=\alpha_i.
\tag{2.4}
\]

The common coordinate in (2.4) has a positive run of exactly four states
in \(T\).  Thus a singleton port saturates the three-residence lower bound;
it does not violate it.

#### Proof

The label \(\beta_{i-4}\) enters in the transition
\(T_{i-4}\to T_{i-3}\).  Three-residence keeps it in

\[
                         T_{i-3},T_{i-2},T_{i-1},T_i.
\]

It therefore belongs to \(P_i\), while it is absent from \(T_{i-4}\) and
hence from \(P_{i-1}\).  These two rank-five states are Johnson adjacent,
so this is their unique entering label.

Similarly \(\alpha_i\) belongs to \(T_i\) and to the preceding three
middle states, but is absent from \(T_{i+1}\).  It is the unique label of
\(P_i\setminus P_{i+1}\).  This proves (2.2)--(2.3).  Equality of the two
labels says exactly that the label enters at transition \(i-4\) and leaves
at transition \(i\), so it occupies the four middle states
\(T_{i-3},\ldots,T_i\).  \(\square\)

This is the first genuinely same-row chronology identity relevant to the
defect-three circuit.  It gives a marked four-return, not a prohibition.

## 3. Exact singleton and exceptional neighborhoods

Define two sets of quotient blocks:

\[
 \mathcal L:=\{J_j:|F_j|=1\},
\qquad
 \mathcal E:=\{J_j:P_j\in E_5\}.
\tag{3.1}
\]

Let \(N_F\) denote the quotient graph obtained from the Boolean intervals
\([F_i,P_i]\).

### Theorem 3.1 (exact forced-port neighborhoods)

\[
                         N_F(U)=\mathcal L,
\qquad
                         N_F(E_5)=\mathcal E.
\tag{3.2}
\]

Therefore

\[
 \Delta_F(U\cup E_5)
 =18-15|\mathcal L\cup\mathcal E|.
\tag{3.3}
\]

In particular, once both target orbits have positive degree,

\[
 \boxed{
 N_F(U)=N_F(E_5)=\{J_*\}
 \quad\Longleftrightarrow\quad
 \mathcal L=\mathcal E=\{J_*\},
 }
\tag{3.4}
\]

and this shore then has defect exactly three.

#### Proof

The port \(F_i\) is nonempty and has size one or two.  It is contained in
a singleton target exactly when it has size one.  This proves the first
identity.

For \(S\in E_5\), both \(S\) and \(P_i\) have size five.  Therefore

\[
                         F_i\subseteq S\subseteq P_i
 \quad\Longleftrightarrow\quad
                         S=P_i\in E_5.
\]

This proves the second identity.  The two target weights are \(15\) and
\(3\), while every right block has capacity \(15\), giving (3.3)--(3.4).
\(\square\)

For a fixed one-core \(C\), put

\[
                         \mathcal L_C:=\{J_j:|C_j|=1\}.
\tag{3.5}
\]

Since \(F_j\subseteq C_j\), one has

\[
                         \mathcal L_C\subseteq\mathcal L,
\tag{3.6}
\]

and exactly

\[
                         N_C(U)=\mathcal L_C,
\qquad
                         N_C(E_5)=\mathcal E.
\tag{3.7}
\]

Thus a deliberately dense core can create a fixed-core defect even when
the forced-port graph has another singleton block.  For existence of some
compiler core, the forced-port statement is the relevant invariant.

### Theorem 3.2 (adaptive two-orbit compiler)

There exists an equivariant one-core and a physical assignment saturating
all members of \(U\cup E_5\) if and only if

\[
 \mathcal L\ne\varnothing,\qquad
 \mathcal E\ne\varnothing,\qquad
                         |\mathcal L\cup\mathcal E|\ge2.
\tag{3.8}
\]

#### Proof

Necessity of the first two conditions is unary eligibility.  If their
union has only one right orbit, eighteen physical targets have only fifteen
physical positions, so assignment is impossible.

Conversely, (3.8) permits distinct blocks

\[
                         J_U\in\mathcal L,\qquad
                         J_E\in\mathcal E.
\tag{3.9}
\]

At a representative of \(J_U\), write \(F_i=\{a\}\).  Equivariance and
unit voltage make the fifteen copies

\[
                         F_{i+tN}=\{a+tv\}
\tag{3.10}
\]

run through all singleton targets exactly once.  Assign those targets to
these fifteen positions.  The orbitwise forced-port lemma constructs an
equivariant one-core contained in each assigned singleton.

At \(J_E\), every physical \(E_5\) target equals the corresponding
rank-five envelope at five positions.  Choose one position for each of
the three targets.  These assignments impose no core omission because
the assigned target equals \(P\).  The two right blocks are disjoint, so
the preceding singleton construction and these three assignments coexist.
\(\square\)

This completely settles the two-orbit compiler once the two marked block
sets are known.  The carrier question is precisely whether the full strict
chronology forces (3.8).

## 4. Local normal form of the unique common block

Assume a common block has a representative with

\[
                         P_i=Q,\qquad F_i=\{x\}.
\tag{4.1}
\]

Then \(x\in Q\), and there are \(b,c\notin Q\) such that

\[
 P_{i-1}=Q-\{x\}+\{b\},
\qquad
 P_{i+1}=Q-\{x\}+\{c\}.
\tag{4.2}
\]

Because \(D^2P\) has rank seven,

\[
 |P_{i-1}\cup P_i\cup P_{i+1}|
 =|Q\cup\{b,c\}|=7,
\tag{4.3}
\]

so

\[
                         b\ne c.
\tag{4.4}
\]

The physical translates are

\[
 P_{i+tN}=Q+tv,\qquad
 F_{i+tN}=\{x+tv\}.
\tag{4.5}
\]

Each of the fifteen singleton targets has one candidate in this block.
Each of the three \(E_5\) targets has five candidates.  Assigning all
singletons consumes all fifteen positions, which is the literal physical
meaning of the defect three.

### Proposition 4.1 (the incident q2 packet)

Let

\[
                         H=\{0,3,6,9,12\}=Q.
\tag{4.6}
\]

For the five physical occurrences whose center envelope is the fixed set
\(Q\), the two incident rank-six colours are

\[
 \{Q\cup\{b+h\}:h\in H\}
 \quad\text{and}\quad
 \{Q\cup\{c+h\}:h\in H\}.
\tag{4.7}
\]

If \(b\) and \(c\) lie in the two different nonzero cosets of \(H\), these
are exactly all ten rank-six supersets of \(Q\), each once.  Translating
the statement by one and two pays all thirty rank-six supersets of the
three exceptional rank-five targets.

#### Proof

The incoming and outgoing unions at the center are

\[
                         Q\cup\{b\},\qquad Q\cup\{c\}.
\]

The five shifts that fix \(Q\) are precisely the elements of \(H\).
Their translates give (4.7).  Each nonzero coset has five elements, and
the two nonzero cosets partition the ten labels outside \(Q\).  \(\square\)

Thus lower-q2 completeness is locally compatible with one exceptional
quotient block.  It can be paid optimally at the very same block.

## 5. A strict depth-three collar realizing the packet

Consider the following nine consecutive rank-five states:

\[
\begin{aligned}
P_{-4}&=\{1,4,7,10,12\},&
P_{-3}&=\{1,4,7,9,12\},\\
P_{-2}&=\{1,4,6,9,12\},&
P_{-1}&=\{1,3,6,9,12\},\\
P_0&=\{0,3,6,9,12\},&
P_1&=\{2,3,6,9,12\},\\
P_2&=\{2,5,6,9,12\},&
P_3&=\{2,5,8,9,12\},\\
P_4&=\{2,5,8,11,12\}.
\end{aligned}
\tag{5.1}
\]

The loss and gain labels on the eight displayed edges are

\[
\begin{array}{c|rrrrrrrr}
\text{edge start}&-4&-3&-2&-1&0&1&2&3\\ \hline
\text{loss}&10&7&4&1&0&3&6&9\\
\text{gain}&9&6&3&0&2&5&8&11.
\end{array}
\tag{5.2}
\]

### Theorem 5.1 (local strict-erosion compatibility)

Every consecutive two-, three-, and four-state union contained in (5.1)
has rank \(6,7,8\), respectively.  Every contained five-state union has
rank nine.  Moreover,

\[
                         F_0=\{0\},
\tag{5.3}
\]

while every other fully determined interior forced port in the collar has
size two.  The two incident q2 colours at the center are

\[
                         Q\cup\{1\},\qquad Q\cup\{2\}.
\tag{5.4}
\]

#### Proof

Each edge in (5.2) is a strict Johnson swap.  In every group of three
successive edges, the three gain labels are distinct and absent from the
state at the start of the group.  Hence every four-state union has rank
\(5+3=8\).  The same inspection with four successive gains gives rank
nine for every five-state union.  The pair and triple assertions follow
from the first one or directly from (5.2).

At \(P_0\), the entering label from \(P_{-1}\) is zero and the leaving
label toward \(P_1\) is zero, proving (5.3).  At the other determined
positions the entering and leaving labels, read from adjacent columns of
(5.2), are distinct.  Equation (5.4) is immediate.  \(\square\)

The rank-nine five-window check is the local no-short-return condition:
within the collar it prevents a coordinate from leaving and re-entering
inside four positions.  It certifies the erosion identity for windows wholly
inside the collar; an extension must retain the same no-short-return rule at
the two boundaries.  The \(N\)-spaced equivariant copies of this collar are
disjoint because \(N=429\).

Under the five shifts in \(H\), (5.4) becomes

\[
                         Q\cup\{1+h\},\qquad Q\cup\{2+h\},
\]

and Proposition 4.1 applies.  Therefore three-residence and all q2 colours
incident with \(E_5\) admit the defect-three local geometry.

## 6. No targetwise support argument forces a second exceptional block

The preceding packet treats q2.  There is a uniform bypass at every larger
rank.

### Theorem 6.1 (mixed-anchor facet path)

Let \(S\subseteq\mathbb Z_{15}\) have size \(s\ge6\).  There is a strict
Johnson path of \(s-4\) rank-five states,

\[
                         V_1,V_2,\ldots,V_{s-4},
\tag{6.1}
\]

such that

\[
                         \bigcup_{j=1}^{s-4}V_j=S
\tag{6.2}
\]

and no \(V_j\) belongs to \(E_5\).

#### Proof

No set of size at least six lies in one residue class modulo three.
Choose a four-set \(A\subseteq S\) meeting at least two residue classes,
and enumerate

\[
                         S\setminus A=\{x_1,\ldots,x_{s-4}\}.
\]

Put

\[
                         V_j=A\cup\{x_j\}.
\tag{6.3}
\]

Consecutive states differ by the swap \(x_j\to x_{j+1}\), so the path is
strict Johnson.  Its union is \(S\).  Every state contains the mixed set
\(A\), whereas every member of \(E_5\) is one full residue class modulo
three.  Hence the path avoids \(E_5\).  \(\square\)

At \(s=6\), this is a q2 witness; at \(s=7\), it is a lower-q1 witness; at
\(s=8\), it is a middle-support witness; and for \(9\le s\le15\), it is a
minimal upper-support interval.  Consequently no individual lower or upper
target of rank at least six forces a second occurrence of an exceptional
rank-five state.  Only rank-five q3 itself forces

\[
                         |\mathcal E|\ge1.
\tag{6.4}
\]

The theorem is deliberately targetwise.  Its paths have not been packed
simultaneously into one exact middle Hamilton chronology.  That simultaneous
packing is exactly where a valid global exclusion could still live.

## 7. Scalar chronology ledgers also permit uniqueness

Every transition of the rank-five \(P\)-walk starts one coordinate run.
Equivariance groups the \(W\) physical runs into \(N=429\) free run orbits.
Let \(n_\ell\) be the number of quotient run orbits of length \(\ell\).
Then

\[
                         \sum_{\ell\ge1}n_\ell=429,
\qquad
                         \sum_{\ell\ge1}\ell n_\ell=5\cdot429=2145.
\tag{7.1}
\]

There is a bijection

\[
                         \mathcal L
 \longleftrightarrow
                         \{\text{run orbits of length one}\},
\tag{7.2}
\]

so

\[
                         |\mathcal L|=n_1.
\tag{7.3}
\]

The scalar identities do not forbid \(n_1=1\).  For example, the formal
distribution

\[
                         n_1=1,\qquad n_5=427,\qquad n_9=1
\tag{7.4}
\]

satisfies both equations in (7.1), as well as the required odd-run parity.
This is only an arithmetic feasibility witness, not a construction of the
whole carrier.

Similarly let \(e=|\mathcal E|\), and let \(c_O\) be the number of quotient
blocks whose rank-five envelope lies in a full rank-five orbit \(O\).
Lower-q3 completeness gives

\[
                         e\ge1,\qquad c_O\ge1,
\qquad
                         e+\sum_{O\ {\rm full}}c_O=429.
\tag{7.5}
\]

The value \(e=1\) is arithmetically compatible: among the 200 full orbits,
take 172 multiplicities equal to two and 28 multiplicities equal to three,
whose sum is 428.  Again, exact middle chronology may impose additional
correlations, but no degree or floor ledger rules out the unique block.

## 7A. A global support-complete FIFO/hourglass obstruction

The local collar can be globalized if exact middle-deck injectivity is
temporarily removed.  This separates support completeness from the exact
factor property.

### Lemma 7A.1 (FIFO controller)

Let \(z=(z_i)\) be a finite linear or cyclic symbol word on
\(\mathbb Z_{15}\) such that

1. every nine consecutive symbols are distinct; and
2. no five consecutive symbols lie in one residue class modulo three.

On a FIFO region define

\[
                         P_i=\{z_i,z_{i+1},z_{i+2},z_{i+3},z_{i+4}\}.
\tag{7A.1}
\]

Then:

\[
 |P_i\cup\cdots\cup P_{i+j}|=5+j
                         \qquad(0\le j\le4),
\tag{7A.2}
\]

\[
 T_i:=P_i\cup P_{i+1}\cup P_{i+2}\cup P_{i+3}
     =\{z_i,\ldots,z_{i+7}\},
\tag{7A.3}
\]

and \(T\) is a rank-eight Johnson chronology.  The maximal cyclic
three-erosion of \(T\) is \(P\).  Every forced port in the FIFO region has
size two:

\[
                         F_i=\{z_i,z_{i+4}\}.
\tag{7A.4}
\]

No FIFO state \(P_i\) belongs to \(E_5\).

#### Proof

Equation (7A.2) follows because the relevant nine-symbol window is
injective.  Consecutive \(P\)-states drop \(z_i\) and gain \(z_{i+5}\);
consecutive \(T\)-states drop \(z_i\) and gain \(z_{i+8}\).  The nine-symbol
condition makes both swaps strict.

One occurrence of a symbol in \(z\) produces a five-state positive run in
\(P\) and an eight-state positive run in \(T\).  Successive occurrences of
the same symbol are separated by at least nine symbol positions, so the
corresponding \(P\)-runs have at least four zero positions between them.
Depth-three dilation and maximal erosion therefore recover one another
run by run.  Formula (7A.4) is the FIFO loss/gain pair, whose labels are
distinct.  The second word condition excludes an \(E_5\) state.  \(\square\)

### Lemma 7A.2 (the hourglass)

Write

\[
                         Q=\{c,q_1,q_2,q_3,q_4\},
\tag{7A.5}
\]

and choose eight distinct labels

\[
                         a,b,u,v,t,w,x,y\notin Q.
\tag{7A.6}
\]

Choose \(a\) and \(b\) in the two different nonzero residue classes modulo
three.  The remaining outside labels, together with the two boundary labels
introduced below, are split so that both boundary FIFO five-sets meet both
nonzero residue classes.

Replace one FIFO segment by

\[
\begin{aligned}
P_{-4}&=Q-\{c,q_1,q_2,q_3\}+\{a,u,v,t\},\\
P_{-3}&=Q-\{c,q_1,q_2\}+\{a,u,v\},\\
P_{-2}&=Q-\{c,q_1\}+\{a,u\},\\
P_{-1}&=Q-\{c\}+\{a\},\\
P_0&=Q,\\
P_1&=Q-\{c\}+\{b\},\\
P_2&=Q-\{c,q_1\}+\{b,w\},\\
P_3&=Q-\{c,q_1,q_2\}+\{b,w,x\},\\
P_4&=Q-\{c,q_1,q_2,q_3\}+\{b,w,x,y\}.
\end{aligned}
\tag{7A.7}
\]

It can be attached to FIFO histories on both sides.  Every five consecutive
states meeting the hourglass have union of rank nine.  Its only singleton
forced port is

\[
                         F_0=\{c\}.
\tag{7A.8}
\]

No state other than \(P_0\) lies in \(E_5\).

The five \(Q\)-coordinate run lengths through the packet are

\[
                         1,3,5,7,9.
\tag{7A.9}
\]

Their deviations from the exact mean-five run ledger are

\[
                         -4,-2,0,2,4,
\tag{7A.10}
\]

which sum to zero.

#### Proof

The left side is the FIFO queue with ordered windows

\[
\begin{split}
(t,v,u,a,q_4),\quad
(v,u,a,q_4,q_3),\quad
(u,a,q_4,q_3,q_2),\\
(a,q_4,q_3,q_2,q_1),\quad
(q_4,q_3,q_2,q_1,c).
\end{split}
\tag{7A.11}
\]

The center transition removes the newest label \(c\), rather than the
oldest label \(q_4\), and inserts \(b\).  This is the one queue reversal.
The right side resumes FIFO with ordered windows

\[
\begin{split}
(q_1,q_2,q_3,q_4,b),\quad
(q_2,q_3,q_4,b,w),\\
(q_3,q_4,b,w,x),\quad
(q_4,b,w,x,y).
\end{split}
\tag{7A.12}
\]

Choose the preceding FIFO window to end in
\((s,t,v,u,a)\) and the following one to begin
\((b,w,x,y,z)\), where \(s,z\) are the two unused labels outside \(Q\).
Distribute the ten outside labels so that each of these two five-sets meets
both nonzero residue classes modulo three.  In particular neither boundary
FIFO state is another member of \(E_5\).  The ports at the two seams then
also have size two.

The five-state unions beginning at \(-4,-3,-2,-1,0\) are respectively

\[
\begin{aligned}
Q+\{a,u,v,t\},\quad&
Q+\{a,u,v,b\},\\
Q+\{a,u,b,w\},\quad&
Q+\{a,b,w,x\},\\
Q+\{b,w,x,y\},
\end{aligned}
\tag{7A.13}
\]

all of rank nine.  Inspection of adjacent loss/gain labels gives (7A.8).
The coordinate \(c\) occurs only at \(P_0\); \(q_1,q_2,q_3,q_4\) occur on
the centered intervals of lengths \(3,5,7,9\).  This proves
(7A.9)--(7A.10).  \(\square\)

The six affected middle states are

\[
\begin{aligned}
T_{-4}&=(Q-\{c\})+\{a,u,v,t\},\\
T_{-3}&=Q+\{a,u,v\},\\
T_{-2}&=Q+\{a,u,b\},\\
T_{-1}&=Q+\{a,b,w\},\\
T_0&=Q+\{b,w,x\},\\
T_1&=(Q-\{c\})+\{b,w,x,y\}.
\end{aligned}
\tag{7A.14}
\]

They are distinct rank-eight states, and consecutive states differ by the
strict swaps

\[
                         t\leftrightarrow c,\quad
v\leftrightarrow b,\quad
u\leftrightarrow w,\quad
a\leftrightarrow x,\quad
c\leftrightarrow y.
\tag{7A.15}
\]

The five local rank-seven edge colours are

\[
\begin{split}
(Q-\{c\})+\{a,u,v\},\quad
Q+\{a,u\},\quad Q+\{a,b\},\\
Q+\{b,w\},\quad
(Q-\{c\})+\{b,w,x\},
\end{split}
\tag{7A.15a}
\]

and are also physically distinct.  Thus neither local physical middle-state
injectivity nor local q1-colour injectivity rejects the hourglass.  Exact
quotient-orbit injectivity across the whole factor remains missing.

### Lemma 7A.3 (FIFO history connector)

Consider ordered eight-symbol histories with distinct entries and no five
consecutive entries in one residue class modulo three.  Permit a transition
that drops the oldest entry and appends a symbol outside the current
history, provided the residue condition remains true.  This directed
history graph is strongly connected.

It can moreover be routed through any prescribed finite block of distinct
symbols whose order has no monochromatic five-subblock.

#### Proof

Let the current eight-set be \(H\).  Append the seven labels of \(H^c\),
then append the eight labels of \(H\) in a chosen order.  All seven
complement labels are initially legal.  After they have been appended, only
the youngest old label remains.  Choose a different first reinserted label;
the remaining old label is dropped and may be inserted later.  This returns
to the set \(H\) in the chosen order.  If the desired first label is the one
temporarily retained, perform two such refresh loops.  Within each block,
interleave residue classes; a block of seven or eight distinct labels cannot
lie in one five-element residue class, so the order can also be chosen to
avoid a monochromatic run of five, including at the two boundaries.

Now let the desired history set be \(K\).  If \(H\ne K\), reorder \(H\)
so that some \(a\in H\setminus K\) is oldest and its final four entries are
not all in the residue class of some \(b\in K\setminus H\).  Appending \(b\)
drops \(a\), preserves the residue condition, and increases
\(|H\cap K|\).  Iterate, then use a refresh loop to obtain the desired
order.  This proves strong connectivity.

For a prescribed block of at most seven symbols, first reach an
eight-history disjoint from it.  For a block
\(w_1,\ldots,w_s\) with \(s\ge8\), first reach the ordered history

\[
                         (w_8,c_1,\ldots,c_7),
\tag{7A.16}
\]

where \(c_1,\ldots,c_7\) are the complement of
\(\{w_1,\ldots,w_8\}\), and place \(w_8\) oldest.  Appending
\(w_1,\ldots,w_s\) is then legal: \(w_8\) is dropped before it is
reinserted, and after the first eight insertions the current history is
\((w_1,\ldots,w_8)\).  The residue interleaving may be built into the
chosen block order and the preparatory history.  \(\square\)

### Theorem 7A.4 (global support-complete obstruction)

There exists a finite cyclic rank-five Johnson walk \(P\), with a free
order-15 shift \(\sigma\), such that

\[
                         P_{\sigma i}=P_i+1,
\tag{7A.17}
\]

and all of the following hold.

1. \(P\) is the maximal three-erosion of \(T=D^3P\), and \(T\) is a
   three-resident rank-eight Johnson walk.

2. For every \(S\subseteq\mathbb Z_{15}\) with \(5\le|S|\le15\), some
   \(|S|-4\) consecutive \(P\)-states have union \(S\).

3. Exactly one \(\sigma\)-orbit \(J_*\) has \(P_i\in E_5\).

4. Exactly the same orbit \(J_*\) has \(|F_i|=1\); all other forced ports
   have size two.

5. There is one equivariant one-core that makes every target orbit of ranks
   one through five have positive degree.

6. No equivariant one-core has a target-saturating Hall matching.

The walk is not asserted to have length 6435, its middle row \(T\) is not
asserted to enumerate every rank-eight set exactly once, and \(D^2P\) is
not asserted to give the exact rank-seven rainbow of a middle wreath
factor.

#### Proof

Choose one representative from every translation orbit of every target
rank \(5,\ldots,15\), except that the exceptional rank-five orbit will be
supplied by the hourglass.  For a representative \(S\notin E_5\), order
its elements as a distinct symbol block with no monochromatic run of five.
Its \(s-4\) FIFO five-windows have union \(S\).  Such an order always
exists: a residue class has only five labels, and the only rank-five set
for which all five are forced consecutive is a member of \(E_5\).

For every translation-orbit representative \(S\) of rank two, three, or
four, choose a mixed five-symbol block containing \(S\), with its first and
last symbols in \(S\).  At its FIFO window,

\[
                         F_i\subseteq S\subseteq P_i.
\tag{7A.18}
\]

The singleton orbit is supplied at the hourglass center.  Put buffers of
at least two positions between all these marked lower-target windows.

Use Lemma 7A.3 to concatenate this finite packet list, inserting the single
hourglass from Lemma 7A.2.  Choose an initial admissible ordered history
\(H\), and use one final connector so that the terminal history is
\(\rho H\).  Concatenate the fifteen translated blocks

\[
                         B,\rho B,\ldots,\rho^{14}B
\tag{7A.19}
\]

by identifying the matching terminal and initial eight-histories.  After
the fifteenth block the construction closes.  Translation by one block is
the free order-15 action \(\sigma\).

All FIFO portions satisfy Lemma 7A.1.  Lemma 7A.2 and its boundary histories
preserve the same rank-nine five-window condition through the sole
hourglass.  Hence \(P\) is the maximal erosion of \(T=D^3P\), and \(T\) is
three-resident Johnson.

Every target representative of rank at least five has its displayed
support interval; the translated blocks give all physical targets.  FIFO
states avoid \(E_5\), and every noncentral hourglass state is mixed.
Therefore \(J_*\) is the unique exceptional-envelope orbit.  FIFO ports
have size two, all noncentral hourglass ports have size two, and its center
port is a singleton.  Thus

\[
                         \mathcal E=\mathcal L=\{J_*\}.
\tag{7A.20}
\]

For ranks five, six, seven, and eight, the intervals in item 2 are
respectively cells of \(P,DP,D^2P,D^3P\).  For \(s\ge8\), the union of
the \(s-4\) consecutive \(P\)-states is equivalently the union of the
corresponding \(s-7\) consecutive \(T=D^3P\) states.  Thus item 2 is
literal lower-q3, lower-q2, lower-q1, middle, and all-upper support
completeness, not merely an abstract subset census.

For the marked targets of ranks one through four, take the union of their
orbit-closed mandatory omissions \(P_i\setminus S\).  Port containment
(7A.18) keeps every omission away from a run endpoint.  The buffers and
their translated copies make distinct marked positions nonadjacent, so the
omission union contains no adjacent pair.  The adaptive one-core theorem
therefore supplies one equivariant core protecting all marked targets.
Rank-five targets equal their envelope at a supplied position and impose
no omission.  This proves positive degree for every target orbit.

Finally, for any equivariant one-core, \(E_5\) has only the block \(J_*\).
If the singleton orbit has zero degree, Hall already fails.  If it has
positive degree, its neighborhood is contained in
\(\mathcal L=\{J_*\}\), so

\[
                         15+3>15
\]

is the defect-three Hall cut.  Hence no one-core passes Hall.  \(\square\)

Theorem 7A.4 is a genuine global obstruction to every support-only version
of the desired theorem.  Its missing property is the exact middle/q1
factor: length 6435, exact-once rank-eight deck injectivity, and the exact
rank-seven rainbow are not enforced.

## 8. What the full chronology would still have to prove

The desired global conclusion is

\[
 \boxed{|\mathcal L\cup\mathcal E|\ge2.}
\tag{8.1}
\]

The proved information is:

1. three-residence converts \(\mathcal L\) into the set of exact four-step
   returns \(\beta_{i-4}=\alpha_i\);
2. lower q3 gives only \(|\mathcal E|\ge1\);
3. the unique common block has an exact resident collar;
4. its stabilizer copies can pay every incident q2 colour;
5. every individual larger support target has an \(E_5\)-avoiding facet
   path; and
6. all scalar occurrence and run equations permit
   \(|\mathcal L|=|\mathcal E|=1\); and
7. Theorem 7A.4 composes these ingredients into one equivariant,
   support-complete, maximal-erosion cyclic walk with the unique common
   block.

Therefore (8.1) is not a consequence of residence, equivariance, maximal
erosion, or even simultaneous completeness of all support layers.  In the
present strict-carrier class, the unexploited constraint is that the
rank-eight \(T\)-row is one exact Hamilton ordering of all 6435 middle
sets, with the exact lower-rank rainbow and all support intervals embedded
in that same order.

No proof of (8.1) from that exact-factor constraint is given here.
Theorem 7A.4 is a global counterexample only to the support-complete relaxed
statement; it is not a 6435-state exact middle factor.  This is the precise
proved/conditional boundary.

Within the FIFO/hourglass architecture, the missing condition has a sharp
universal-cycle form.  On every FIFO position,

\[
                         T_i=\{z_i,z_{i+1},\ldots,z_{i+7}\}.
\tag{8.2}
\]

Exact middle-deck injectivity would require the cyclic eight-symbol windows,
together with the finitely many hourglass-crossing states, to list every
eight-subset of \(\mathbb Z_{15}\) exactly once in 6435 positions.  The
hourglass is one controlled queue-reversal orbit inside that universal
cycle.  Thus the middle-deck part of extending Theorem 7A.4 is equivalent,
in this architecture, to admitting such a universal cycle with one
queue-reversal orbit; excluding it means proving that every such reversal
forces another singleton-port or exceptional-envelope orbit.  A full
strict extension must additionally retain any separately imposed exact
lower-q1 rainbow.

## 9. The one-new-block theorem for all minimal circuits

Let \(G\) be any of the quotient graphs \(G_P,G_F,G_C\), with right
capacity 15.  If \(X\) is an inclusion-minimal positive-degree deficient
shore, the preceding minimal-circuit theorem gives one of

\[
\begin{array}{c|c}
\text{type}&w(X)-15|N_G(X)|\\ \hline
F&15\\
E_3&5\\
E_5&3.
\end{array}
\tag{9.1}
\]

### Corollary 9.1 (one-new-block repair cut)

For every such \(X\),

\[
 \left\lceil{w(X)\over15}\right\rceil
                         =|N_G(X)|+1.
\tag{9.2}
\]

Thus the exact Hall cut for a minimal circuit always asks for one additional
distinct quotient neighbor, independently of whether its defect is
15, 5, or 3.

#### Proof

In the three cases, \(w(X)\) equals respectively

\[
 15|N_G(X)|+15,\qquad
 15|N_G(X)|+5,\qquad
 15|N_G(X)|+3.
\]

Taking the ceiling after division by fifteen gives (9.2).  \(\square\)

This is the common finite carrier cut behind all three circuit types.

## 10. Exact finite lazy cuts for the carrier master

### 10.1 Six-state reification of the exceptional cut

The three eroded states needed at an anchor are

\[
\begin{aligned}
P_{i-1}&=T_{i-4}\cap T_{i-3}\cap T_{i-2}\cap T_{i-1},\\
P_i&=T_{i-3}\cap T_{i-2}\cap T_{i-1}\cap T_i,\\
P_{i+1}&=T_{i-2}\cap T_{i-1}\cap T_i\cap T_{i+1}.
\end{aligned}
\tag{10.1}
\]

Hence both predicates

\[
 e_j={\bf1}_{J_j\in\mathcal E},
\qquad
 s_j={\bf1}_{J_j\in\mathcal L}
\tag{10.2}
\]

are functions of a directed six-middle-state collar, or five consecutive
selected middle arcs.  Relative shifts on those arcs determine the physical
phase.  They can therefore be reified by a finite allowed-path table in the
existing carrier CP model; no one-core variables are required.

The exact exceptional-port conditions are

\[
                         \sum_j e_j\ge1,
\qquad
                         \sum_j s_j\ge1,
\tag{10.3}
\]

and

\[
 \boxed{
 \sum_{k\ne j}(e_k+s_k)\ge1
 \qquad(j=0,\ldots,428).
 }
\tag{10.4}
\]

Under (10.3), the family (10.4) is equivalent to
\(|\mathcal E\cup\mathcal L|\ge2\).  If an incumbent has the unique common
block \(J_*\), only the single violated inequality

\[
                         \sum_{k\ne *}(e_k+s_k)\ge1
\tag{10.5}
\]

need be added.  It says exactly: create another exceptional envelope block
or another singleton forced-port block.  It is stronger and more reusable
than a whole-carrier no-good.

One implementation may introduce a Boolean for every feasible marked
five-arc path and identify it with the conjunction of its selected arc
literals.  A more compact implementation may use the same finite
state-path machinery already used for shadow witnesses.  The mathematical
cut is (10.5), independent of encoding choice.

Explicitly, if \(\pi\) is a feasible five-arc collar and \(a_r\) are its
five carrier-arc literals, its conjunction flag \(z_\pi\) is defined by

\[
 z_\pi\le a_r\quad(r\in\pi),
\qquad
 z_\pi\ge\sum_{r\in\pi}a_r-4.
\tag{10.5a}
\]

Anchor collars by the middle quotient vertex at their distinguished
position.  The selected circuit supplies exactly one collar through each
anchor, so \(e_j\) and \(s_j\) are the sums of the corresponding marked
\(z_\pi\)'s.  This indexing uses stable middle-orbit anchors, not an
unknown numerical traversal order.  In a lazy implementation only collars
needed by the violated cut have to be materialized.

### 10.2 General forced-port Hall cuts

For a target orbit \(O\) and quotient block \(J\), define the exact
carrier predicate

\[
 y^F_{O,J}
 ={\bf1}\{\text{some relative phase has }
                    F_i\subseteq S\subseteq P_i,\ S\in O\}.
\tag{10.6}
\]

For a target shore \(X\), reify

\[
                         n^F_{X,J}=\bigvee_{O\in X}y^F_{O,J}.
\tag{10.7}
\]

Then the exact carrier-only Hall cut for \(X\) is

\[
 \boxed{
 \sum_{J\in\mathcal J}n^F_{X,J}
 \ge
 \left\lceil{\sum_{O\in X}w(O)\over15}\right\rceil.
 }
\tag{10.8}
\]

This inequality is globally valid for every carrier because its left side
is exactly \(|N_F(X)|\).  The complete finite family (10.8) is equivalent
to weighted Hall in the forced-port graph.  It can be separated lazily:

1. reconstruct \(P,F\) for an incumbent carrier;
2. run the 331-by-429 weighted quotient max-flow on \(G_F\);
3. obtain a deficient shore \(X\) from the residual cut; and
4. add only (10.8) for that \(X\).

There are finitely many shores, so exact separation terminates.  When the
returned shore is inclusion-minimal, Corollary 9.1 says the new inequality
asks for exactly one additional block.

The forced-port family is the exact maximal-neighborhood, ordinary
unary-eligibility Hall test: if it fails, no one-core can repair the
carrier.  Passing it does not by itself synchronize the mandatory omissions
of different assignment edges; the carrier-dependent pair-conflict cuts
below are strictly stronger.

### 10.3 Fixed-core Hall cuts

If the master explicitly chooses an equivariant one-core, replace (10.6)
by

\[
 y^C_{O,J}
 ={\bf1}\{\text{some phase has }
                    C_i\subseteq S\subseteq P_i,\ S\in O\},
\tag{10.9}
\]

and replace \(n^F\) by \(n^C\) in (10.8).  The resulting finite cut family
is necessary and sufficient for weighted Hall of that chosen core.

Fixing a canonical core is not without loss: failure may be repaired by a
different run phase.  Thus (10.9) is exact for a joint carrier-core master,
but it must not be used to reject a carrier when the core is external and
still adaptive.

### 10.4 Exact adaptive-core completion

There is also a finite formulation that retains adaptive core choice
without explicit core letters.  For every physical target-position edge
\(e=(S,i)\), let

\[
                         y_e^F={\bf1}_{F_i\subseteq S\subseteq P_i}
\tag{10.10}
\]

and introduce an assignment variable \(m_e\).  Impose

\[
\begin{aligned}
\sum_i m_{S,i}&=1 &&\text{for every physical target }S,\\
\sum_S m_{S,i}&\le1 &&\text{for every physical position }i,\\
m_e&\le y_e^F &&\text{for every edge }e.
\end{aligned}
\tag{10.11}
\]

For \(e=(S,i)\), its mandatory orbit-closed omissions are

\[
 Z(e)=
 \{\,(i+tN,x+tv):
          x\in P_i\setminus S,\ t\in\mathbb Z_{15}\,\}.
\tag{10.12}
\]

Two port-legal edges \(e,f\) conflict when \(Z(e)\cup Z(f)\) contains
adjacent omitted occurrences in one coordinate run.  Let
\(\chi_{e,f}(P)\) be this exact carrier-dependent conflict predicate.
Add

\[
                         m_e+m_f\le2-\chi_{e,f}(P).
\tag{10.13}
\]

When \(\chi=1\), this is the pair-conflict clause; when \(\chi=0\), it is
vacant.  The adaptive one-core theorem proves that (10.10)--(10.13) are
necessary and sufficient, within the occurrence-injective graded
architecture, for a target-saturating assignment protected by one common
equivariant \(C\subseteq P\) with \(DC=DP\).  There is no higher-order run
obstruction inside that scope.  This is not a characterization of arbitrary
literal contiguous-OR compilers outside the graded one-core architecture.

The predicates and pair clauses may also be separated lazily.  Because
short target orbits need not admit an equivariant injection into a free
right orbit, the final assignment variables in (10.11) are physical, even
though the Hall separator in (10.8) is quotient-weighted.

Equations (10.8) and (10.13) are therefore an exact finite complete
Hall/core cut package for the equivariant graded one-core architecture:

- (10.8) rejects an immutable forced-port capacity cut;
- (10.9) handles a core chosen inside the master; and
- (10.10)--(10.13) give the exact adaptive common-core compiler.

No SAT, exhaustive search, or carrier solve is needed to validate these
cuts.

## 11. Final verdict

The defect-three circuit is completely characterized:

\[
                         \mathcal L=\mathcal E=\{J_*\}.
\]

It is not ruled out by three-residence: it is an exact length-four
middle-row return.  It is not ruled out by lower q2: the stabilizer copies
of one collar can cover every incident q2 target.  It is not ruled out by
lower q3: one quotient block is the minimum positive multiplicity.  No
individual upper target forces a second exceptional state.  The
FIFO/hourglass theorem shows that even simultaneous support completeness at
all ranks, maximal erosion, and equivariance do not force a second block
when exact middle-deck injectivity is removed.

The full strict-carrier question remains:

\[
\begin{split}
 &\text{exact 6435-state middle Hamilton deck}
 +\text{ three-residence}
 +\text{ lower q2/q3 completeness}
 +\text{ all upper supports}\\
 &\hspace{32mm}\stackrel{?}{\Longrightarrow}
 |\mathcal L\cup\mathcal E|\ge2.
\end{split}
\tag{11.1}
\]

Implication (11.1) is not proved, and there is no global strict exact-factor
counterexample.  Theorem 7A.4 shows that removing the exact middle/q1
factor-injectivity package makes the implication false.  The next positive
proof must therefore use that global exact-factor constraint.  Until then,
the finite marked path cut (10.5) is the precise way to enforce the missing
conclusion in the carrier CP model.
