# Lane N: the full-swap Motzkin first matching and the sharp conjugacy obstruction

Date: 2026-07-26

Method: pure mathematics only. No finite search, computation, solver, or
web input is used.

Write \(C_n=\operatorname {Cat}_n\). Let \(\mathcal D_s\) be the Dyck
ports of semilength \(s\), and let \(F_s\) be the canonical exact anchored
\(\mathcal D_s\)-port factor.

## 0. Verdict

Put

\[
 H_s=\left\langle(2\ 3),(4\ 5),\ldots,
                         (2s-2\ 2s-1)\right\rangle              \tag{0.1}
\]

and let

\[
 \omega_s=(2\ 3)(4\ 5)\cdots(2s-2\ 2s-1).                       \tag{0.2}
\]

Every \(h\in H_s\) preserves the Dyck ports. Hence

\[
 G_h(P)=hF_s(hP),\qquad P\in\mathcal D_s,                        \tag{0.3}
\]

is a literal exact anchored factor.

The full swap \(G_{\omega_s}\) has an exact root-scale first matching

\[
 P\longrightarrow Y_0(P)\longrightarrow X_1(P)                 \tag{0.4}
\]

whose complete first-return-resolved quota matrix can be written in
closed form.

Define \(R_n\) by

\[
 R(z)=\sum_{n\ge0}R_nz^n
     =\frac1{1-z^2C(z)^2}
     =\frac{C(z)^2}{2C(z)-1}.                                   \tag{0.5}
\]

Equivalently, \(R_n\) counts Dyck words of semilength \(n\) having no
singleton primitive component.

\[
 R_0=1,\qquad R_1=0,\qquad
 R_n=\sum_{\ell=2}^n C_{\ell-1}R_{n-\ell}\quad(n\ge2).             \tag{0.5a}
\]

Let \(\mathcal F_{s,j}\) be the roots whose first return is \(2j\). For
\(1\le j,k\le s\), let \(M^{(s)}_{jk}\) be the number of
\(P\in\mathcal F_{s,j}\) for which \(\omega_sP\) has first-return
semilength \(k\). Then \(M^{(s)}\) is symmetric and

\[
 M^{(s)}_{jk}=
 \begin{cases}
  0,&j=k<s,\\[2mm]
  R_{\min(j,k)-1}\,
  C_{|j-k|-1}\,
  C_{s-\max(j,k)},&
     j\ne k,\ \max(j,k)<s,\\[2mm]
  R_{j-1}C_{s-j-1},&j<s,\ k=s,\\[1mm]
  R_{k-1}C_{s-k-1},&k<s,\ j=s,\\[1mm]
  R_{s-1},&j=k=s.
 \end{cases}                                                   \tag{0.6}
\]

The corresponding physical first-insertion target is

\[
 \lambda_s(k)=
 \begin{cases}
  2k+1,&k<s,\\
  2s,&k=s.
 \end{cases}                                                   \tag{0.7}
\]

Thus the exact quota in source fibre \(j\) at target \(\lambda_s(k)\)
is \(M^{(s)}_{jk}\).

For every \(s\ge3\),

\[
 \boxed{
 \max_{j,x}
 \#\{P\in\mathcal F_{s,j}:b_1^{G_{\omega_s}}(P)=x\}
 =R_{s-1}.}                                                     \tag{0.8}
\]

More strongly,

\[
 \boxed{
 \min_{h\in H_s}\ 
 \max_{j,x}
 \#\{P\in\mathcal F_{s,j}:b_1^{G_h}(P)=x\}
 =R_{s-1}.}                                                     \tag{0.9}
\]

Hence the full swap is minimax-optimal among all flaw-preserving
coordinate-conjugate factors (0.3). Its exact zero-background resolved
cap threshold is

\[
                              p\ge R_{s-1}.                       \tag{0.10}
\]

The asymptotic constant is

\[
 R_n\sim\frac49C_n,\qquad
 \frac{R_{s-1}}{C_s}\longrightarrow\frac19.                     \tag{0.11}
\]

Thus, with \(\theta=C_s/p\), this construction covers the exact
first-return-resolved range

\[
                              \theta\le\frac{C_s}{R_{s-1}}
                                      =9+o(1).                   \tag{0.12}
\]

