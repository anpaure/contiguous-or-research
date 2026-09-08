# Exact common-`Q` criterion for the one-cell star-hidden two-fan ear

Date: 2026-08-01  
Lane: A, literal compiler/common-cap interface  
Status: exact local theorem.  This note combines the frozen fan--crossing
identity with the positive-cover/common-`Q` criterion.  It characterizes one
complete local cap state.  It does not plant that state in a global carrier,
protect exterior witnesses automatically, or prove an all-`k` construction.

## 0. Result

Put a new source letter at position `0` and retain the `2d-2` old side
positions

\[
 -(d-1),\ldots,-1,1,\ldots,d-1 .
\]

The `2d-1` fan cells and the `d-1` destroyed crossing cells cannot be assigned
independently.  Nevertheless their **literal common-cap problem has an exact
closed form**.  Intersect, at each source position, its legal cap with every
assigned target whose interval contains that position.  The resulting sets
\(K_p\) form the unique componentwise maximal candidate word.  A nonzero
common-`Q` word exists if and only if the unions of the \(K_p\)'s reproduce
all assigned targets exactly.

For unrestricted local caps this reduces to a two-threshold Ferrers law.
Coordinates outside the star are forced by the two nested fan chains;
coordinates in the star are programmable precisely through interval-zero
crossing traces.  For the complementary coatom chains, every filler and every
base coordinate outside the star is forced into **every** crossing target.
Only coordinates in the common star can distinguish the crossings.

If the \(d-1\) crossing targets are required to be pairwise distinct, a star
bank of size \(h\) can encode at most \(2h\) of them.  Hence

\[
             |Z|\ge \left\lceil{d-1\over2}\right\rceil                 \tag{0.1}
\]

is necessary, and the interval-zero code attaining this bound is explicit.
This is a trace bound, not a cap theorem: the required copies of the hidden
coordinates must still lie in their literal side caps.

## 1. Geometry and cap state

Fix \(d\ge2\).  Let \(A_p\ne\varnothing\) be the source letter at position
\(p\in\{0,\pm1,\ldots,\pm(d-1)\}\).  Define

\[
 L_h=\bigcup_{t=0}^{h-1}A_{-t},\qquad
 R_h=\bigcup_{t=0}^{h-1}A_t,
 \qquad 1\le h\le d,                                      \tag{1.1}
\]

where \(A_{-0}=A_0\), and put

\[
 Z=L_1=R_1=A_0.                                           \tag{1.2}
\]

For \(1\le i<d\), the old length-\(d\) crossing cell is

\[
 C_i=\bigcup_{t=1}^{i}A_{-t}\ \cup\
     \bigcup_{t=1}^{d-i}A_t.                              \tag{1.3}
\]

The authoritative seam identity is

\[
             \boxed{Z\cup C_i=L_{i+1}\cup R_{d-i+1}}.     \tag{1.4}
\]

Let \(P_p\) be the coordinates still allowed at position \(p\) after every
fixed exterior negative pin and carrier cap has been imposed.  Thus a legal
word must satisfy \(A_p\subseteq P_p\).  A positive row meeting both the ear
and frozen exterior positions has a fixed exterior OR contribution \(E_J\).
Such a row must be included below as
\(E_J\cup\bigcup_{p\in J}A_p=T_J\); dropping \(E_J\) would overconstrain the
local word.  Rows with a protected complete witness outside the ear require
no local positive condition.

## 2. The maximal common-`Q` word

We first record the architecture-free form.  Let \({\cal R}\) be a family of
physical rows \(J\) on the local positions, assign a target \(T_J\) to each
row, and let \(E_J\) be its fixed exterior OR contribution.  For wholly local
rows put \(E_J=\varnothing\).  Define

\[
 K_p=P_p\cap\bigcap_{J\in{\cal R}:\,p\in J}T_J .           \tag{2.1}
\]

An empty intersection over rows is interpreted as the whole ground set.

