# Complete third PBBS turn shadow from a deficit-seven boundary

Date: 2026-07-25

No computation or external input is used.

## 0. Theorem

Let \(n=2m+1\), let \(f\) be the canonical PBBS permutation, and put
\(g=f^2\). For every

\[
S\in\binom{[n]}{m-3}
\]

there are four consecutive \(g\)-states

\[
A_0\longrightarrow A_1\longrightarrow A_2\longrightarrow A_3
\]

such that

\[
\boxed{A_0\cap A_1\cap A_2\cap A_3=S.}
\tag{0.1}
\]

Thus the canonical PBBS third turn shadow has complete rank-\((m-3)\)
support. The fixed-fibre theorem gives the simultaneous cap

\[
\boxed{1\le\mu_{P,3}^{\mathrm{corr}}(S)\le\binom73=35.}
\tag{0.2}
\]

Unlike depth two, arbitrary four-state PBBS intersections need not all
have rank \(m-3\), because gap-five returns exist. The theorem asserts
that every correct-rank target nevertheless has a correct-rank occurrence.

## 1. Seven forward and reverse marks

Put \(Z=[n]\setminus S\). The deficit-seven word of \(S\) has seven
forward-unmatched zeros and seven reverse-unmatched zeros. Form an expanded
circular word \(\mathcal W_S\):

- write \(A_x\) at every \(x\in U_+(S)\);
- write \(C_x\) at every \(x\in U_-(S)\);
- at a shared coordinate write the consecutive pair \(C_x,A_x\).

The word has seven symbols of each type. Choose an \(A\to C\) transition
and name it

\[
A_c,C_b.
\tag{1.1}
\]

The physical coordinates \(b,c\) are distinct. Starting at \(C_b\), let
\(C_{a_1},C_{a_2}\) be the next two \(C\)-symbols. Starting at \(A_c\)
and moving backwards, let \(A_{d_1},A_{d_2}\) be the preceding two
\(A\)-symbols.

The proposed extras path is

\[
\boxed{
\{a_2,a_1,b\}\longrightarrow
\{a_1,b,c\}\longrightarrow
\{b,c,d_1\}\longrightarrow
\{c,d_1,d_2\}.}
\tag{1.2}
\]

Adding \(S\) to every displayed triple gives the desired PBBS states once
the three arrows are verified.

## 2. The exact local legality inequalities

Let

\[
\begin{aligned}
k&=\#\{\text{\(A\)-symbols strictly between \(C_b\) and \(C_{a_1}\)}\},\\
\ell&=\#\{\text{\(A\)-symbols strictly after \(C_b\) and before
                         \(C_{a_2}\)}\}.
\end{aligned}
\tag{2.1}
\]

Moving backwards from \(A_c\), define dually

\[
\begin{aligned}
k'&=\#\{\text{\(C\)-symbols strictly between \(A_c\) and \(A_{d_1}\)
                         in the backward direction}\},\\
\ell'&=\#\{\text{\(C\)-symbols encountered before reaching \(A_{d_2}\)
                         in the backward direction}\}.
\end{aligned}
\tag{2.2}
\]

Call the boundary (1.1) good when

\[
\boxed{k\le2,\quad \ell\le4,\quad k'\le2,\quad \ell'\le4.}
\tag{2.3}
\]

The inequalities also rule out every dangerous shared-coordinate
coincidence in (1.2). Indeed, \(k\le2\) puts a possible \(A\)-copy of
\(C_{a_1}\) among \(F_1,F_2,F_3\), not at \(F_6=d_1\);
\(\ell\le4\) puts a possible \(A\)-copy of \(C_{a_2}\) no later than
\(F_5=d_2\), and never at \(F_0=c\). Also a possible \(A\)-copy of
\(C_b\) is \(F_1\), not \(F_5\). The dual statements follow from
\(k',\ell'\). At an endpoint equality such as \(C_{a_2}=F_5\), the
predecessor is strict and therefore skips that same physical coordinate.
Thus all four triples in (1.2) have three distinct coordinates and every
claimed swap changes the state.

### Lemma 2.1 — every good boundary gives the three PBBS arrows

If (1.1) is good, then after adjoining \(S\), all three arrows in (1.2)
are genuine \(g=f^2\) transitions.

#### Proof

For a rank-\((m-1)\) core \(K\), an arrow

