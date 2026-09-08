# Lane N: a root-associator first matching and the exact endpoint obstruction

Date: 2026-07-26

Method: pure mathematics only. No finite search, computation, solver, or
web input is used.

Write \(C_n=\operatorname {Cat}_n\), and let \(\mathcal D_s\) be the
Dyck words of semilength \(s\), identified with their up-step subsets of
\([2s]\).

## 0. Outcome

There is a uniform root-scale construction, valid for every \(s\ge2\).
Let \(F_s\) be the canonical exact anchored \(\mathcal D_s\)-port factor
and let

\[
                              \tau=(2\ 3).                       \tag{0.1}
\]

The transposition \(\tau\) preserves \(\mathcal D_s\). Reindexing by the
physical initial port, define

\[
                              G_s(P)=\tau F_s(\tau P).            \tag{0.2}
\]

This is an exact anchored factor, not merely a proposed first column. In
particular, its first matching

\[
                              P\longrightarrow Y_0^{G_s}(P)
                               \longrightarrow X_1^{G_s}(P)      \tag{0.3}
\]

has a literal completion through all later \(X/Y\)-states.

Let

\[
 \mathcal F_{s,j}
 =\{\,1A0B:A\in\mathcal D_{j-1},\ B\in\mathcal D_{s-j}\,\},
 \qquad
 |\mathcal F_{s,j}|=C_{j-1}C_{s-j}                               \tag{0.4}
\]

be the canonical first-return fibres. Put, for \(2\le j\le s\),

\[
 A_j=C_{j-2}C_{s-j},\qquad
 B_j=(C_{j-1}-C_{j-2})C_{s-j}.                                  \tag{0.5}
\]

The exact first-insertion quotas of \(G_s\) are

\[
\begin{array}{c|c|c}
\text{initial fibre}&\text{first inserted coordinate}&
                     \text{number of rows}\\ \hline
\mathcal F_{s,1}&2j\quad(2\le j\le s)&A_j\\
\mathcal F_{s,j},\quad j\ge2&3&A_j\\
\mathcal F_{s,j},\quad j\ge2&2j&B_j.
\end{array}                                                       \tag{0.6}
\]

Thus the quotas are exact Catalan integers; no rounding or fractional
matching is involved. For \(s\ge3\), their largest fibre-resolved cell is

\[
 \boxed{
 \max_{1\le j\le s}\max_x
 \#\{P\in\mathcal F_{s,j}:b_1^{G_s}(P)=x\}
       =C_{s-1}-C_{s-2}.}                                      \tag{0.7}
\]

Consequently, in the zero-background ledger in which the canonical
first-return label is retained, this one exact factor splits every fibre
below a hard cap \(p\) if and only if

\[
                              p\ge C_{s-1}-C_{s-2}.               \tag{0.8}
\]

The exact normalization is

\[
 {C_{s-1}-C_{s-2}\over C_s}
 =\frac{3(s+1)(s-2)}{4(2s-1)(2s-3)}
 \longrightarrow\frac3{16}.                                    \tag{0.9}
\]

Equivalently, if \(\theta=C_s/p\), condition (0.8) is

\[
 \theta\le
 \frac{4(2s-1)(2s-3)}{3(s+1)(s-2)}
 \longrightarrow\frac{16}{3}.                                  \tag{0.10}
\]

There is also a sharp obstruction, and it must not be confused with
(0.7). After the fibre labels are forgotten, every exact anchored factor
\(H\), not only \(G_s\), satisfies

\[
 h_H(1)=0,\qquad
 \max_{x\in[2s]}h_H(x)=h_H(2s)=C_{s-1},                          \tag{0.11}
\]

where \(h_H(x)\) is the number of rows which insert \(x\) first. Hence a
raw physical first-insertion histogram obeys the hard cap \(p\) precisely
when \(p\ge C_{s-1}\). No exact factor can improve this maximum.