### Theorem 2.1 (maximal-letter common-`Q` equivalence)

There is a word of nonempty letters \(A_p\subseteq P_p\) satisfying

\[
                    E_J\cup\bigcup_{p\in J}A_p=T_J
                    \qquad(J\in{\cal R})                 \tag{2.2}
\]

if and only if

\[
 E_J\subseteq T_J\quad(J\in{\cal R}),\qquad
 K_p\ne\varnothing\quad\hbox{for every }p,                \tag{2.3}
\]

and

\[
                    T_J=E_J\cup\bigcup_{p\in J}K_p
                    \qquad(J\in{\cal R}).                 \tag{2.4}
\]

When these conditions hold, \(A_p=K_p\) is the unique componentwise maximal
legal word.

#### Proof

If \(A\) is feasible, then \(E_J\subseteq T_J\).  If \(p\in J\), every
coordinate of \(A_p\) also lies in \(T_J\).  Together with
\(A_p\subseteq P_p\), this gives \(A_p\subseteq K_p\).  Hence every \(K_p\)
is nonempty and

\[
 T_J=E_J\cup\bigcup_{p\in J}A_p
    \subseteq E_J\cup\bigcup_{p\in J}K_p.
\]

The reverse inclusion follows from \(E_J\subseteq T_J\) and (2.1), because
every \(K_p\) with \(p\in J\) is contained in \(T_J\).  This proves
(2.3)--(2.4).  Conversely, (2.3)--(2.4) say exactly that the word
\(A_p=K_p\) is nonzero, respects every cap, and realizes every row.  Any
other feasible word is componentwise contained in it.  \(\square\)

For the star-hidden ear, take the rows in (1.1)--(1.3).  The maximal letters
are

\[
 K_0=P_0\cap Z\cap\bigcap_{h=2}^{d}L_h
                   \cap\bigcap_{h=2}^{d}R_h,              \tag{2.5}
\]

\[
 K_t^-=P_{-t}\cap\bigcap_{i=t}^{d-1}C_i
                    \cap\bigcap_{h=t+1}^{d}L_h,
       \qquad 1\le t<d,                                   \tag{2.6}
\]

and

\[
 K_t^+=P_t\cap\bigcap_{i=1}^{d-t}C_i
                   \cap\bigcap_{h=t+1}^{d}R_h,
       \qquad 1\le t<d.                                   \tag{2.7}
\]

Therefore Theorem 2.1 becomes the following completely explicit test:

\[
 \boxed{
 \begin{aligned}
  Z&=K_0,\\
  L_h&=K_0\cup\bigcup_{t<h}K_t^- &&(2\le h\le d),\\
  R_h&=K_0\cup\bigcup_{t<h}K_t^+ &&(2\le h\le d),\\
  C_i&=\bigcup_{t\le i}K_t^-\cup
       \bigcup_{t\le d-i}K_t^+ &&(1\le i<d),
 \end{aligned}}                                           \tag{2.8}
\]

together with nonemptiness of every displayed \(K\)-set.

Failure of one equality in (2.8) is exactly a positive-cover obstruction:
some required coordinate has had all of its legal positions erased.  An
empty \(K_p\) is exactly an empty-position obstruction.  Thus (2.8), rather
than separate fan and crossing Hall tests, is the literal common-`Q` gate.

## 3. Target-only Ferrers normal form

Now take unrestricted local caps \(P_p=\Omega\).  For a coordinate \(x\),
let \(z_x={\bf1}_{x\in Z}\), and let

\[
 \alpha_x,\beta_x\in\{1,\ldots,d-1,\infty\}              \tag{3.1}
\]

be its first left and right side distances.  The exact coordinate traces are

\[
 \begin{aligned}
 x\in L_h&\iff z_x=1\ \hbox{or}\ \alpha_x<h,\\
 x\in R_h&\iff z_x=1\ \hbox{or}\ \beta_x<h,\\
 x\in C_i&\iff \alpha_x\le i\ \hbox{or}\ \beta_x\le d-i.
 \end{aligned}                                             \tag{3.2}
\]