The residual \(R_{s-1}\)-cell is not an artefact of the full swap.
It is fixed at first-return class \(s\) by every \(h\in H_s\). To beat
(0.8) within this coordinate-conjugacy grammar, a move must change the
uncoloured Motzkin up/down skeleton; merely flipping the horizontal
colours cannot suffice.

After source-fibre labels are forgotten, the universal endpoint theorem
still forces raw load \(C_{s-1}\) at target \(2s\). Thus (0.8) is a
resolved endpoint-class theorem, not a raw physical cap theorem.

For \(s=2\), \(R_1=0\) but the two off-diagonal quotas are \(1\); the
minimax value is \(1\). All minimax statements below therefore retain the
quantifier \(s\ge3\).

## 1. The coordinate-conjugate exact factors

For \(1\le i\le s-1\), write

\[
                              \sigma_i=(2i\ 2i+1).                 \tag{1.1}
\]

### Lemma 1.1 (Dyck preservation)

Every \(\sigma_i\), and hence every \(h\in H_s\), maps
\(\mathcal D_s\) bijectively to itself.

#### Proof

Immediately before positions \(2i,2i+1\), a Dyck word has an odd
nonnegative height, hence height at least one. Equal adjacent symbols are
unchanged. Swapping \(01\) to \(10\) can only raise the intermediate
height. Swapping \(10\) to \(01\) lowers that intermediate height by two,
but the new first step is a down-step from height at least one, so the
new height is still nonnegative. The height after both positions is
unchanged, and all later heights agree. Since \(\sigma_i\) is an
involution, it is a bijection. \(\square\)

### Lemma 1.2 (literal exact completion)

For every \(h\in H_s\), define all phases by

\[
\begin{aligned}
 X_t^{G_h}(P)&=hX_t^{F_s}(hP),\qquad0\le t\le s,\\
 Y_t^{G_h}(P)&=hY_t^{F_s}(hP),\qquad0\le t<s.
                                                                    \tag{1.2}
\end{aligned}
\]

These states form an exact anchored \(\mathcal D_s\)-port
complement-path factor.

#### Proof

The map \(P\mapsto hP\) permutes the roots. A coordinate permutation
preserves inclusion and Johnson adjacency, and it permutes both complete
set ranks. Thus (1.2) has the complete \(X/Y\) ledgers. Also

\[
 X_0^{G_h}(P)=h(hP)=P,\qquad
 X_s^{G_h}(P)=h([2s]\setminus hP)=[2s]\setminus P,      \tag{1.3}
\]

because every \(h\in H_s\) is an involution and commutes with complement.
\(\square\)

In particular, no residual Hall or monodromy lemma is being assumed.
The first matching is completed by the explicitly conjugated later
phases.

## 2. The two-coloured Motzkin grammar

Fix \(P=p_1p_2\cdots p_{2s}\in\mathcal D_s\). Necessarily
\(p_1=1\) and \(p_{2s}=0\). Put \(n=s-1\). For
\(1\le i\le n\), replace the pair

\[
                              (p_{2i},p_{2i+1})                    \tag{2.1}
\]

by a two-coloured Motzkin step:

\[
\begin{array}{c|c}
11&\text{up}\\
00&\text{down}\\
01&\alpha\text{-horizontal}\\
10&\beta\text{-horizontal}.
\end{array}                                                       \tag{2.2}
\]

### Lemma 2.1 (Catalan--Motzkin bijection)

The map (2.2) is a bijection between \(\mathcal D_s\) and
two-coloured Motzkin excursions of length \(s-1\).

#### Proof

Let \(H(t)\) be the Dyck height after position \(t\). At every odd
position,

\[
                              H(2i+1)=1+2m_i                         \tag{2.3}
\]

for an integer \(m_i\ge0\). The four pairs in (2.2) change \(m_i\) by
\(+1,-1,0,0\), respectively. A \(00\)-pair can occur only above ground,
so these steps form a nonnegative Motzkin excursion.

Conversely, expand the four step types according to (2.2), prepend the
initial \(1\), and append the final \(0\). A Motzkin down-step starts
above ground, so its two zeros cannot make the Dyck height negative.
An \(\alpha\)-horizontal at Motzkin ground may touch Dyck height zero
after its first symbol, which is allowed. The resulting word is Dyck.
The constructions are inverse. \(\square\)

The full swap \(\omega_s\) fixes the up/down steps and exchanges the two
horizontal colours.

### Lemma 2.2 (first-return reading rule)