The source of (0.11) is the pair \(\{1,2s\}\): every Dyck port contains
1 and omits \(2s\). For \(s\ge3\), it is the unique fully saturated
unordered coordinate pair, and for every \(s\) it is the unique saturated
pair with a fixed orientation over all roots. This is the exact universal
endpoint-pair obstruction. It is not a proof that no higher-order Hall or
carrier obstruction exists.

Therefore this note proves a nontrivial recursive first-matching theorem
and identifies the sharp raw obstruction. It does **not** prove
coefficient one: (0.7) is a fibre-resolved statement, and arbitrary
physical carrier collisions or pre-existing background must still be
charged before applying a cap.

## 1. Dyck grammar and the canonical first edge

Use \(1\) for an up-step and \(0\) for a down-step. Every nonempty Dyck
word has the unique first-return decomposition

\[
                              P=1A0B,                              \tag{1.1}
\]

where \(A,B\) are Dyck words. If \(|A|=j-1\), then the first return of
\(P\) occurs at position \(2j\), and \(P\in\mathcal F_{s,j}\).

For the canonical factor \(F_s\), the first inserted coordinate is exactly
that first-return position:

\[
                              b_1^{F_s}(P)=2j
                   \qquad(P\in\mathcal F_{s,j}).        \tag{1.2}
\]

Thus its first histogram is

\[
 h_{F_s}(2j)=C_{j-1}C_{s-j},\qquad h_{F_s}(2j-1)=0.     \tag{1.3}
\]

The construction below changes the complete factor, not only (1.2).
This distinction is essential: a Dyck grammar successor is another Dyck
port, whereas a legal \(X_1\)-state is outside the initial port set.

## 2. The root associator involution

### Lemma 2.1 (Dyck preservation)

For \(s\ge2\), \(\tau=(2\ 3)\) maps \(\mathcal D_s\) bijectively to
itself.

#### Proof

If symbols two and three agree, there is nothing to prove. Otherwise the
first three symbols are either \(110\) or \(101\), because every Dyck word
starts with \(1\). Swapping them exchanges these two prefixes. Both have
nonnegative partial heights, and the height after position three is
unchanged. Every later partial height is therefore unchanged. Since
\(\tau\) is an involution, it is a bijection. \(\square\)

For \(2\le j\le s\), define

\[
\begin{aligned}
 \mathcal A_{s,j}
   &=\{\,1(10R)0V:R\in\mathcal D_{j-2},
                     V\in\mathcal D_{s-j}\,\},\\
 \mathcal A'_{s,j}
   &=\{\,10(1R0)V:R\in\mathcal D_{j-2},
                     V\in\mathcal D_{s-j}\,\},\\
 \mathcal B_{s,j}
   &=\mathcal F_{s,j}\setminus\mathcal A_{s,j}.
                                                                    \tag{2.1}
\end{aligned}
\]

The first family consists of those class-\(j\) roots whose left Dyck word
begins with the singleton component \(10\). The second lies in class one;
the first primitive component of its tail has semilength \(j-1\).

### Theorem 2.2 (recursive root matching)

For every \(s\ge2\),

\[
 \mathcal F_{s,1}=\biguplus_{j=2}^s\mathcal A'_{s,j},
 \qquad
 \mathcal F_{s,j}=\mathcal A_{s,j}\mathbin{\dot\cup}
                   \mathcal B_{s,j}\quad(j\ge2),       \tag{2.2}
\]