### Theorem 3.1 (target-only characterization)

The prescribed targets \(Z,L_2,\ldots,L_d,R_2,\ldots,R_d,C_1,\ldots,C_{d-1}\)
are realized by one nonzero local word if and only if all of the following
hold.

1. The fan chains are nested and have common nonempty base:

   \[
   \varnothing\ne Z\subseteq L_2\subseteq\cdots\subseteq L_d,
   \qquad
   Z\subseteq R_2\subseteq\cdots\subseteq R_d.            \tag{3.3}
   \]

2. Every coordinate outside the star is forced by the fans:

   \[
   C_i\setminus Z=
   (L_{i+1}\cup R_{d-i+1})\setminus Z
   \qquad(1\le i<d).                                      \tag{3.4}
   \]

3. For every \(z\in Z\), the zero set

   \[
                     \{i:z\notin C_i\}                   \tag{3.5}
   \]

   is an interval, possibly empty or all of \([1,d-1]\).

4. Both side words can be kept nonzero:

   \[
   L_2\cap\bigcap_{i=1}^{d-1}C_i\ne\varnothing,
   \qquad
   R_2\cap\bigcap_{i=1}^{d-1}C_i\ne\varnothing.          \tag{3.6}
   \]

Equivalently, there are parameters (3.1) satisfying (3.2), with some
\(\alpha_x=1\) and some \(\beta_x=1\).

#### Proof

Necessity of (3.3)--(3.5) is the frozen identity (1.4) and its threshold
form.  If \(A_{-1}\ne\varnothing\), every coordinate in \(A_{-1}\) lies in
\(L_2\) and in every crossing; this proves the first condition in (3.6),
and the right condition is symmetric.

Conversely, for \(x\notin Z\), take \(\alpha_x\) and \(\beta_x\) to be its
first fan-entry distances.  Equation (3.4) gives the last line of (3.2).
For \(z\in Z\), an interval of zeros \([a,b]\) is obtained by choosing a
left first occurrence at \(b+1\) when \(b<d-1\), and a right first occurrence
at \(d-a+1\) when \(a>1\); omit the corresponding occurrence at a boundary.
The empty and full zero intervals are obtained respectively by covering the
whole index line from one or both sides, or by using no side copy.  Conditions
(3.6) permit choices with \(\alpha=1\) and \(\beta=1\).  Put a coordinate at
its first side position and, when necessary to avoid empty later letters,
repeat a coordinate whose threshold is already one.  Repetition after the
first occurrence changes no fan or crossing union.  This constructs a
nonzero word with exactly the prescribed targets.  \(\square\)

### Corollary 3.2 (constructive Ferrers sufficient condition)

Choose nonempty sets

\[
 Z,X_1,\ldots,X_{d-1},Y_1,\ldots,Y_{d-1}                 \tag{3.7}
\]

such that

\[
 Z\subseteq P_0,\qquad X_t\subseteq P_{-t},\qquad
 Y_t\subseteq P_t.                                        \tag{3.8}
\]

Define

\[
 \begin{aligned}
 L_h&=Z\cup\bigcup_{t<h}X_t,\\
 R_h&=Z\cup\bigcup_{t<h}Y_t,\\
 C_i&=\bigcup_{t\le i}X_t\cup\bigcup_{t\le d-i}Y_t.
 \end{aligned}                                             \tag{3.9}
\]

Then the literal word

\[
              A_0=Z,\qquad A_{-t}=X_t,\qquad A_t=Y_t     \tag{3.10}
\]

is one common-`Q` realization.  In particular, nested marginals become a
theorem only when their increments coexist in the same cap state as in
(3.8).  The prepared coatom boundary-chain theorem supplies this kind of
one-sided literal containment; it does not by itself prescribe the coupled
crossing targets.

## 4. Complementary coatom chains

