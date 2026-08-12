# PBBS zero-winding returns: exact owner-wreath structure and endpoint limitation

Date: 2026-07-25

Pure mathematics only.  No computation, finite search, or external input is
used.

## 0. Verdict

Let \(N=2r+1\), let \(A_t\in\binom{[N]}r\) be consecutive states of the
canonical PBBS factor, and let \(\lambda_t\) be the coordinate omitted by
the edge \(A_tA_{t+1}\).  Suppose

\[
 \lambda_{2s+1}=\lambda_0=u
 \tag{0.1}
\]

is a genuine zero-winding consecutive return.  Then the following statements
hold.

1. The normalized Dyck height is exactly \(s\), and \(d(D_0)=1\).
2. The labels

   \[
   \lambda_0,\lambda_1,\ldots,\lambda_{2s}
   \tag{0.2}
   \]

   are pairwise distinct.  The only repetition in (0.1)--(0.2) is the
   returned endpoint \(\lambda_{2s+1}=\lambda_0\).
3. Put

   \[
   a_j=\lambda_{2j}\quad(0\le j\le s),
   \qquad
   b_j=\lambda_{2j+1}\quad(0\le j<s).
   \tag{0.3}
   \]

   There are disjoint cores \(K,K'\), each of size \(r-s\), for which the
   even and odd step-two owners have the exact formulas

   \[
   \boxed{
   A_{2j}=K\cup\{a_0,\ldots,a_{j-1}\}
               \cup\{b_j,\ldots,b_{s-1}\}}
   \quad(0\le j\le s),
   \tag{0.4}
   \]

   \[
   \boxed{
   A_{2j+1}=K'\cup\{b_0,\ldots,b_{j-1}\}
                 \cup\{a_{j+1},\ldots,a_s\}}
   \quad(0\le j\le s).
   \tag{0.5}
   \]

   Empty ranges are omitted.  The state after the returned endpoint edge is

   \[
   \boxed{A_{2s+2}=K\cup\{a_1,\ldots,a_s\}.}
   \tag{0.6}
   \]

4. Consequently the even step-two owner segment is literally a fixed-core
   run of cyclic \(s\)-windows, and the odd segment is its complementary-core
   run.  The open one-step segment through the edge labelled \(a_s\) embeds
   in an exact \((N,r)\)-wreath.  In fact it has \((r-s)!^2\) explicit
   ordered wreath completions.
5. The two occurrences of the returned label \(a_0\) form an exact
   core-swap square: the initial and terminal Kneser edges are the two
   crossed pairings of the same two cores and the same two active windows.

There is an important logical qualification.  The condition \(d(D_0)=1\)
alone supplies only the first physical seam

\[
 a_1=a_0-1\pmod N.                                 \tag{0.7}
\]

It neither implies a return nor chooses the remaining wreath completion.
The word \(1110011000\) is an exact symbolic counterexample.  Thus:

* **yes**, a genuine \(d=1\) zero-winding return has the asserted
  fixed-core owner half and the other parity gives the complementary-core
  half;
* **no**, the endpoint \(d=1\) sector by itself does not supply a canonical
  complementary ambient half.

The proof below uses only the omitted-label recurrence, literal block
rotation, height invariance, and the height--gap theorem.  It does not use
the invalid first-deepest-sector iteration.

## 1. Literal zero-winding coordinates

Write

\[
 D_j=\tau^jD_0=P_j1R_j0S_j,
 \qquad
 d_j=|S_j|+1,
 \qquad
 \delta_j=|P_j|+1.
 \tag{1.1}
\]

The exact two-step block rotation is

\[
 \tau(P1R0S)=S1P0R.                                \tag{1.2}
\]

Put

\[
 C_j=\sum_{h=0}^{j-1}d_h,
 \qquad
 M_j=\delta_j-C_j.                                 \tag{1.3}
\]

Zero winding is the ordinary equality

\[
 C_s=\delta_s<N.                                   \tag{1.4}
\]

For completeness, let

\[
 \widehat d_j=d(\phi D_j),
 \qquad \beta_j=\delta(\phi D_j).
\]

The two voltage identities at \(D_j\) and \(\phi D_j\) are

\[
 d_j=N-\delta_j-\beta_j,
 \qquad
 \widehat d_j=N-\beta_j-\delta_{j+1}.
\]

Therefore

\[
 \boxed{M_{j+1}-M_j=-\widehat d_j<0.}              \tag{1.5}
\]

Since \(M_s=0\),

\[
 M_0>M_1>\cdots>M_{s-1}>M_s=0.                    \tag{1.6}
\]

Also

\[
 0=C_0<C_1<\cdots<C_s<N.                           \tag{1.7}
\]

### Lemma 1.1 (height and the initial deficit)

A zero-winding return as above satisfies

\[
 \boxed{\operatorname{ht}(D_j)=s\ (0\le j\le s),
        \qquad S_0=\varnothing,
        \qquad d_0=1.}                             \tag{1.8}
\]

#### Proof

For \(0\le j\le s\), put

\[
 Q_j=(S_{j-1}1)(S_{j-2}1)\cdots(S_01),
 \qquad Q_0=\varnothing.
\]

Its length is \(C_j\).  Equation (1.2) says that
\(D_{j+1}\) begins with \(S_j1P_j\).  By (1.6),

\[
 C_j<\delta_j=|P_j|+1\qquad(j<s),
\]

so induction shows that \(Q_j\) is the length-\(C_j\) prefix of \(P_j\)
for \(j<s\).  At the terminal equality (1.4),

\[
 \boxed{Q_s=P_s1.}                                 \tag{1.9}
\]

Every \(S_j\) is Dyck.  Hence the right side of (1.9) first reaches
height \(s\) at its last displayed one.  Thus \(D_s\) has height \(s\).
The one-step map \(\phi\), and therefore \(\tau\), preserves height, so
all \(D_j\) have height \(s\).

The block \(S_0\) in (1.9) is read at height \(s-1\), immediately before
the last displayed one.  If it were nonempty, its first up-step would reach
height \(s\) earlier, contradicting the canonical first-maximum position.
Thus \(S_0=\varnothing\), and \(d_0=1\). \(\square\)

The spatial part of the even-time skew product is

\[
 (u,D_j)\longmapsto(u-d_j,D_{j+1}).
\]

Consequently the omitted labels have the exact integer-coordinate form

\[
 \boxed{
 \lambda_{2j}=u-C_j,
 \qquad
 \lambda_{2j+1}=u+M_j}
 \pmod N
 \qquad(0\le j\le s).                              \tag{1.10}
\]

In particular (1.4) makes \(\lambda_{2s+1}=u\), while (1.8) gives
\(a_1=u-1\), proving (0.7).

## 2. No internal omitted-label collision

### Theorem 2.1 (simple-return label theorem)

The labels in (0.2) are pairwise distinct.

#### Proof

Equations (1.7) and (1.10) make the even labels

\[
 \lambda_0,\lambda_2,\ldots,\lambda_{2s}
\]

pairwise distinct.  Equations (1.6) and (1.10) do the same for

\[
 \lambda_1,\lambda_3,\ldots,\lambda_{2s+1}.
\]

Suppose an even label \(\lambda_{2p}\) equals an odd label
\(\lambda_{2q+1}\), other than the endpoint equality
\((p,q)=(0,s)\).  Within the time interval from one occurrence to the
other there is no third occurrence of that label, by the two parity
uniqueness statements.  Hence these two times delimit a consecutive
omitted-label return of gap

\[
 g'=|2p-(2q+1)|\le2s-1.                            \tag{2.1}
\]

Every normalized state on the intervening PBBS orbit has Dyck height
\(s\), because \(\phi\) preserves height and Lemma 1.1 identifies that
height.  The exact height--gap theorem therefore requires

\[
 g'\ge2s+1,                                        \tag{2.2}
\]

contradicting (2.1).  Thus no internal cross-parity equality exists.
\(\square\)

This is the replacement for the false sector-shift converse.  Notice that
it assumes an actual zero-winding return; it does not attempt to derive one
from \(d_0=1\).

## 3. Exact fixed-core owner formulas

The PBBS factor recurrence is

\[
 \boxed{
 A_{t+1}=[N]\setminus(A_t\cup\{\lambda_t\}).}
 \tag{3.1}
\]

Therefore

\[
 \boxed{
 A_{t+2}=A_t-\{\lambda_{t+1}\}+\{\lambda_t\}.}
 \tag{3.2}
\]

Let

\[
 Z=\{a_0,\ldots,a_s,b_0,\ldots,b_{s-1}\},
 \qquad R=[N]\setminus Z.
 \tag{3.3}
\]

Theorem 2.1 gives \(|Z|=2s+1\), so \(|R|=2(r-s)\).

### Theorem 3.1 (two fixed cores)

There is a partition

\[
 R=K\mathbin{\dot\cup}K',
 \qquad |K|=|K'|=r-s,                              \tag{3.4}
\]

for which (0.4)--(0.6) hold.

#### Proof

Set \(K=A_0\cap R\).  By (3.2), the coordinate \(b_j\) is removed in the
move \(A_{2j}\to A_{2j+2}\).  It has not occurred earlier, so it was
already in \(A_0\).  Similarly every \(a_j\) is absent from \(A_0\) until
the move in which it is inserted.  Hence

\[
 A_0=K\cup\{b_0,\ldots,b_{s-1}\}.
 \tag{3.5}
\]

Since \(|A_0|=r\), this gives \(|K|=r-s\).  Put \(K'=R\setminus K\),
which has the same size.

Iterating (3.2) with
\(\lambda_{2j}=a_j\) and \(\lambda_{2j+1}=b_j\) proves (0.4).  Applying
(3.1) to \(A_{2j}\) and the omitted label \(a_j\) gives (0.5).  Finally,
the returned endpoint move uses

\[
 \lambda_{2s}=a_s,
 \qquad \lambda_{2s+1}=a_0,
\]

so (3.2) gives (0.6). \(\square\)

The complement-projected even owners \(X_j=[N]\setminus A_{2j}\) obey the
equivalent exact formula

\[
 X_j=K'\cup\bigl(Z\setminus
  (\{a_0,\ldots,a_{j-1}\}\cup\{b_j,\ldots,b_{s-1}\})\bigr).
 \tag{3.6}
\]

Thus the conclusion is unchanged whichever owner convention is used.

## 4. Cyclic-window and wreath form

Arrange the active labels in the cyclic order

\[
 \Gamma=(b_0,b_1,\ldots,b_{s-1},a_0,a_1,\ldots,a_s),
 \tag{4.1}
\]

and let \(V_i\) be the cyclic \(s\)-window of \(\Gamma\) starting at
position \(i\), with indices modulo \(2s+1\).

### Theorem 4.1 (exact active wreath halves)

One has

\[
 \boxed{A_{2j}=K\cup V_j\quad(0\le j\le s+1),}
 \tag{4.2}
\]

and

\[
 \boxed{A_{2j+1}=K'\cup V_{s+1+j}\quad(0\le j\le s),}
 \tag{4.3}
\]

where the index in (4.3) is reduced modulo \(2s+1\).

#### Proof

For \(j<s\), the window \(V_j\) is

\[
 \{b_j,\ldots,b_{s-1},a_0,\ldots,a_{j-1}\};
\]

the same formula remains valid at \(j=s,s+1\) with empty ranges and cyclic
interpretation.  This is (0.4) and (0.6).  Similarly \(V_{s+1+j}\) is

\[
 \{a_{j+1},\ldots,a_s,b_0,\ldots,b_{j-1}\},
\]

which is (0.5). \(\square\)

Hence the even step-two owners are a consecutive fixed-\(K\) cyclic-window
run, while the odd owners are the complementary fixed-\(K'\) run.  More
strongly, the open one-step segment is contained in an actual ambient
wreath.

More precisely, among the first \(2s+1\) owner states, the even owners
\(A_0,A_2,\ldots,A_{2s}\) use \(V_0,\ldots,V_s\), while the odd owners
\(A_1,A_3,\ldots,A_{2s-1}\) use
\(V_{s+1},\ldots,V_{2s}\).  These two lists partition all \(2s+1\)
active cyclic windows exactly once.  The two endpoint states then repeat
the active windows across the cores:

\[
 A_{2s+1}=K'\cup V_0,
 \qquad A_{2s+2}=K\cup V_{s+1}.
 \tag{4.3a}
\]

### Corollary 4.1a (the endpoint core-swap square)

Put

\[
 U=V_0=\{b_0,\ldots,b_{s-1}\},
 \qquad
 V=V_{s+1}=\{a_1,\ldots,a_s\}.
\]

Then the initial and returned-label edges are exactly

\[
 \boxed{
 \begin{array}{ccl}
 A_0&=&K\cup U,\\
 A_1&=&K'\cup V,
 \end{array}
 \qquad
 \begin{array}{ccl}
 A_{2s+1}&=&K'\cup U,\\
 A_{2s+2}&=&K\cup V.
 \end{array}}
 \tag{4.3b}
\]

Both displayed Kneser edges omit \(a_0\).  Thus the terminal occurrence
does supply the complementary **core pairing** of the initial edge.  This
is an exact two-edge switch, not a claim that the scalar condition
\(d_0=1\) constructs the unused ambient wreath completion.

#### Proof

Equations (0.4)--(0.6) give three corners, while (0.5) at \(j=0\) gives
the fourth.  The four constituent sets are disjoint across each displayed
column, and each column's union is \([N]\setminus\{a_0\}\). \(\square\)

### Theorem 4.2 (explicit ambient wreath completions)

Put \(q=r-s\).  Choose arbitrary orders

\[
 K=(k_1,\ldots,k_q),
 \qquad K'=(k'_1,\ldots,k'_q),
\]

and form the cyclic omitted-label permutation

\[
 \begin{aligned}
 z={}&(a_0,b_0,a_1,b_1,\ldots,a_{s-1},b_{s-1},a_s,\\
     &k_1,k'_1,k_2,k'_2,\ldots,k_q,k'_q).
 \end{aligned}                                      \tag{4.4}
\]

Let

\[
 W_t=\{z_{t+1},z_{t+3},\ldots,z_{t+2r-1}\},
 \tag{4.5}
\]

with subscripts modulo \(N\).  Then \((W_t)_{t\in\mathbb Z_N}\) is an
exact \((N,r)\)-wreath, its edge \(W_tW_{t+1}\) omits \(z_t\), and

\[
 \boxed{W_t=A_t\qquad(0\le t\le2s+1).}             \tag{4.6}
\]

#### Proof

The two sets in (4.5) for consecutive \(t\) partition
\([N]\setminus\{z_t\}\), so they are disjoint \(r\)-sets and their edge
omits \(z_t\).  This is the standard omitted-permutation description of a
wreath.  Equivalently, because multiplication by two is invertible modulo
the odd integer \(N\), the sets in (4.5) are precisely the cyclic
\(r\)-windows in the coordinate order
\(z_0,z_2,z_4,\ldots,z_{2(N-1)}\).

The odd-indexed entries of (4.4) are exactly

\[
 b_0,\ldots,b_{s-1},k_1,\ldots,k_q,
\]

so (3.5) gives \(W_0=A_0\).  The two paths then have the same omitted
labels \(z_t=\lambda_t\) for \(0\le t\le2s\).  Recurrence (3.1) determines
the next owner uniquely, proving (4.6) by induction. \(\square\)

There are \((q!)^2\) displayed ordered completions when the cores are
regarded as labelled sets.  For a short return \(2s+1<N\), one has
\(q>0\).  The next omitted label of a completion is \(k_1\), whereas the
actual PBBS return edge has omitted label

\[
 \lambda_{2s+1}=a_0.                               \tag{4.7}
\]

Thus the open segment is wreath-compatible, but the returned endpoint edge
branches away from every simple completion in (4.4).  If \(s=r\), there is
no unused core and (4.7) is the ordinary closure of the full wreath; this is
the nonshort boundary case.

## 5. What \(d_0=1\) does and does not supply

For a genuine zero-winding return, Lemma 1.1 proves \(d_0=1\), and (1.10)
then gives only the physical adjacency \(a_1=a_0-1\).  The remaining
facts used in Theorems 3.1--4.2 are:

* the full zero-winding equality;
* strict first passage;
* height equality \(h=s\);
* the height--gap exclusion of every internal label collision; and
* the Kneser recurrence (3.1).

The endpoint deficit alone cannot replace them.

### Proposition 5.1 (exact endpoint counterexample)

The semilength-five Dyck word

\[
 D_0=1110011000                                    \tag{5.1}
\]

has \(d(D_0)=1\) and height three, but no zero-winding return at
step-two time three.

#### Proof

Literal application of (1.2) gives

\[
 \begin{array}{c|c|c|c}
 j&D_j&\delta(D_j)&d(D_j)\\ \hline
 0&1110011000&3&1\\
 1&1110001100&3&5\\
 2&1100111000&7&1\\
 3&1110011000&3&1.
 \end{array}                                       \tag{5.2}
\]

At the putative height time,

\[
 d(D_0)+d(D_1)+d(D_2)=1+5+1=7\ne3=\delta(D_3).
 \tag{5.3}
\]

Thus the endpoint sector neither returns nor closes a wreath half.
\(\square\)

Even after a genuine return is assumed, \(d_0=1\) does not select the
unused complementary core order: Theorem 4.2 displays \((r-s)!^2\)
choices.  The complementary **owner parity** in (4.3) is forced, but it is
forced by the whole return and the factor recurrence, not by the scalar
endpoint condition.

## 6. Adversarial audit

1. **No sector transport is used.**  The height and \(d_0=1\) conclusions
   come from the literal staircase prefix (1.9), whose legality follows
   from the strict variable (1.5).
2. **Cross-parity distinctness is not assumed.**  It is proved by turning
   any collision into a shorter consecutive return and invoking the exact
   height--gap theorem at the invariant height \(s\).
3. **The endpoint edge is separated from the open wreath segment.**  The
   embedding (4.6) stops at state \(A_{2s+1}\); the next actual omitted
   label repeats \(a_0\), while a short wreath completion must use an unused
   core label.
4. **Both owner conventions are covered.**  Equations (0.4)--(0.6) are for
   the middle factor states; (3.6) gives the complement-projected owners.
5. **The fixed cores have exact sizes.**  Internal label distinctness leaves
   \(2(r-s)\) inactive coordinates, split evenly because every even owner
   has size \(r\).
6. **The logical converse is explicitly rejected.**  Proposition 5.1
   prevents the valid structure theorem from being misread as
   \(d(D)=1\Rightarrow\) return.