For \(j<s\), \(P\) has first-return semilength \(j\) if and only if step
\(j\) is the first ground-level \(\alpha\)-horizontal step. If there is
no ground-level \(\alpha\)-horizontal, then \(P\) has first-return
semilength \(s\).

Similarly, \(\omega_sP\) has first-return semilength \(k<s\) if and only
if step \(k\) is the first ground-level \(\beta\)-horizontal step; it has
class \(s\) if there is no such step.

#### Proof

At odd word positions the height in (2.3) is positive. At an even
position \(2j<2s\), the height can first become zero only when the
Motzkin path is at ground and the first symbol of the corresponding pair
is \(0\). This is exactly a ground \(\alpha=01\) step. If none occurs,
the first return is the final appended zero at \(2s\). The statement for
\(\omega_sP\) follows because \(\omega_s\) exchanges \(\alpha\) and
\(\beta\). \(\square\)

This is the required first-return grammar: the two endpoint classes are
the first occurrences of two colours in one common ground-atom word.

### Proposition 2.3 (exact action of every partial swap)

Let \(S\subseteq[s-1]\) and

\[
                              h_S=\prod_{i\in S}(2i\ 2i+1).        \tag{2.4}
\]

For a Dyck word \(P\), define

\[
\begin{aligned}
 \mathsf C(P)
   &=\{\,i<s:H_P(2i)=0\,\},\\
 \mathsf L(P)
   &=\{\,i<s:H_P(2i-1)=1,\
                  (p_{2i},p_{2i+1})=(1,0)\,\}.
                                                                    \tag{2.5}
\end{aligned}
\]

Thus \(\mathsf C(P)\) is the set of top-level component cuts, and
\(\mathsf L(P)\) is the set of singleton components in the left forest
of the current top-level root. Then

\[
 \boxed{
 \mathsf C(h_SP)
   =\bigl(\mathsf C(P)\setminus S\bigr)
      \cup\bigl(\mathsf L(P)\cap S\bigr).}             \tag{2.6}
\]

Consequently the first-return semilength of \(h_SP\) is

\[
 J_S(P)=
 \min\left(
  (\mathsf C(P)\setminus S)
   \cup(\mathsf L(P)\cap S)\cup\{s\}\right),            \tag{2.7}
\]

and the first physical target in \(G_{h_S}\) is

\[
                              b_1^{G_{h_S}}(P)=h_S(2J_S(P)).       \tag{2.8}
\]

#### Proof

If \(i\notin S\), the height at \(2i\) is unchanged, so a cut persists
exactly when \(i\in\mathsf C(P)\). If \(i\in S\), an old cut has local
pair \(01\) and is destroyed by the swap to \(10\). A new cut is created
exactly when the old height at \(2i-1\) was one and the local pair was
\(10\), which is \(i\in\mathsf L(P)\). This proves (2.6). Taking the
first cut proves (2.7), and canonical first-return insertion followed by
coordinate conjugation proves (2.8). \(\square\)

There is also an exact recursion for the retained top cell. Write a
primitive root as \(P=1A0\), where \(A\) has semilength \(n=s-1\).
For \(0\le t\le n\), let \(\rho_S(t)\) count suffix forests of total
semilength \(n-t\) in which no singleton component begins at a selected
global position. Then

\[
\begin{aligned}
 \rho_S(n)&=1,\\
 \rho_S(t)
   &=\sum_{\ell=1}^{n-t}
       \mathbf1_{\{\ell\ge2\ \mathrm{or}\ t+1\notin S\}}\,
       C_{\ell-1}\rho_S(t+\ell).                       \tag{2.9}
\end{aligned}
\]

The top-to-top load of \(G_{h_S}\) is exactly \(\rho_S(0)\). Formula
(2.9) is monotone decreasing in \(S\); when \(S=[s-1]\), only primitive
components of size at least two remain, and

\[
                              \rho_{[s-1]}(0)=R_{s-1}.             \tag{2.10}
\]

Thus the full swap is already forced by the exact partial-swap recursion:
it minimizes the retained top cell.

## 3. Ground atoms and the exact quota matrix

Let \(M(z)\) be the generating function of arbitrary two-coloured
Motzkin excursions, counted by length. A ground-level excursion is a
sequence of the following atoms:

* one \(\alpha\)-horizontal, of weight \(z\);
* one \(\beta\)-horizontal, of weight \(z\);
* an elevated block, of generating function