Let \(F=\{f_1,\ldots,f_d\}\), and let \(B_L,B_R\) be disjoint from \(F\).
Consider the two prepared chains

\[
 L_{h+1}=B_L\cup\{f_1,\ldots,f_h\},\qquad
 R_{h+1}=B_R\cup\{f_{d-h+1},\ldots,f_d\},
 \quad 1\le h<d.                                          \tag{4.1}
\]

The typed star is a nonempty set \(Z\).  Put

\[
 G=F\cup\bigl((B_L\cup B_R)\setminus Z\bigr).            \tag{4.2}
\]

### Theorem 4.1 (coatom crossing normal form)

With unrestricted local caps, the chains (4.1) and star \(Z\) admit crossing
targets \(C_i\) in one literal word if and only if

\[
 \varnothing\ne Z\subseteq B_L\cap B_R,                  \tag{4.3}
\]

\[
                    G\subseteq C_i\subseteq G\cup Z
                    \qquad(1\le i<d),                    \tag{4.4}
\]

and, for every \(z\in Z\), the set \(\{i:z\notin C_i\}\)
is an interval.

For general caps, (4.3)--(4.4) are still necessary, but they are sufficient
only together with the maximal-letter test (2.5)--(2.8).  Equivalently, the
mandatory first-occurrence copies---the filler and base increments as well as
the hidden thresholds---must all occur in their actual caps \(P_{\pm t}\).

#### Proof

A coordinate of \(B_L\setminus Z\) first appears on the left at distance
one, and a coordinate of \(B_R\setminus Z\) first appears on the right at
distance one.  Each therefore belongs to every crossing.  The filler
\(f_j\) has endpoint-aware thresholds

\[
 (\alpha_{f_j},\beta_{f_j})=
 \begin{cases}
  (1,\infty),&j=1,\\
  (j,d-j+1),&2\le j\le d-1,\\
  (\infty,1),&j=d.
 \end{cases}                                               \tag{4.5}
\]

For an interior filler and every \(i\), either \(j\le i\) or
\(d-j+1\le d-i\); the endpoint fillers have threshold one on their
available shore.
Thus every filler also belongs to every crossing.  No coordinate outside
\(G\cup Z\) occurs in either fan, so (3.4) excludes it from every crossing.
This proves (4.3)--(4.4); the interval-zero condition and sufficiency are
Theorem 3.1.  With caps, Theorem 2.1 is exact.  \(\square\)

More explicitly, every capped realization must have

\[
 \begin{aligned}
 Z&\subseteq P_0,\\
 (B_L\setminus Z)\cup\{f_1\}&\subseteq P_{-1},&
 f_t&\in P_{-t} &&(2\le t<d),\\
 (B_R\setminus Z)\cup\{f_d\}&\subseteq P_1,&
 f_{d-t+1}&\in P_t &&(2\le t<d),
 \end{aligned}                                             \tag{4.6}
\]

as well as a cap-compatible choice of side copies for every hidden trace.
Under a prepared boundary-chain trace guard, (4.6) is supplied by the
antecedent and the hidden copies are the only additional cap question.
Without that hypothesis, (4.6) cannot be omitted.  The full test remains
(2.5)--(2.8), which also handles the disjunctions for an all-one hidden
trace and any nonzero padding copies.

For the two-phase endpoint theorem, one phase has
\((B_L,B_R)=(B_1,B_0)\) and the other has \((B_0,B_1)\).  A **single typed
star used in both phases** therefore requires

\[
                     \varnothing\ne Z\subseteq B_0\cap B_1.             \tag{4.7}
\]

If the intersection is empty, this face has an exact empty-star obstruction.
This statement does not exclude two different phase-dependent stars.

The rank consequence of (4.4) is

\[
 |C_i|\ge |G|=d+|(B_L\cup B_R)\setminus Z|.               \tag{4.8}
\]