\[
K\cup\{x\}\longrightarrow K\cup\{y\}
\tag{2.4}
\]

is a \(g\)-edge exactly when

\[
r_+(K\cup\{x\})=y,\qquad r_-(K\cup\{y\})=x.
\tag{2.5}
\]

Equivalently, \(y\) is the strict predecessor of \(x\) among the three
forward-unmatched zeros of \(K\), and \(x\) is the strict successor of
\(y\) among the three reverse-unmatched zeros of \(K\).

Number the forward \(A\)-marks from \(A_c\) as

\[
F_0=c,F_1,\ldots,F_6
\]

in the forward direction; thus \(F_6=d_1\) and \(F_5=d_2\).
Number the reverse \(C\)-marks from \(C_b\) as

\[
G_0=b,G_1=a_1,G_2=a_2,\ldots,G_6.
\]

**First arrow.** Its common core is

\[
K_0=S\cup\{G_0,G_1\}.
\]

Flipping \(G_0\) removes the first two forward-unmatched \(F\)-marks after
\(G_0\). Because \(k\le2\), flipping \(G_1\) then removes the next two.
Hence

\[
U_+(K_0)=\{F_0,F_5,F_6\}.
\tag{2.6}
\]

Since \(\ell\le4\), the strict predecessor of \(G_2\) in this triple is
\(F_0=c\). On the reverse side, flipping the two consecutive reverse
marks \(G_0,G_1\) leaves

\[
U_-(K_0)=\{G_2,G_3,G_4\},
\tag{2.7}
\]

whose strict successor after \(c\) is \(G_2=a_2\). Equation (2.5) gives

\[
S\cup\{a_2,a_1,b\}\longrightarrow S\cup\{a_1,b,c\}.
\tag{2.8}
\]

**Middle arrow.** Its common core is

\[
K_1=S\cup\{G_0,F_0\}.
\]

Flipping \(G_0,F_0\) leaves

\[
U_+(K_1)=\{F_4,F_5,F_6\},\qquad
U_-(K_1)=\{G_1,G_2,G_3\}.
\tag{2.9}
\]