\[
                              U(z)=z^2M(z).                         \tag{3.1}
\]

The Catalan--Motzkin bijection gives

\[
 M(z)=C(z)^2,\qquad
 U(z)=z^2C(z)^2=z(C(z)-1).                           \tag{3.2}
\]

The three ground-sequence generating functions needed below are

\[
\begin{aligned}
 R(z)&=\frac1{1-U(z)}
      =\frac{C(z)^2}{2C(z)-1},
       &&\text{no ground horizontal of either colour},\\
 L(z)&=\frac1{1-z-U(z)}=C(z),
       &&\text{one specified colour forbidden},\\
 M(z)&=\frac1{1-2z-U(z)}=C(z)^2,
       &&\text{no colour forbidden}.
                                                                  \tag{3.3}
\end{aligned}
\]

The identities use \(C=1+zC^2\), which gives
\(1-zC=1/C\) and \(1-z(C+1)=1/C^2\).

### Theorem 3.1 (exact first-class matrix)

The matrix \(M^{(s)}\) is given by (0.6).

#### Proof

By Lemma 2.2, \(M^{(s)}_{jk}\) counts length-\(n=s-1\) ground-atom
sequences whose first ground \(\alpha\) occurs at time \(j\), or never
when \(j=s\), and whose first ground \(\beta\) occurs at time \(k\), or
never when \(k=s\).

Suppose \(j<k<s\). Before time \(j\), both colours are forbidden, giving
\(R_{j-1}\). At time \(j\) there is one \(\alpha\)-atom. Between times
\(j\) and \(k\), only \(\beta\) is forbidden, giving
\(C_{k-j-1}\). At time \(k\) there is one \(\beta\)-atom. The remaining
length \(n-k\) is arbitrary, giving

\[
 [z^{n-k}]C(z)^2=C_{n-k+1}=C_{s-k}.                  \tag{3.4}
\]

This proves the second line of (0.6) for \(j<k\). Exchanging the colours
proves symmetry and the case \(k<j\).

The first occurrences cannot coincide at a finite time, because one
horizontal atom has only one colour. Hence \(M^{(s)}_{jj}=0\) for
\(j<s\).

If \(j<k=s\), there is no ground \(\beta\)-atom. The prefix before the
first \(\alpha\) contributes \(R_{j-1}\), and the remaining length
\(n-j=s-j-1\) permits only \(\alpha\)-atoms and elevated blocks, giving
\(C_{s-j-1}\). This proves the third and fourth lines. If \(j=k=s\),
both colours are absent, giving \(R_{s-1}\). \(\square\)

As a check forced by the partition,

\[
 \sum_{k=1}^sM^{(s)}_{jk}
   =|\mathcal F_{s,j}|=C_{j-1}C_{s-j}.                \tag{3.5}
\]

No floor or ceiling is hidden in (0.6); every quota is an exact product
of Catalan or \(R\)-numbers.

### Corollary 3.2 (physical first targets)

In a row \(P\), the first target of \(G_{\omega_s}\) is

\[
 b_1^{G_{\omega_s}}(P)
   =\omega_s\bigl(2\,\operatorname {fr}(\omega_sP)\bigr),         \tag{3.6}
\]

where \(\operatorname {fr}\) denotes first-return semilength. Therefore
(0.7) gives the target map, and \(M^{(s)}_{jk}\) is exactly the quota in
source fibre \(j\) at physical target \(\lambda_s(k)\).

#### Proof

The canonical factor inserts the first-return coordinate \(2k\).
For \(k<s\), \(\omega_s\) sends \(2k\) to \(2k+1\); it fixes \(2s\).
Equation (1.2) completes the full row. \(\square\)

Summing each column of (0.6) makes the physical collision explicit:

\[
\begin{aligned}
 h_{G_{\omega_s}}(2k+1)&=C_{k-1}C_{s-k},
                                      &&1\le k<s,\\
 h_{G_{\omega_s}}(2s)&=C_{s-1},\\
 h_{G_{\omega_s}}(x)&=0
                                      &&\text{otherwise}.
                                                               \tag{3.7}
\end{aligned}
\]

Thus the raw histogram is only the coordinate permutation
\(\omega_{s*}h_{F_s}\); all new dispersion lies in the retained source
first-return axis.

## 4. The sharp maximum