At equality all crossings equal \(G\).  Thus the prepared coatom fan chains
alone do not produce a distinct crossing bank; distinction must be encoded
inside \(Z\) and physically supported by its side caps.

## 5. Sharp hidden-code capacity

Suppose the coatom outside-star bank \(G\) is fixed, so

\[
                         C_i=G\cup H_i,\qquad H_i\subseteq Z.            \tag{5.1}
\]

### Theorem 5.1 (interval-zero code bound)

If \(C_1,\ldots,C_N\) are pairwise distinct consecutive crossing targets,
where \(N\ge2\), then

\[
                              N\le2|Z|.                   \tag{5.2}
\]

Conversely, for every \(h\ge1\) there are \(2h\) pairwise distinct binary
states on an \(h\)-element star bank for which each coordinate has an
interval zero set.  Hence (5.2) is sharp.

#### Proof

Along the crossing index, each star coordinate has trace
\(1^*0^*1^*\) and therefore changes at most twice.  If \(N\) consecutive
states are pairwise distinct, every one of the \(N-1\) boundaries changes
at least one coordinate, so \(N-1\le2h\), where \(h=|Z|\).  Equality
\(N=2h+1\) would use all \(2h\) possible changes.  Every coordinate would
then change exactly twice, and the final state would equal the initial
state, contradicting pairwise distinctness.  Thus \(N\le2h\).

For sharpness, start with all \(h\) bits equal to one, turn
\(z_1,z_2,\ldots,z_h\) off successively, and then turn
\(z_1,z_2,\ldots,z_{h-1}\) on successively.  The resulting \(2h\) states
are distinct, and the zeros of each bit form one interval.  \(\square\)

Taking \(N=d-1\) gives (0.1).  The construction is physically realizable
whenever the threshold copies of its star coordinates satisfy the cap rows
in Theorem 2.1.  In particular, a persistent hidden bank
\(Z\subseteq\bigcap_pP_p\) of size \(\lceil(d-1)/2\rceil\) suffices for the
trace part, while a star target available only at \(p=0\) does not.

The typed singleton \(A_0=Z=S_\tau\) consumes the unique surplus fan cell.
After the other \(2d-2\) fan cells carry the two chains, only the \(d-1\)
addresses from the rest of the one-cell exchange remain.  The hidden-code
coordinates do not create additional physical addresses.

## 6. Smallest obstruction

Nested fans are not sufficient, already at \(d=2\).  With unrestricted caps
take

\[
 Z=\{a\},\qquad L_2=\{a,b\},\qquad
 R_2=\{a,c\},\qquad C_1=\{b\}.                            \tag{6.1}
\]

All four targets are nonempty and pairwise distinct, but

\[
 K_0=\{a\},\qquad K_1^-=\{b\},\qquad K_1^+=\varnothing.  \tag{6.2}
\]

Equivalently, the positive requirement \((R_2,c)\) is killed at the star by
the negative singleton target \(Z\) and at position \(+1\) by the negative
crossing target \(C_1\).  This is an exact two-pin positive-cover core.
Dimension \(d=1\) has no crossing row, so \(d=2\) is minimal.  If pairwise
distinct target values are required, three coordinates are also minimal.

## 7. Proved boundary

The common-cap part of the local ear is now completely characterized:

* (2.5)--(2.8) are necessary and sufficient for any fixed caps and target
  assignment;
* (3.3)--(3.6) are the cap-free Ferrers/threshold characterization;
* (4.3)--(4.4) are the exact coatom-chain specialization;
* (5.2) is the sharp amount of persistent star state needed to distinguish
  a full crossing bank.

What remains is physical, not marginal: choose one cut and one target
assignment for which all hidden threshold copies lie in the same legal cap
state, every exterior positive row has a retained witness, and the resulting
\(d-1\) free addresses connect to the global compiler matching.  The
prepared two-phase boundary theorem supplies literal nested fans, but it
does not supply this common hidden-copy state.  No additive-constant or
exact-\(B(k)\) conclusion is claimed here.
