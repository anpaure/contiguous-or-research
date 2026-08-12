# Exact ambient-completion kernel for simple PBBS return sectors

Date: 2026-07-25

Pure mathematics only.

## 0. Outcome

The factor-two reduction in
`PBBS_MINIMAL_RETURN_FIXED_CORE_NORMAL_FORM_20260725.md` shows that the
Catalan-order residence gate may be restricted to simple returns.  A
simple gap-\((2s+1)\) return has active labels

\[
 Z=U\mathbin{\dot\cup}A,
 \qquad |U|=s,quad |A|=s+1,
\]

and inactive cores

\[
 [N]\setminus Z=K\mathbin{\dot\cup}K',
 \qquad |K|=|K'|=q=r-s.
\]

It has \((q!)^2\) ordered ambient wreath completions.  If the orders of
\(K\) and \(K'\) are chosen independently and uniformly, the probability
that a fixed middle vertex \(T\) occurs in the random completion is given
exactly by two reciprocal-binomial kernels, apart from the fixed open
segment.

For a projected-edge-disjoint family of simple sectors, every middle
vertex lies in at most four fixed open segments.  Therefore the desired
Catalan packing bound follows from one explicit fractional tail-load
inequality, stated in (4.3) below.  No integral selection of completions is
needed: bounded fractional vertex load already gives the volume bound.

The tail-load inequality itself is not proved here.

## 1. One completion written as two random Boolean chains

Use the notation of the simple-return normal form:

\[
 U=\{b_0,\ldots,b_{s-1}\},
 \qquad
 A=\{a_0,a_1,\ldots,a_s\}.
 \tag{1.1}
\]

Choose independent uniform orders

\[
 K=(k_1,ldots,k_q),
 \qquad K'=(k'_1,ldots,k'_q).
 \tag{1.2}
\]

The ambient omitted-label order is

\[
 (a_0,b_0,a_1,b_1,\ldots,a_{s-1},b_{s-1},a_s,
   k_1,k'_1,\ldots,k_q,k'_q).
 \tag{1.3}
\]

The first \(2s+2\) wreath vertices are the fixed open PBBS segment

\[
 A_0,A_1,\ldots,A_{2s+1}.
 \tag{1.4}
\]

The remaining distinct vertices split into the following two chains.  For
\(1\le j\le q-1\), put

\[
 O_j
 =U\cup\{k_1,\ldots,k_j\}
    \cup\{k'_{j+1},\ldots,k'_q\},
 \tag{1.5}
\]

and, for \(0\le j\le q-1\), put

\[
 E_j
 =A\cup\{k_{j+2},\ldots,k_q\}
    \cup\{k'_1,\ldots,k'_j\}.
 \tag{1.6}
\]

Empty ranges are omitted.  Notice that \(O_0=K'\cup U=A_{2s+1}\) and
\(O_q=K\cup U=A_0\), so exactly the internal values in (1.5) are new.
The lists (1.4)--(1.6) contain

\[
 (2s+2)+(q-1)+q=2r+1=N
\]

vertices.

### Lemma 1.1

Equations (1.4)--(1.6) are exactly the vertex set of the ambient wreath
completion determined by (1.2)--(1.3).

#### Proof

The open segment statement is the ambient-wreath theorem in the simple
return normal form.  At its last vertex one has

\[
 O_0=K'\cup U.
\]

The two-step wreath recurrence removes \(k'_j\) and inserts \(k_j\),
which gives (1.5) inductively.  Complementing between successive odd
states gives (1.6).  The endpoint values \(O_0,O_q\) are already the two
fixed open endpoint vertices, and the count above exhausts the wreath.
\(\square\)

## 2. Exact incidence probability of one middle vertex

For a sector \(I=(Z,U,A,K,K')\), let \(\mathbb P_I\) denote the uniform
measure on its \((q!)^2\) ordered completions.  Let

\[
 \mathcal O(I)=\{A_0,\ldots,A_{2s+1}\}
 \tag{2.1}
\]

be the fixed open vertex set.

### Theorem 2.1 (completion incidence kernel)

For every \(T\in\binom{[N]}r\),

\[
 \boxed{
 \begin{aligned}
 \mathbb P_I(T\text{ lies in the completed wreath})
 ={}&\mathbf1_{\{T\in\mathcal O(I)\}}\\
 &+\mathbf1_{\{T\cap Z=U\}}
   \mathbf1_{\{1\le j\le q-1\}}
   {1\over\binom qj^2}\\
 &+\mathbf1_{\{T\cap Z=A\}}
   {1\over\binom qj\binom q{j+1}},
 \end{aligned}}
 \tag{2.2}
\]

where in the second line

\[
 j=|T\cap K|,
 \tag{2.3}
\]

and in the third line

\[
 j=|T\cap K'|\in\{0,\ldots,q-1\}.
 \tag{2.4}
\]

The three events in (2.2) refer to distinct completion vertices; at the
two excluded odd endpoints the vertex is already counted by the first
line.

#### Proof

Suppose first that \(T=O_j\) for an internal odd-chain index.  Necessarily

\[
 T\cap Z=U,
 \qquad |T\cap K|=j,
 \qquad |T\cap K'|=q-j.
\]

A uniform order of \(K\) has the prescribed \(j\)-set \(T\cap K\) as
its first \(j\) elements with probability \(1/\binom qj\).  Independently,
a uniform order of \(K'\) has the prescribed \((q-j)\)-set
\(T\cap K'\) as its final \(q-j\) elements with the same probability.
This gives the second line of (2.2).

Now suppose \(T=E_j\).  Necessarily \(T\cap Z=A\).  The first \(j\)
elements of the \(K'\)-order must be \(T\cap K'\), which has probability
\(1/\binom qj\).  The first \(j+1\) elements of the \(K\)-order must be
\(K\setminus T\), which has probability \(1/\binom q{j+1}\).  Independence
gives the third line.  Lemma 1.1 shows that there are no other vertices.
\(\square\)

As a check, summing (2.2) over all middle vertices \(T\) gives \(N\):
every completion is an \(N\)-vertex wreath.

## 3. The fixed open load is at most four

### Lemma 3.1 (open-segment endpoint throughput)

Let \(\mathcal P\) be a pairwise projected-edge-disjoint family of simple
return sectors.  Then every PBBS middle vertex belongs to the fixed open
segment of at most four members of \(\mathcal P\).

#### Proof

Work on one lifted PBBS component and cut it at the vertex under
consideration.  Every relevant short sector is now an ordinary
chronological interval.  Separate them according to the parity of their
starting occurrence relative to the cut.  Within either parity, the
projected traces are ordinary intervals on one step-two line and are
pairwise edge-disjoint.  At a fixed vertex, at most one such interval can
approach from the left and at most one can leave to the right.  Thus at
most two sectors of either parity contain the vertex, for a total of four.
Different PBBS components have disjoint vertex sets.  \(\square\)

The value four allows shared endpoints.  If sectors are taken half-open at
one end, the same proof gives two; the coarser value four is enough for the
coefficient-one volume ledger.

## 4. Exact fractional completion gate

For a simple sector \(I\), define its random-tail kernel by deleting the
first line of (2.2):

\[
 \begin{aligned}
 \pi_I(T)={}&
 \mathbf1_{\{T\cap Z_I=U_I\}}
 \mathbf1_{\{1\le j\le q_I-1\}}
 {1\over\binom {q_I}j^2}\\
 &+\mathbf1_{\{T\cap Z_I=A_I\}}
 {1\over\binom {q_I}j\binom {q_I}{j+1}}.
 \end{aligned}
 \tag{4.1}
\]

### Theorem 4.1 (fractional ambient-completion criterion)

Suppose there is a constant \(C_A\) such that every projected-edge-disjoint
family \(\mathcal P\) of simple sectors of residence at most
\(H=\lceil A\sqrt r\rceil\) satisfies

\[
 \boxed{
 \sup_{T\in\binom{[N]}r}
 \sum_{I\in\mathcal P}\pi_I(T)\le C_A.}
 \tag{4.2}
\]

Then

\[
 \boxed{|\mathcal P|\le(C_A+4){W\over N}.}
 \tag{4.3}
\]

Consequently \((CP_A)\) holds, and hence the contiguous-OR coefficient-one
theorem follows from the established linear-seam reduction.

#### Proof

Choose a completion of every sector independently from its uniform
completion measure, but retain only expectations.  By Theorem 2.1 and
Lemma 3.1, the expected total number of selected completed wreaths which
contain a fixed middle vertex \(T\) is at most \(C_A+4\).

Every completed wreath contains exactly \(N\) middle vertices.  Double
count expected sector--vertex incidences:

\[
 N|\mathcal P|
 =\sum_{T\in\binom{[N]}r}
   \sum_{I\in\mathcal P}
   \mathbb P_I(T\text{ lies in the completion})
 \le(C_A+4)W.
\]

This proves (4.3).  The factor-two simple-return reduction transfers the
same big-oh estimate to unrestricted residence packings.  The established
linear-seam theorem then gives coefficient one.  \(\square\)

## 5. Exact remaining inequality

The full completion problem is therefore reduced to (4.2).  Expanded, it
asks for a uniform bound on

\[
 \begin{aligned}
 \sum_{I\in\mathcal P:\,T\cap Z_I=U_I}
 {1\over\binom {q_I}{|T\cap K_I|}^2}
 +
 \sum_{I\in\mathcal P:\,T\cap Z_I=A_I}
 {1\over
   \binom {q_I}{|T\cap K'_I|}
   \binom {q_I}{|T\cap K'_I|+1}}.
 \end{aligned}
 \tag{5.1}
\]

Only sectors for which \(T\) contains exactly one of the two active halves
contribute.  Interior core mixtures are suppressed by reciprocal central
binomial factors; the largest nonfixed endpoint terms are \(1/q_I\).

No proof of a uniform bound for (5.1) is supplied here.  The result is a
strict reduction: it replaces the selection of pairwise disjoint full
wreath completions by an explicit positive fractional load inequality with
an exact kernel and a fixed open load at most four.