The coefficient \(R_n\) also counts sequences of primitive Dyck words,
each of semilength at least two. Indeed the generating function for one
non-singleton primitive component is

\[
                              z(C(z)-1)=z^2C(z)^2=U(z),             \tag{4.1}
\]

so a sequence of them has generating function \(R(z)=1/(1-U(z))\).

### Theorem 4.1 (full-swap maximum)

For every \(s\ge3\), all entries in (0.6) are at most \(R_{s-1}\), and
the \((s,s)\)-entry equals \(R_{s-1}\).

#### Proof

Consider first \(j<k<s\). Put

\[
 a=j-1,\qquad b=k-j-1,\qquad c=s-k.                   \tag{4.2}
\]

Then \(a+b+c=s-2\) and \(c\ge1\). An object counted by
\(R_aC_bC_c\) consists of

* a sequence \(A\) of non-singleton primitive Dyck components;
* arbitrary Dyck words \(B\) and \(D\) of sizes \(b,c\).

Map it to

\[
                              A\cdot1(BD)0.                         \tag{4.3}
\]

The last component has semilength \(b+c+1\ge2\), so (4.3) is counted by
\(R_{s-1}\). The last primitive component and the known split after
\(2b\) symbols recover \(A,B,D\), so the map is injective. Thus every
strictly interior off-diagonal entry is at most \(R_{s-1}\).

For a boundary entry \(R_aC_b\), where \(a+b=s-2\), append the primitive
component \(1B0\) when \(b\ge1\). If \(b=0\), then \(a=s-2\). At \(s=3\)
the domain has size \(R_1=0\); for \(s\ge4\), wrap the nonempty
non-singleton-component word \(A\) as \(1A0\). In either case this gives
an injection into the objects counted by \(R_{s-1}\).

The remaining diagonal entries below \(s\) vanish, while
\(M^{(s)}_{ss}=R_{s-1}\). \(\square\)

### Theorem 4.2 (sharp \(H_s\)-conjugacy obstruction)

For every \(h\in H_s\), the resolved cell

\[
 \{P\in\mathcal F_{s,s}:
     b_1^{G_h}(P)=2s\}                                      \tag{4.4}
\]

has at least \(R_{s-1}\) rows. Consequently (0.9) holds.

#### Proof

In the two-coloured Motzkin model, take the \(R_{s-1}\) paths having no
ground horizontal step of either colour. They have first-return class
\(s\). An element \(h\in H_s\) swaps the two horizontal colours at some
chosen time positions and leaves every up/down step unchanged. Therefore
these paths still have no ground horizontal after applying \(h\), so
\(hP\) also has first-return class \(s\).

Every element of \(H_s\) fixes coordinate \(2s\). The canonical first
target of \(hP\) is \(2s\), and conjugating it by \(h\) leaves it \(2s\).
This proves the lower bound. The full swap attains it by Theorem 4.1.
\(\square\)

Thus the no-ground-horizontal Motzkin skeleton is the complete invariant
obstruction for this conjugacy family.

### Corollary 4.3 (floor/ceiling obstruction inside \(H_s\))

For \(s\ge5\), no \(H_s\)-conjugate can distribute the top fibre
\(\mathcal F_{s,s}\), of size \(C_{s-1}\), with floor/ceiling quotas
among its \(s\) possible first-return target classes.

#### Proof

The common cell in Theorem 4.2 has size at least \(R_{s-1}\). Wrapping
an arbitrary Dyck word of semilength \(s-2\) in one primitive component
gives

\[
                              R_{s-1}\ge C_{s-2}.                    \tag{4.5}
\]

Also

\[
 C_{s-2}-\frac{C_{s-1}}s
 =C_{s-2}\frac{s^2-4s+6}{s^2}>1
 \qquad(s\ge5).                                        \tag{4.6}
\]

Hence

\[
                              R_{s-1}>
                        \left\lceil\frac{C_{s-1}}s\right\rceil.    \tag{4.7}
\]

For fixed \(h\), the possible targets are the \(s\) distinct coordinates
\(h(2),h(4),\ldots,h(2s)\). A floor/ceiling distribution among them has
maximum \(\lceil C_{s-1}/s\rceil\), contradicting (4.7). \(\square\)

This is an obstruction only to the adjacent-pair conjugation grammar.
An unrestricted exact factor can redistribute the top fibre while still
obeying the global endpoint constraint below.