The inequality \(k\le2\) makes \(F_6=d_1\) the strict predecessor of
\(G_1=a_1\) in the first triple. The inequality \(k'\le2\) makes
\(G_1=a_1\) the strict successor of \(F_6=d_1\) in the second. Hence

\[
S\cup\{a_1,b,c\}\longrightarrow S\cup\{b,c,d_1\}.
\tag{2.10}
\]

**Last arrow.** Its common core is

\[
K_2=S\cup\{F_0,F_6\}.
\]

Flipping these two cyclically consecutive forward marks leaves

\[
U_+(K_2)=\{F_3,F_4,F_5\}.
\tag{2.11}
\]

The strict predecessor of \(G_0=b\) is \(F_5=d_2\). Reversing the first
arrow argument and using \(k'\le2,\ell'\le4\) shows that the strict
successor of \(F_5=d_2\) in \(U_-(K_2)\) is \(G_0=b\). Thus

\[
S\cup\{b,c,d_1\}\longrightarrow S\cup\{c,d_1,d_2\}.
\tag{2.12}
\]

This proves all three arrows. \(\square\)

## 3. A good boundary always exists

Write the expanded circular word in runs as

\[
A^{\alpha_0}C^{\gamma_0}
A^{\alpha_1}C^{\gamma_1}\cdots
A^{\alpha_{t-1}}C^{\gamma_{t-1}},
\tag{3.1}
\]

where all parts are positive and

\[
\sum_i\alpha_i=\sum_i\gamma_i=7.
\tag{3.2}
\]

At the boundary after \(A^{\alpha_i}\), the forward quantities are

\[
\begin{array}{c|c|c}
&k&\ell\\ \hline
\gamma_i\ge3&0&0\\
\gamma_i=2&0&\alpha_{i+1}\\
\gamma_i=1,\ \gamma_{i+1}\ge2&
 \alpha_{i+1}&\alpha_{i+1}\\
\gamma_i=\gamma_{i+1}=1&
 \alpha_{i+1}&\alpha_{i+1}+\alpha_{i+2}.
\end{array}
\tag{3.3}
\]

The backward quantities are the same table with \(A,C\) interchanged and
indices reversed. In particular:

- if \(\alpha_i\ge3\), then \(k'=\ell'=0\);
- if \(\alpha_i=2\), then \(k'=0\) and
  \(\ell'=\gamma_{i-1}\);
- if \(\alpha_i=1\), then
  \(k'=\gamma_{i-1}\), and \(\ell'\) is either
  \(\gamma_{i-1}\) or \(\gamma_{i-1}+\gamma_{i-2}\).

### Lemma 3.1 — seven-by-seven boundary lemma

Every circular word with seven \(A\)'s and seven \(C\)'s has an
\(A\to C\) boundary satisfying (2.3).

#### Proof

We split according to the number \(t\) of \(A\)-runs.

If \(t=1\), both runs have size seven and the unique boundary has
\(k=\ell=k'=\ell'=0\).

Suppose \(t=2\). Choose an \(A\)-run of size at least four. Its boundary
has \(k'=\ell'=0\). If its following \(C\)-run has size at least three,
it is good. If that \(C\)-run has size two, then (3.3) gives
\(k=0,\ell\le3\). If it has size one, (3.3) is good unless the other
\(A\)-run has size three. In that sole exceptional subcase the other
boundary has an \(A\)-run of size three and a \(C\)-run of size six, so
it is good.

Suppose \(t=3\). Choose an \(A\)-run of size at least three. Again the
backward inequalities are automatic. The other two \(A\)-runs have total
at most four. Formula (3.3) shows that the chosen boundary can fail the
forward inequalities only if its \(C\)-run has size one and the next
\(A\)-run has size three. If this happens, use the boundary after that
next size-three \(A\)-run. It cannot again be followed by a size-three
\(A\)-run, because the third \(A\)-run is positive and the total is seven.
Hence that boundary is good.

Finally suppose \(t\ge4\). If some \(\alpha_i\ge3\), then all the other
\(A\)-parts have size at most two. The backward inequalities at \(i\)
are automatic, and every line of (3.3) gives \(k\le2,\ell\le4\).
If all \(\alpha_i\le2\), the forward inequalities hold at every boundary.
If some \(\alpha_i=2\), use that boundary: here \(k'=0\) and

\[
\ell'=\gamma_{i-1}\le7-(t-1)\le4.
\]

If every \(\alpha_i=1\), then \(t=7\), and (3.2) forces every
\(\gamma_i=1\); every boundary is good.

All cases contain a good boundary. \(\square\)

## 4. Complete support

Choose the good boundary supplied by Lemma 3.1. Lemma 2.1 gives the four
PBBS states in (1.2). Their extras have empty common intersection:

\[
\{a_2,a_1,b\}\cap\{a_1,b,c\}
\cap\{b,c,d_1\}\cap\{c,d_1,d_2\}=\varnothing.
\]

Therefore their full intersection is exactly \(S\), proving (0.1).
The correct-fibre cap \(\binom73=35\) is the general deficit-\((2q+1)\)
cap at \(q=3\). This proves (0.2).

## 5. First obstruction to the naive generalization

Not every \(A\to C\) transition works at depth three. The first arrow in
(1.2) fails by the predecessor/successor test as soon as, for example,
more than two \(A\)-marks occur before \(C_{a_1}\), or more than four
occur before \(C_{a_2}\). Thus a boundary-selection argument is already
needed at depth two and becomes a two-prefix condition at depth three.
At both depths at least one, but not necessarily every, \(A\to C\)
transition works.  The q=3 argument above supplies a valid boundary by
its separate seven-by-seven case split.  More generally, the
global-maximum corridor rule below supplies a valid boundary at every
depth.  This is strictly stronger than choosing an arbitrary
$A\to C$ boundary; explicit arbitrary-boundary counterexamples do not
satisfy the corridor inequalities.

## 6. General all-depth corridor theorem

**Scope warning.**  The ladder is false at an arbitrary $A\to C$
boundary.  What is proved here is that the global-maximum cut satisfies
the stronger two-sided corridor inequalities, and those inequalities
make every sequential PBBS flip legal.  The forward calculation, reverse
calculation, and shared-coordinate audit are all required.

The same calculation isolates the exact all-depth combinatorial gate.
Fix \(q\ge1\), let \(S\) have rank \(m-q\), and put

\[
d=2q+1.
\]

Its expanded unmatched-mark word has \(d\) symbols of each type. At an
\(A_0\to C_0\) boundary, number the \(C\)-symbols forward as

\[
C_0,C_1,\ldots,C_{d-1}
\]

and the \(A\)-symbols backwards as

\[
A_0,A_1,\ldots,A_{d-1}.
\]

For \(1\le j\le q-1\), let \(x_j\) be the number of \(A\)-symbols
strictly between \(C_0\) and \(C_j\), and let \(y_j\) be the number of
\(C\)-symbols encountered moving backwards from \(A_0\) to \(A_j\).
Put \(x_0=y_0=0\).
Call the boundary a two-sided \(2\)-corridor when

\[
\boxed{x_j\le2j,\qquad y_j\le2j\quad(1\le j\le q-1).}
\tag{6.1}
\]

### Theorem 6.1 — a corridor produces a complete \(q\)-shadow occurrence

If a two-sided \(2\)-corridor boundary exists, the \(q+1\) extras

\[
\boxed{
P_t=
\{C_0,\ldots,C_{q-t-1}\}
\cup
\{A_0,\ldots,A_{t-1}\},
\qquad0\le t\le q,}
\tag{6.2}
\]

with an empty range omitted, satisfy

\[
S\cup P_0\longrightarrow S\cup P_1\longrightarrow\cdots
\longrightarrow S\cup P_q
\tag{6.3}
\]

under \(g=f^2\), and

\[
\bigcap_{t=0}^q(S\cup P_t)=S.
\tag{6.4}
\]

#### Proof

Fix \(0\le t<q\), put \(r=q-t-1\), and let

\[
K_t=S\cup\{C_0,\ldots,C_{r-1}\}
       \cup\{A_0,\ldots,A_{t-1}\}.
\tag{6.5}
\]

This is the common rank-\((m-1)\) core of the \(t\)-th two states in
(6.3). The transition deletes \(C_r\) and inserts \(A_t\).

Write the forward \(A\)-marks as

\[
F_0=A_0,F_1,\ldots,F_{d-1},
\qquad A_j=F_{d-j}\quad\text{(indices modulo \(d\))}.
\]

Process the flips \(C_0,\ldots,C_{r-1}\) in that order. Inductively, the
first \(j\) flips remove \(F_1,\ldots,F_{2j}\): before flipping \(C_j\),
condition \(x_j\le2j\) says every old \(A\)-mark preceding \(C_j\) has
already been removed, so the flip removes \(F_{2j+1},F_{2j+2}\).
After all \(r\) such flips, process the cyclically consecutive marks
\(A_0,\ldots,A_{t-1}\). They remove themselves and the next \(t\)
remaining forward marks. Exactly three forward-unmatched marks remain:

\[
\boxed{U_+(K_t)=\{A_t,A_{t+1},A_{t+2}\}.}
\tag{6.6}
\]

Moreover \(x_r\le2r\) puts \(C_r\) before the other two marks in (6.6),
so its strict predecessor there is \(A_t\).

The reversed argument using the \(y_j\)'s gives

\[
\boxed{U_-(K_t)=\{C_r,C_{r+1},C_{r+2}\},}
\tag{6.7}
\]

and the strict successor of \(A_t\) in this triple is \(C_r\). The
deficit-three predecessor/successor law therefore gives

\[
g(K_t\cup\{C_r\})=K_t\cup\{A_t\},
\]

which is the \(t\)-th arrow in (6.3).

The corridor inequalities and the forced shared order \(C_x,A_x\) also
prevent a selected \(C_j\) from coinciding with a selected \(A_h\) in a
way that reduces any \(|P_t|\) or survives every \(P_t\). Explicitly, if
\(C_j=A_h\), then its \(A\)-copy occurs after \(C_j\), so

\[
d-h-1=x_j\le2j.
\]

This is incompatible with \(j+h\le q-1\), the condition needed for that
coordinate to occur in every set in (6.2). Hence the common extras
intersection is empty, proving (6.4). \(\square\)

The following purely circular selection statement supplies the corridor.

### Lemma 6.2 — global-maximum corridor lemma

Every circular word with \(d\) \(A\)'s and \(d\) \(C\)'s has an
\(A\to C\) boundary such that, after indexing from that boundary,

\[
\boxed{x_j\le j,\qquad y_j\le j\quad(1\le j\le d-1).}
\tag{6.8}
\]

In particular, it satisfies (6.1).

#### Proof

Index the \(C\)-symbols cyclically and let

\[
z_i=\#\{\text{\(A\)-symbols strictly between \(C_i\) and \(C_{i+1}\)}\}.
\]

Then

\[
\sum_{i\in\mathbb Z_d}z_i=d.
\tag{6.9}
\]

Extend the prefix potential \(H\) periodically by

\[
H(i+1)-H(i)=z_i-1.
\tag{6.10}
\]

The total increment around the circle is zero. Choose \(i\) at a global
maximum of \(H\). Since

\[
H(i)-H(i-1)=z_{i-1}-1\ge0,
\]

one has \(z_{i-1}\ge1\); hence \(C_i\) is immediately preceded by an
\(A\)-symbol and gives an \(A\to C\) boundary.

For every \(j\ge1\),

\[
\sum_{h=0}^{j-1}z_{i+h}-j
=H(i+j)-H(i)\le0.
\tag{6.11}
\]

The left sum is exactly the number \(x_j\) of \(A\)-symbols before the
\(j\)-th following \(C\)-symbol, proving \(x_j\le j\).

For the backward statement, the \(L\) gaps immediately preceding
\(C_i\) contain

\[
\sum_{h=1}^{L}z_{i-h}
=d-\sum_{h=0}^{d-L-1}z_{i+h}
\ge d-(d-L)=L
\tag{6.12}
\]

\(A\)-symbols, using (6.11) with \(j=d-L\). Taking \(L=j+1\), the current
gap and the preceding \(j\) gaps contain at least \(j+1\) \(A\)-symbols.
Starting at the final \(A\)-symbol in the current gap, the \(j\)-th
previous \(A\)-symbol is therefore reached after crossing at most \(j\)
\(C\)-symbols. This is \(y_j\le j\). \(\square\)

### Theorem 6.3 — complete PBBS intersection support at every depth

For every \(1\le q\le m\) and every

\[
S\in\binom{[2m+1]}{m-q},
\]

there is a canonically oriented \(q\)-edge path under \(g=f^2\),

\[
A_0\longrightarrow A_1\longrightarrow\cdots\longrightarrow A_q,
\]

such that

\[
\boxed{\bigcap_{t=0}^q A_t=S.}
\tag{6.13}
\]

Moreover,

\[
\boxed{
1\le\mu_{P,q}^{\mathrm{corr}}(S)
\le\binom{2q+1}{q}.}
\tag{6.14}
\]

#### Proof

Apply Lemma 6.2 to the expanded unmatched-mark word of \(S\), then apply
Theorem 6.1. The upper bound is the proved correct-fibre cap: the \(q\)
labels deleted from the initial state are distinct members of \(U_-(S)\)
and determine the path. \(\square\)

Theorem 6.3 concerns support. For \(q\ge3\), other PBBS windows can have
rank greater than \(m-q\) because short omitted-label returns exist.
Nothing here bounds their total rank excess or gives a useful
growing-\(q\) collision bound; those remain separate gates for the
constant-one program.

There is therefore the following fixed-depth ledger. Let \(b_q(P_m)\)
be the number of the \(W=\binom{2m+1}m\) PBBS \(q\)-windows whose rank is
larger than \(m-q\), and put \(N_q=\binom{2m+1}{m-q}\). Complete support
uses at least one correct window for every target, so

\[
\boxed{b_q(P_m)\le W-N_q.}
\tag{6.15}
\]

The elementary adjacent-rank telescope gives

\[
W-N_q\le2q(q+1)\operatorname{Cat}_m.
\tag{6.16}
\]

If \(L_q=\binom{2q+1}{q}\), the total correct occurrence mass is at most
\(W\), and every correct load lies in \([1,L_q]\). Hence

\[
\boxed{
\sum_{S\in\binom{[n]}{m-q}}
\binom{\mu_{P,q}^{\mathrm{corr}}(S)-1}{2}
\le
\frac{L_q-2}{2}(W-N_q)
=O_q(\operatorname{Cat}_m).}
\tag{6.17}
\]

Thus every fixed PBBS depth has complete support, Catalan rank defect,
and Catalan high-collision defect.  The constants in (6.17) grow
exponentially with \(q\), so this does not by itself give the required
Gaussian window.