and \(\tau\) exchanges \(\mathcal A_{s,j}\) with
\(\mathcal A'_{s,j}\) while fixing \(\mathcal B_{s,j}\) pointwise.
Moreover,

\[
 |\mathcal A_{s,j}|=|\mathcal A'_{s,j}|=A_j,\qquad
 |\mathcal B_{s,j}|=B_j.                              \tag{2.3}
\]

#### Proof

The displayed words in (2.1) differ exactly by swapping symbols two and
three:

\[
                              110R0V\longleftrightarrow101R0V.  \tag{2.4}
\]

Every word in \(\mathcal F_{s,1}\) is \(10W\), and the unique first
primitive component \(1R0\) of \(W\) determines exactly one
\(j\in\{2,\ldots,s\}\). This proves the first disjoint union. If
\(P=1A0B\in\mathcal F_{s,j}\), \(j\ge2\), then \(A\) begins either \(10\)
or \(11\). The first case is \(\mathcal A_{s,j}\); in the second case
symbols two and three of \(P\) are both \(1\), so \(\tau P=P\). This
proves (2.2) and the action statement.

There are \(C_{j-2}\) choices for \(R\) and \(C_{s-j}\) choices for \(V\),
giving \(A_j\). Subtracting from
\(|\mathcal F_{s,j}|=C_{j-1}C_{s-j}\) gives \(B_j\). \(\square\)

In ordered-tree notation, with \(N(L,R)\) denoting a root with left and
right subtrees, the nontrivial pairs are exactly the root associator moves

\[
 N(\varnothing,N(R,V))
       \longleftrightarrow
 N(N(\varnothing,R),V).                               \tag{2.5}
\]

Thus (2.2) is genuinely recursive in the first-return grammar, rather
than a finite embedded pentagon.

The involution moves exactly \(2C_{s-1}\) roots, because

\[
 \sum_{j=2}^s A_j
 =\sum_{a+b=s-2}C_aC_b=C_{s-1}.                       \tag{2.6}
\]

Its moved fraction is

\[
 {2C_{s-1}\over C_s}={s+1\over2s-1}\longrightarrow\frac12.    \tag{2.7}
\]

## 3. Exact completion of the first matching

Write the canonical factor row as

\[
 X_0^{F_s}(Q),Y_0^{F_s}(Q),X_1^{F_s}(Q),\ldots,
 Y_{s-1}^{F_s}(Q),X_s^{F_s}(Q).                       \tag{3.1}
\]

Define every state of \(G_s\), not merely its first state, by

\[
\begin{aligned}
 X_t^{G_s}(P)&=\tau X_t^{F_s}(\tau P),\qquad 0\le t\le s,\\
 Y_t^{G_s}(P)&=\tau Y_t^{F_s}(\tau P),\qquad 0\le t<s.
                                                                    \tag{3.2}
\end{aligned}
\]

### Theorem 3.1 (exact conjugate factor)

The states (3.2) form an exact anchored \(\mathcal D_s\)-port
complement-path factor. In particular, (0.3) is a pair of bijective
ownership matchings and has a literal completion through phase \(s\).

#### Proof

By Lemma 2.1, \(P\mapsto\tau P\) permutes the row labels. Applying a
coordinate permutation preserves set sizes, inclusion, and Johnson
adjacency. Since \(F_s\) owns every \(s\)-set and every \((s+1)\)-set
exactly once, (3.2) has the same complete \(X/Y\) ownership ledgers.

At the initial endpoint,

\[
 X_0^{G_s}(P)=\tau(\tau P)=P.                         \tag{3.3}
\]

Coordinate permutations commute with complement, so

\[
 X_s^{G_s}(P)
 =\tau\bigl([2s]\setminus\tau P\bigr)
 =[2s]\setminus P.                                   \tag{3.4}
\]

Thus every row has its prescribed ordered endpoints and all ledgers are
exact. \(\square\)

For a completely explicit first column, let \(a_1^{F_s}(Q)\) be the
coordinate deleted on the first canonical transition. Then

\[
\begin{aligned}
 b_1^{G_s}(P)&=\tau\bigl(b_1^{F_s}(\tau P)\bigr),\\
 a_1^{G_s}(P)&=\tau\bigl(a_1^{F_s}(\tau P)\bigr),\\
 Y_0^{G_s}(P)&=P\cup\{b_1^{G_s}(P)\},\\
 X_1^{G_s}(P)&=P\setminus\{a_1^{G_s}(P)\}
                         \cup\{b_1^{G_s}(P)\}.        \tag{3.5}
\end{aligned}
\]

Distinctness of all \(Y_0\)'s and \(X_1\)'s follows from the complete
factor proof; it is not an unproved Hall assumption.

## 4. Exact first-return quotas

For a factor \(H\), define the fibre-resolved first histogram

\[
 h^H_{s,j}(x)
 =\#\{P\in\mathcal F_{s,j}:b_1^H(P)=x\}.              \tag{4.1}
\]

### Theorem 4.1 (quota formula)

For \(G_s\), the nonzero entries of (4.1) are exactly those in (0.6).

#### Proof

If \(P\in\mathcal A'_{s,j}\subset\mathcal F_{s,1}\), then
\(\tau P\in\mathcal A_{s,j}\subset\mathcal F_{s,j}\). Equations
(1.2) and (3.5) give

\[
 b_1^{G_s}(P)=\tau(2j)=2j,\qquad j\ge2.               \tag{4.2}
\]

If \(P\in\mathcal A_{s,j}\), then
\(\tau P\in\mathcal F_{s,1}\), so

\[
 b_1^{G_s}(P)=\tau(2)=3.                              \tag{4.3}
\]

Finally, \(\tau\) fixes every \(P\in\mathcal B_{s,j}\), and it fixes
the coordinate \(2j\ge4\), whence

\[
 b_1^{G_s}(P)=2j.                                     \tag{4.4}
\]

The counts are (2.3). \(\square\)

Equivalently, relative to the canonical first histogram and with \(e_x\)
denoting the target basis vector, the exact signed action on each fibre is

\[
\begin{aligned}
 \Delta_{s,1}
  &=\sum_{j=2}^s A_j e_{2j}-C_{s-1}e_2,\\
 \Delta_{s,j}
  &=A_j(e_3-e_{2j}),\qquad2\le j\le s.                \tag{4.5}
\end{aligned}
\]

Summing over the fibres gives

\[
\begin{aligned}
 h_{G_s}(3)&=\sum_{j=2}^sA_j=C_{s-1},\\
 h_{G_s}(2j)&=A_j+B_j=C_{j-1}C_{s-j},
                         \qquad2\le j\le s,\\
 h_{G_s}(x)&=0\quad\text{for all other }x.            \tag{4.6}
\end{aligned}
\]

Thus

\[
                              h_{G_s}=\tau_*h_{F_s}.    \tag{4.7}
\]

Formula (4.6) is the first essential caveat: the exact gains in (0.6)
collide after the first-return label is forgotten.

## 5. Sharp cap for the resolved construction

Put

\[
                              d_n=C_n-C_{n-1}\qquad(n\ge1).       \tag{5.1}
\]

### Theorem 5.1 (largest resolved quota)

For \(s\ge3\), every entry in (0.6) is at most \(d_{s-1}\), and equality
is attained by \(B_s=d_{s-1}\). Hence (0.7) holds.

#### Proof

The concatenation map on Dyck words is injective, so

\[
                              C_aC_b\le C_{a+b}.        \tag{5.2}
\]

Every \(A_j\) has indices summing to \(s-2\), and therefore

\[
                              A_j\le C_{s-2}.           \tag{5.3}
\]

For \(s\ge3\),

\[
 {d_{s-1}\over C_{s-2}}
 ={C_{s-1}\over C_{s-2}}-1
 =\frac{3(s-2)}s\ge1.                                 \tag{5.4}
\]

Thus all \(A_j\)-entries are at most \(d_{s-1}\).

For \(B_j\), set \(a=j-1\), \(b=s-j\), so \(a+b=s-1\). The ratio

\[
 r_n={d_n\over C_n}=\frac{3(n-1)}{2(2n-1)}             \tag{5.5}
\]

is increasing in \(n\). Using (5.2),

\[
 B_j=d_aC_b
     =r_aC_aC_b
     \le r_aC_{a+b}
     \le r_{a+b}C_{a+b}
     =d_{s-1}.                                         \tag{5.6}
\]

At \(j=s\), \(b=0\), and (5.6) is equality:

\[
                              B_s=C_{s-1}-C_{s-2}.      \tag{5.7}
\]

This proves the theorem. \(\square\)

For \(s=2\), the largest resolved cell is \(1\); the expression
\(C_1-C_0\) vanishes, so the \(s\ge3\) quantifier in Theorem 5.1 is
necessary.

Since the maximum for this construction is attained, its zero-background
hard-cap condition is exactly (0.8), not merely sufficient. This is not
an optimality theorem over all exact factors.

## 6. The universal raw endpoint theorem

Let \(H\) be an arbitrary exact anchored \(\mathcal D_s\)-port factor.
Every row is a length-\(s\) complement geodesic. Hence every coordinate
present initially is deleted exactly once, and every absent coordinate is
inserted exactly once.

In the row rooted at \(P\), let

* \(a(P)\) be the transition on which coordinate \(1\) is deleted;
* \(b(P)\) be the transition on which coordinate \(2s\) is inserted.

Every Dyck port contains \(1\) and omits \(2s\).

### Theorem 6.1 (forced endpoint rows)

Exactly \(C_{s-1}\) rows satisfy

\[
                              b(P)=1,\qquad a(P)=s.      \tag{6.1}
\]

All other rows delete \(1\) before inserting \(2s\). In particular,

\[
                              h_H(2s)=C_{s-1}.           \tag{6.2}
\]

#### Proof

The number of \(X\)-states in row \(P\) containing both endpoint
coordinates is

\[
                              (a(P)-b(P))_+.            \tag{6.3}
\]

The number of adjacent-union \(Y\)-states containing both is

\[
                              (a(P)-b(P)+1)_+.          \tag{6.4}
\]

Their difference is one exactly when \(b(P)\le a(P)\).

The complete \(X/Y\) ledgers therefore give

\[
 \sum_{P\in\mathcal D_s}(a(P)-b(P))_+
   =\binom{2s-2}{s-2}=(s-1)C_{s-1},                    \tag{6.5}
\]

and

\[
\begin{aligned}
 \#\{P:b(P)\le a(P)\}
  &=\binom{2s-2}{s-1}-\binom{2s-2}{s-2}\\
  &=C_{s-1}.                                           \tag{6.6}
\end{aligned}
\]

Only the rows counted in (6.6) contribute to (6.5), and each contributes
at most \(s-1\). The right side of (6.5) is the maximum possible total
\(C_{s-1}(s-1)\). Hence every counted row has

\[
                              a(P)-b(P)=s-1,            \tag{6.7}
\]

which forces (6.1). Conversely, \(b(P)=1\) always implies
\(b(P)\le a(P)\), so the first-insertion rows are exactly these
\(C_{s-1}\) rows. \(\square\)

There is a useful strengthening.

### Theorem 6.2 (exact minimax first histogram)

For every exact anchored factor \(H\) and every coordinate \(x\ne1\),

\[
                              h_H(x)\le C_{s-1}.        \tag{6.8}
\]

Together with (6.2), this proves (0.11).

#### Proof

Again use the pair \(\{1,x\}\). A root which already contains \(x\)
cannot insert \(x\) first. In a root which omits \(x\), let \(i_x(P)\)
be its insertion time and retain \(a(P)\) for the deletion time of \(1\).

Rows initially containing both coordinates contribute equally many
pair-containing \(X\)- and \(Y\)-states. A split row contributes one more
\(Y\)-state precisely when

\[
                              i_x(P)\le a(P).           \tag{6.9}
\]

The aggregate \(Y-X\) pair count is

\[
 \binom{2s-2}{s-1}-\binom{2s-2}{s-2}=C_{s-1}.          \tag{6.10}
\]

Thus exactly \(C_{s-1}\) roots omitting \(x\) satisfy (6.9). Every row
which inserts \(x\) first lies among them, proving (6.8). Coordinate \(1\)
is present in every root, so \(h_H(1)=0\). Theorem 6.1 supplies equality
at \(2s\). \(\square\)

### Corollary 6.3 (sharp raw cap and forced excess)

A hard raw constraint

\[
                              h_H(x)\le p\quad(x\in[2s])           \tag{6.11}
\]

holds for every exact factor when \(p\ge C_{s-1}\), and for no exact
factor when \(p<C_{s-1}\). Also

\[
 \sum_x(h_H(x)-p)_+\ge(C_{s-1}-p)_+.                  \tag{6.12}
\]

The often-used sufficient obstruction \(C_s\ge4p\) is valid but not
sharp, since

\[
 {C_{s-1}\over C_s}
 =\frac{s+1}{2(2s-1)}
 =\frac14+\frac3{4(2s-1)}.                            \tag{6.13}
\]

Under \(C_s\ge4p\), (6.12) gives only

\[
 C_{s-1}-p\ge\frac{3C_s}{4(2s-1)}=o(C_s).             \tag{6.14}
\]

Thus the endpoint theorem blocks a hard cap, but by itself does not block
an \(o(C_s)\)-overload objective.

## 7. Why the endpoint pair is the unique saturated one

The following classification fixes the precise scope of the word
“unique.”

For distinct coordinates \(u,v\), call a split row a **crossing row** if
the absent member is inserted no later than the present member is
deleted. The same pair-ledger calculation as (6.10) shows that every
exact factor has exactly \(C_{s-1}\) crossing rows for every pair.

If both \(u,v\) are present initially, let \(d_P(u),d_P(v)\) be their
deletion times. If both are absent, let \(i_P(u),i_P(v)\) be their
insertion times. Define

\[
\begin{aligned}
 B_{uv}={}&
 \sum_{P:u,v\in P}\min\{d_P(u),d_P(v)\}\\
 &+\sum_{P:u,v\notin P}
        \bigl(s+1-\max\{i_P(u),i_P(v)\}\bigr).         \tag{7.1}
\end{aligned}
\]

The complete \(X\)-ledger gives the exact defect identity

\[
 \sum_{\text{crossing }P}
 \left[(s-1)-
  \bigl(d_P(\text{present})-i_P(\text{absent})\bigr)\right]
 =B_{uv}.                                              \tag{7.2}
\]

Indeed, a crossing split row contributes the displayed time difference
to the pair-containing \(X\)-count; a noncrossing split row contributes
zero; the both-present and both-absent rows contribute exactly (7.1).
The total pair-containing \(X\)-count is \((s-1)C_{s-1}\), while there
are \(C_{s-1}\) crossing rows. Rearranging gives (7.2).

Consequently, all crossing rows are maximally saturated if and only if
\(B_{uv}=0\), which holds if and only if every Dyck port contains exactly
one of \(u,v\).

### Proposition 7.1 (saturated-pair classification)

For \(s\ge3\), the only unordered pair split by every Dyck port is
\(\{1,2s\}\).

#### Proof

The Dyck port \([s]\) rules out a pair with both coordinates in
\([s]\), and it also rules out a pair with both coordinates in
\(\{s+1,\ldots,2s\}\). Thus write \(u\le s<v\).

If \(v<2s\), choose

\[
                              r\in[2,s]\setminus\{u\},             \tag{7.3}
\]

which is possible for \(s\ge3\). The set

\[
                              [s]\setminus\{r\}\cup\{v\}          \tag{7.4}
\]

is a Dyck port and contains both \(u\) and \(v\), a contradiction. To
check the Dyck condition, relative to the initial block \([s]\), the
first changed step is the down-step at \(r\ge2\); the height there is
\(r-2\ge0\), and before the compensating up-step at \(v\le2s-1\) the
height never falls below zero.

Hence \(v=2s\). If \(u>1\), then

\[
                              [s]\setminus\{u\}\cup\{s+1\}        \tag{7.5}
\]

is a Dyck port containing neither \(u\) nor \(2s\), again a contradiction.
Thus \(u=1\). \(\square\)

For \(s=2\), \(\{2,3\}\) is a second split pair, but its orientation
varies between roots; it does not force one fixed first-insertion target.
For every \(s\), coordinate \(1\) is the unique coordinate present in all
Dyck ports and \(2s\) is the unique coordinate absent from all Dyck ports.
Therefore \(\{1,2s\}\) is always the unique saturated
**fixed-orientation** endpoint pair.

## 8. Carrier and integrality caveats

The construction preserves integrality in the strongest possible way:
it stays inside one exact factor and explicitly constructs every literal
state. Nevertheless, three scopes must remain separate.

1. **Resolved versus physical cells.** Bound (0.7) applies to cells
   labelled by both the canonical first-return fibre \(j\) and the target
   \(x\). If different fibres map to the same physical target, their
   loads add. Equations (4.6) show that this restores the forced raw load
   \(C_{s-1}\).

2. **Ambient background.** If a carrier gives resolved cell \((j,x)\)
   a pre-existing load \(\beta_{j,x}\), zero overload requires the exact
   inequalities

   \[
                              \beta_{j,x}+h^{G_s}_{s,j}(x)\le p.   \tag{8.1}
   \]

   The scalar condition (0.8) is neither necessary nor sufficient after
   arbitrary backgrounds are introduced. With a common exterior set
   \(O\), the target basis vector \(e_x\) in (4.5) becomes the physical
   target \(e_{O\cup\{x\}}\); equal exterior cores cause the same
   collisions as (4.6).

3. **Whole-factor conjugation.** The proof does not splice the new first
   column into the old canonical tail. All phases are conjugated by
   (3.2). Fixed rowwise \(Y\)-colors or carrier profiles need not be
   preserved, although the complete aggregate \(X/Y\) ledgers and ports
   are preserved exactly.

Hence the construction solves the integral root first-matching and
completion problem for the quotas (0.6). It does not by itself prove a
favourable multidepth PCap drift.

## 9. Independent audits and exact boundary

The two decisive calculations were audited independently.

* The fibre audit used the disjoint grammar partition (2.2). It recovered
  \(A_j\), \(B_j\), the collision identities (4.6), and the exact maximum
  \(C_{s-1}-C_{s-2}\). It also found the necessary \(s\ge3\) restriction
  and the resolved-versus-raw caveat.
* The endpoint audit recomputed the rowwise \(X/Y\) containment counts,
  proved (6.1), sharpened the raw cap threshold to the exact value
  \(C_{s-1}\), and classified the saturated pair via (7.2). It also found
  the exceptional unoriented pair \(\{2,3\}\) at \(s=2\).

Both audits agree with the summed conjugacy identity (4.7). In particular,
the \(C_{s-1}\) forced rows at target \(2s\) split under \(G_s\) as

\[
 C_{s-2}\quad\text{from }\mathcal F_{s,1},
 \qquad
 C_{s-1}-C_{s-2}\quad\text{from }\mathcal F_{s,s}.      \tag{9.1}
\]

Proved:

1. The root associator involution (2.5) matches class one recursively to a
   distinguished Catalan subfamily of every higher first-return class.
2. Conjugating the full canonical factor gives one literal exact factor,
   with no residual Hall or monodromy assumption.
3. The first-insertion quotas are exactly (0.6).
4. Their largest fibre-resolved cell is exactly
   \(C_{s-1}-C_{s-2}\) for \(s\ge3\).
5. Every exact factor has raw first-histogram maximum exactly \(C_{s-1}\),
   forced at coordinate \(2s\).
6. For \(s\ge3\), \(\{1,2s\}\) is the unique fully saturated pair; for
   every \(s\), it is the unique saturated pair with fixed orientation.

Not proved:

* that \(C_{s-1}-C_{s-2}\) is the smallest possible maximum over all
  fibre-resolved exact factors;
* floor/ceiling equidistribution inside every fibre when
  \(p<C_{s-1}-C_{s-2}\);
* favourable drift after arbitrary carrier collisions or ambient loads;
* control of every later start-resolved target profile needed for
  coefficient one.

The exact advance is therefore the recursive completed factor (0.2) with
the quotas (0.6), together with the sharp endpoint theorem (0.11). Any
next construction must either split the residual \(B_j\) classes by a
larger exact factor move or exploit carrier separation; it cannot lower
the raw physical first-insertion maximum below \(C_{s-1}\).