## 5. Constants and cap threshold

The Catalan singular expansion is

\[
 C(z)=2-2\sqrt{1-4z}+O(1-4z).                         \tag{5.1}
\]

Substitution into (0.5) gives

\[
 R(z)=\frac43-\frac89\sqrt{1-4z}+O(1-4z).             \tag{5.2}
\]

Comparing the square-root coefficients yields

\[
                              R_n\sim\frac49C_n.        \tag{5.3}
\]

Since \(C_{s-1}/C_s\to1/4\),

\[
                              \frac{R_{s-1}}{C_s}
                                  \longrightarrow\frac19.        \tag{5.4}
\]

The one-transposition construction has resolved constant \(3/16\), so
the full swap improves that asymptotic maximum by the factor
\[
                              \frac{1/9}{3/16}=\frac{16}{27}.      \tag{5.4a}
\]

The cell \((s,2s)\) attains \(R_{s-1}\), so the zero-background resolved
hard-cap condition for this factor is exactly (0.10), not merely
sufficient.

At the natural Catalan scale

\[
                              s=\min\{t:C_t\ge p\},                  \tag{5.5}
\]

one has \(R_{s-1}\le C_{s-1}<p\). Thus the zero-background
first-return-resolved hard-cap gate is solved unconditionally at that
scale. This does not imply that an ambient parent carrier retains the
first-return label as a physical separator.

## 6. The raw endpoint obstruction remains

Let \(H\) be any exact anchored factor. In a row \(P\), let \(a(P)\) be
the deletion time of coordinate \(1\), and \(b(P)\) the insertion time
of coordinate \(2s\). Every Dyck root contains \(1\) and omits \(2s\).
The row contains both coordinates in

\[
                              (a(P)-b(P))_+                         \tag{6.1}
\]

\(X\)-states and

\[
                              (a(P)-b(P)+1)_+                       \tag{6.2}
\]

\(Y\)-states. Exact ownership gives

\[
\begin{aligned}
 \sum_P(a(P)-b(P))_+
   &=\binom{2s-2}{s-2}=(s-1)C_{s-1},\\
 \#\{P:b(P)\le a(P)\}
   &=\binom{2s-2}{s-1}-\binom{2s-2}{s-2}
     =C_{s-1}.                                           \tag{6.3}
\end{aligned}
\]

Every one of the \(C_{s-1}\) contributing rows must attain the maximum
\(s-1\). Hence it has \(b(P)=1,a(P)=s\), and

\[
                              h_H(2s)=C_{s-1}.                       \tag{6.4}
\]

Applying the same pair count to \(\{1,x\}\) shows
\(h_H(x)\le C_{s-1}\) for every \(x\ne1\), while \(h_H(1)=0\).
Therefore every exact factor has

\[
                              \max_xh_H(x)=C_{s-1}.                  \tag{6.5}
\]

In particular, the entries \(M^{(s)}_{j,s}\) in (0.6) collide after
forgetting \(j\):

\[
                              \sum_{j=1}^sM^{(s)}_{j,s}=C_{s-1}.    \tag{6.6}
\]

The full swap redistributes this forced endpoint load among source
first-return classes; it cannot reduce the raw physical load.

There is a stronger recursive consequence which scalar quotas do not
capture.

### Theorem 6.1 (forced lower-rank core factor)

Let

\[
 \mathcal S_H=\{P\in\mathcal D_s:b_1^H(P)=2s\},\qquad
 r=s-1,\qquad I=\{2,3,\ldots,2s-1\}.                   \tag{6.7}
\]

For every exact factor \(H\), \(|\mathcal S_H|=C_r\). The rows in
\(\mathcal S_H\), after stripping the pair \(\{1,2s\}\) from every state
which contains it and then complementing inside \(I\), form an exact
rank-\(r\) complement-path factor with port set

\[
 \boxed{
 \mathcal Q_H=
 \{\,I\setminus(P\setminus\{1\}):P\in\mathcal S_H\,\}.}            \tag{6.8}
\]

#### Proof

The endpoint saturation proof shows that a row belongs to
\(\mathcal S_H\) exactly when it inserts \(2s\) on transition one and
deletes \(1\) on transition \(s\). Such a row contains
\(\{1,2s\}\) in every \(Y_t\), \(0\le t<s\), and in every internal
\(X_t\), \(1\le t<s\).

The \(C_r\) special rows therefore contain \(sC_r\) such \(Y\)-states
and \(rC_r\) such \(X\)-states. These are exactly the complete ledger
counts

\[
 sC_r=\binom{2s-2}{s-1},\qquad
 rC_r=\binom{2s-2}{s-2}.                              \tag{6.9}
\]

Hence the special rows exhaust all \(Y\)-states and all \(X\)-states
containing the endpoint pair.

For \(P\in\mathcal S_H\), put \(E_P=P\setminus\{1\}\subset I\).
Stripping the endpoint pair gives

\[
 E_P=U_0\supset L_1\subset U_1\supset\cdots
       \supset L_r\subset U_r=I\setminus E_P,           \tag{6.10}
\]

where the \(U\)'s are \(r\)-sets and the \(L\)'s are
\((r-1)\)-sets. By (6.9), across all special rows the \(U\)'s exhaust
\(\binom Ir\) once and the \(L\)'s exhaust \(\binom I{r-1}\) once.

Complement every state in \(I\). This turns (6.10) into paths on the
standard middle shores \(\binom Ir,\binom I{r+1}\), with initial port
\(I\setminus E_P\) and terminal complement \(E_P\). All states are
owned exactly once. This is the asserted exact factor. \(\square\)

### Corollary 6.2 (root-refined target obstruction)

If a prescribed set \(\mathcal S_0\subseteq\mathcal D_s\) is to be
exactly the set of roots inserting \(2s\) first in some completed factor,
then

\[
 |\mathcal S_0|=C_{s-1}                                         \tag{6.11}
\]

and

\[
 \{\,I\setminus(P\setminus\{1\}):P\in\mathcal S_0\,\}             \tag{6.12}
\]

must itself be the port set of an exact rank-\((s-1)\) factor.
In particular, the facet family

\[
                              \{P\setminus\{1\}:P\in\mathcal S_0\} \tag{6.13}
\]

must be complement-free inside \(I\).

#### Proof

The first two assertions are Theorem 6.1. If both \(E\) and
\(I\setminus E\) occurred in (6.13), then the port set (6.12) would
contain a complementary pair \(Q,I\setminus Q\). In any anchored
complement factor, \(I\setminus Q\) occurs terminally in the row rooted
at \(Q\) and initially in its own row, contradicting exact ownership.
\(\square\)

This is a recursive palette-and-monodromy obstruction invisible to the
unrefined counts
\(\bigl(|\mathcal S_0\cap\mathcal F_{s,j}|\bigr)_{j=1}^s\).
It is necessary, not sufficient: a lower-rank factor with port set
(6.12) need not lift together with all remaining rank-\(s\) rows.

## 7. Exact scope and next gate

Proved:

1. \(G_{\omega_s}\) is one literal exact anchored factor.
2. Its source-fibre/physical-target quotas are exactly (0.6)--(0.7).
3. Its largest resolved quota is exactly \(R_{s-1}\).
4. No coordinate-conjugate factor from \(H_s\) has a smaller largest
   resolved quota.
5. \(R_{s-1}/C_s\to1/9\).
6. The raw physical maximum remains exactly \(C_{s-1}\) in every exact
   factor.
7. The roots assigned to target \(2s\) induce the exact lower-rank port
   factor in Theorem 6.1.

Not proved:

* that \(R_{s-1}\) is optimal among arbitrary exact factors;
* floor/ceiling equidistribution when \(p<R_{s-1}\);
* sufficiency of the recursive port condition (6.12);
* preservation of a fibre label after an ambient carrier merges physical
  cells;
* favourable two-sided or multidepth drift of the complete conjugated
  trajectories.

With ambient background \(\beta_{j,k}\), zero overload requires the
cellwise inequalities

\[
                              \beta_{j,k}+M^{(s)}_{jk}\le p.          \tag{7.1}
\]

The scalar threshold (0.10) applies only at zero background or when the
carrier keeps the \((j,k)\)-cells physically separated.

The conjugacy lane is now exhausted sharply. The residual objects are
the \(R_{s-1}\) two-coloured Motzkin paths with no ground horizontal.
They consist entirely of elevated blocks. Any further recursive first
matching must act inside those elevated blocks and then prove the
aggregate \(Y\)-palette and endpoint monodromy anew; no choice of the
flaw-preserving swaps in \(H_s\) can do it.
