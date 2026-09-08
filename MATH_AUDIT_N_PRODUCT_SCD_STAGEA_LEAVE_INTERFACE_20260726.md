# Product-SCD tails after arbitrary Stage A: exact leave interface and floor-buffer stability

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

The product-SCD outer-tail word is completely independent of the middle
factor.  It can be appended after any switching, conjugation, exact
completion, or deletion operation, and no seam, owner, chronology, or
MSW hypothesis is needed.  Its exact odd-dimensional charge is

\[
                    2L_m(m-H-1),                              \tag{0.1}
\]

where

\[
 L_m(r)=2\sum_{a=0}^{\lfloor m/2\rfloor}
 A_m(a)w_m(a)C_m(r-a).                                        \tag{0.2}
\]

The factor (2) in (0.2) belongs to the even product word, and the
factor (2) in (0.1) is the trimmed one-coordinate lift.  Uniformly for
all (0\le H\le m-1),

\[
 \frac{2L_m(m-H-1)}{\binom{2m+1}{m}}
 \le C\exp\!\left(-\frac{H^2}{8m}\right),                     \tag{0.3}
\]

for an absolute constant (C).  Thus (H/\sqrt m\to\infty) is the only
asymptotic hypothesis on the tail itself.

The exact missing hypothesis is central, not external: after Stage A one
must still cover all targets in ranks

\[
                         m-H,\ldots,m+H+1                      \tag{0.4}
\]

at total additional cost (o(W)), where

\[
 n=2m+1,\qquad W=\binom nm,\qquad B=W/n=\operatorname {Cat}_m. \tag{0.5}
\]

An arbitrary exact factor does not supply this.  The certified canonical
MSW example already has

\[
                 M_1(F_m^{\rm MSW})\ge(1/32-o(1))W.            \tag{0.6}
\]

Nor does a leave described merely as (o(W)) rows: the entire exact
factor has only (B=W/n=o(W)) rows.

There is, however, a uniform positive theorem.  Let (F) be any exact
factor with

\[
 J_H(F):=\sum_{q=1}^H\frac{O_q(F)}{c_q}=o(W),                  \tag{0.7}
\]

and delete any (R) complete cyclic rows.  The resulting partial factor
has at most

\[
 \boxed{
 2J_H(F)+2nR\bigl(1+S_H\bigr),
 \qquad S_H:=\sum_{q=1}^H\frac1{c_q}=O(\sqrt m),}              \tag{0.8}
\]

missing lower and upper central targets in total.  Consequently

\[
                         R=o(B/\sqrt m)                         \tag{0.9}
\]

is a uniform row-cardinality sufficient condition, independent of how
slowly or quickly $H/\sqrt m\to\infty$.  In middle-occurrence units
$\Lambda=nR$, condition (0.9) is

\[
                         \Lambda=o(W/\sqrt m).                  \tag{0.10}
\]

Together with (H=o(m)), which is needed only for the standard central
row collar, (0.3), (0.7), and (0.9) give one literal word of length
(W+o(W)).  This theorem applies to every Stage-A exact factor satisfying
(0.7); it is not MSW-specific.

## 1. The seam-free black-box interface

For a set-valued word (U=(U_1,\ldots,U_s)), write

\[
 \operatorname {Cov}(U)=
 \left\{\bigcup_{i=a}^bU_i:1\le a\le b\le s\right\}.          \tag{1.1}
\]

### Lemma 1.1 (concatenation is monotone)

For arbitrary literal words (U,V),

\[
             \operatorname {Cov}(U)\cup\operatorname {Cov}(V)
                    \subseteq\operatorname {Cov}(U\Vert V).   \tag{1.2}
\]

#### Proof

Every interval internal to either block remains a contiguous interval
after concatenation.  Cross-seam intervals may create extra targets but
cannot destroy an old witness.  \(\square\)

Let

\[
 \mathcal B_{m,H}=
 \bigcup_{j=m-H}^{m+H+1}\binom{[n]}j                         \tag{1.3}
\]

be the central band.  The audited product-SCD construction gives a word
(T_{m,H}) with

\[
 |T_{m,H}|=2L_m(m-H-1)                                       \tag{1.4}
\]

covering every nonempty target outside (1.3).  The exact definitions in
(0.2) are

\[
 A_m(a)=\binom ma-\binom m{a-1},                              \tag{1.5}
\]

\[
 w_m(a)=
 \begin{cases}m,&a=0,\\m-2a+1,&a>0,\end{cases}               \tag{1.6}
\]

and

\[
 C_m(t)=
 \begin{cases}
 0,&t<0,\\
 \displaystyle\binom m{\min(t,\lfloor m/2\rfloor)},&t\ge0.
 \end{cases}                                                  \tag{1.7}
\]

The exact construction and the two distinct factors in (0.1)--(0.2) are
proved in
`MATH_AUDIT_N_PRODUCT_SCD_TWO_TAIL_INTERFACE_20260726.md`.  The all-(H)
bound (0.3) is proved in
`MATH_ATTACK_N_PRODUCT_SCD_TAIL_UNIFORM_ASYMPTOTIC_20260726.md`.

### Theorem 1.2 (uniform black-box Stage-A theorem)

Let (A_{m,H}) be any literal word on ([n]), without any factor or
owner assumption.  Suppose that its uncovered targets inside
\(\mathcal B_{m,H}\) form a family 
(\mathcal E_{m,H}\).  Then a universal literal word exists with length

\[
 \boxed{
 |A_{m,H}|+|\mathcal E_{m,H}|+2L_m(m-H-1).}                   \tag{1.8}
\]

In particular, if

\[
 |A_{m,H}|\le W+o(W),\qquad
 |\mathcal E_{m,H}|=o(W),\qquad
 H/\sqrt m\longrightarrow\infty,                              \tag{1.9}
\]

then 

\[
                            \nu(2m+1)\le W+o(W).                \tag{1.10}
\]

#### Proof

Concatenate (A_{m,H}), one literal set-letter equal to each member of
\(\mathcal E_{m,H}\), and (T_{m,H}).  The first two blocks cover the
central band and the last covers its complement.  Lemma 1.1 preserves all
internal witnesses.  Equation (0.3) proves the asymptotic assertion.
\(\square\)

Thus a leave which is already defined to be the family of uncovered
central **targets** needs only cardinality (o(W)).  A leave defined in
rows, owners, components, or deleted occurrences must first be converted
to this target ledger.

## 2. Exact central compiler for an arbitrary row family

For a cyclic order 
\(\pi\) of ([n]), let (I_\pi(j,s)) be its cyclic interval of length
(s) beginning at (j\).  Define

\[
 E_j=I_\pi(j,m-H),\qquad j\in\mathbb Z/n\mathbb Z.             \tag{2.1}
\]

The row block is

\[
 \mathsf R_H(\pi)=
 E_0,E_1,\ldots,E_{n-1},E_0,E_1,\ldots,E_{2H}.                 \tag{2.2}
\]

It has (n+2H+1) entries.  For (0\le j<n) and
(1\le t\le2H+2), the relevant interval stays inside (2.2), and

\[
 \bigcup_{u=0}^{t-1}E_{j+u}
             =I_\pi(j,m-H+t-1).                                \tag{2.3}
\]

Let (P) be any family of (K) cyclic rows.  For (0\le q\le H), put

\[
 \mu_q^P(S)=
 \#\{(\pi,j):\pi\in P, I_\pi(j,m-q)=S\},                    \tag{2.4}
\]

and let

\[
 M_q(P)=
 \#\{S\in\tbinom{[n]}{m-q}:\mu_q^P(S)=0\}.                  \tag{2.5}
\]

### Lemma 2.1 (partial-row central ledger)

Concatenating the blocks (2.2) over (P) and then appending its missing
central targets gives a word of length at most

\[
 \boxed{
 K(n+2H+1)+2\sum_{q=0}^HM_q(P).}                              \tag{2.6}
\]

covering every target in 
\(\mathcal B_{m,H}\).

#### Proof

For the lower rank (m-q), use (2.3) with (t=H-q+1).  For the upper
rank (m+1+q), use (t=H+q+2).  Moreover

\[
 [n]\setminus I_\pi(j,m-q)
       =I_\pi(j+m-q,m+1+q),                                   \tag{2.7}
\]

so complementation bijects the lower and upper support sets of every row
family (P).  The two hole counts are therefore both (M_q(P)).  Append
each missing target as one literal letter.  Any accidental cross-block
witness only decreases the required number of repairs.  \(\square\)

If (F) is an exact middle wreath factor, then

\[
 |F|=B,\qquad \mu_0^F\equiv1,\qquad M_0(F)=0.                  \tag{2.8}
\]

Consequently Lemma 2.1 and the tail give the familiar finite bound

\[
 \nu(2m+1)\le
 W+\frac{2H+1}{n}W
 +2\sum_{q=1}^HM_q(F)
 +2L_m(m-H-1).                                                 \tag{2.9}
\]

This holds for every exact factor, before or after arbitrary legal
modification.  What varies with the factor is the central hole term.

## 3. Floor-buffer stability under an arbitrary deletion

For (q\ge1), set

\[
 N_q=\binom n{m-q},\qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor.                   \tag{3.1}
\]

A balanced quota (b_q\) takes values in
\(\{c_q,c_q+1\}\) and has total mass (W\).  For an exact factor (F),
let

\[
 O_q(F)=\min_{b_q}
       \sum_S\bigl(\mu_q^F(S)-b_q(S)\bigr)_+.                 \tag{3.2}
\]

Because both histograms have total mass (W), a minimizing quota also
satisfies

\[
 \sum_S\bigl(b_q(S)-\mu_q^F(S)\bigr)_+=O_q(F).                \tag{3.3}
\]

The next lemma is the decisive deletion estimate.

### Lemma 3.1 (floor-buffer deletion inequality)

Let 
\(\mu\) be any nonnegative integral load vector of total mass (W), let
(b\in\{c,c+1\}^{\mathcal X}\) have total mass (W), and let
\(0\le\delta\le\mu\) be an arbitrary deleted occurrence vector.  Put
\(\mu'=\mu-\delta\).  Then

\[
 \boxed{
 c\,|\{S:\mu'(S)=0\}|
 \le
 \sum_S(b(S)-\mu(S))_+ +\|\delta\|_1.}                       \tag{3.4}
\]

#### Proof

If 
\(\mu'(S)=0\), then 
\(\mu(S)=\delta(S)\), and

\[
 c\le b(S)
 \le (b(S)-\mu(S))_+ +\mu(S)
 =  (b(S)-\mu(S))_+ +\delta(S).                               \tag{3.5}
\]

Sum (3.5) over the holes of 
\(\mu'\), enlarge the first sum to all (S), and bound the second by
\(\|\delta\|_1\).  \(\square\)

This lemma does not assume that the remaining occurrences themselves form
an exact factor.  It is precisely the floor multiplicity, not ownership
synchronization, that buffers deletions.

### Lemma 3.2 (uniform reciprocal-floor sum)

For every (1\le H\le m),

\[
 \boxed{
 S_H:=\sum_{q=1}^H\frac1{c_q}=O(\sqrt m),}                     \tag{3.6}
\]

with an absolute implied constant.

#### Proof

For every real (x\ge1\),

\[
                         \frac1{\lfloor x\rfloor}\le\frac2x. \tag{3.7}
\]

Indeed this is immediate on (1\le x<2\), and
\(\lfloor x\rfloor\ge x/2\) for (x\ge2\).  Hence

\[
 \frac1{c_q}\le\frac{2N_q}{W}.                                \tag{3.8}
\]

Successive binomial ratios give

\[
 \frac{N_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+2+i}.                          \tag{3.9}
\]

Since

\[
 \log\frac{m-i}{m+2+i}
 =\log\left(1-\frac{2i+2}{m+2+i}\right)
 \le-\frac{2i+2}{m+2+i}
 \le-\frac{2i+2}{2m+1},                                      \tag{3.10}
\]

we obtain

\[
 \frac{N_q}{W}\le
 \exp\!\left(-\frac{q(q+1)}{2m+1}\right).                    \tag{3.11}
\]

Equations (3.8)--(3.11) and comparison with a Gaussian integral yield

\[
 S_H\le2\sum_{q\ge1}
 e^{-q(q+1)/(2m+1)}=O(\sqrt m).                                \tag{3.12}
\]

\(\square\)

## 4. Exact theorem for row replacement and row deletion

Let (F) be an arbitrary exact factor, and delete an arbitrary set
\(\mathcal D\subseteq F\) of (R) complete cyclic rows.  Put

\[
                         P=F\setminus\mathcal D.                \tag{4.1}
\]

At every depth (q), the deleted row histogram has mass exactly (nR).
Apply Lemma 3.1 to a minimizing quota for (F).  For (q\ge1),

\[
 \boxed{
 M_q(P)\le\frac{O_q(F)+nR}{c_q}.}                              \tag{4.2}
\]

At (q=0), exactness gives the sharper identity

\[
                         M_0(P)=nR.                             \tag{4.3}
\]

Define (J_H(F)) as in (0.7).  Summing (4.2)--(4.3) proves

\[
 \boxed{
 \sum_{q=0}^HM_q(P)
 \le J_H(F)+nR(1+S_H).}                                       \tag{4.4}
\]

By complement symmetry, twice this number repairs both sides of the
central band.  Combining Lemma 2.1 with the exact tail gives the finite
interface theorem.

### Theorem 4.1 (uniform arbitrary-factor deletion interface)

For every exact middle factor (F), every set of (R) deleted complete
rows, and every (0\le H\le m-1),

\[
\boxed{
\begin{aligned}
 \nu(2m+1)\le{}&
 (B-R)(n+2H+1)\\
 &+2J_H(F)+2nR(1+S_H)\\
 &+2L_m(m-H-1).
\end{aligned}}                                                 \tag{4.5}
\]

Every word and every repair in (4.5) is literal and integral.

Using Lemma 3.2 and discarding the favorable saving from the (R)
omitted row blocks gives the simpler uniform finite inequality

\[
\boxed{
 \nu(2m+1)\le
 W+\frac{2H+1}{n}W
 +2J_H(F)+C_0nR\sqrt m
 +2L_m(m-H-1),}                                               \tag{4.5a}
\]

for one absolute constant (C_0).  Thus (4.5) is the exact
retained-row ledger, while (4.5a) is the convenient factor-independent
asymptotic interface.

Consequently, for arbitrary sequences (F_m,H_m,R_m\), if

\[
 \frac{H_m}{\sqrt m}\longrightarrow\infty,\qquad
 H_m=o(m),\qquad
 J_{H_m}(F_m)=o(W),\qquad
 R_m=o(B/\sqrt m),                                             \tag{4.6}
\]

then

\[
                         \nu(2m+1)\le W+o(W).                   \tag{4.7}
\]

#### Proof

Only the asymptotic conclusion remains to check.  The retained row blocks
have length at most

\[
 B(n+2H+1)=W+\frac{2H+1}{n}W=W+o(W).                           \tag{4.8}
\]

Equations (3.6), (4.4), and (W=nB\) give

\[
 nR(1+S_H)=O(nR\sqrt m)=o(W).                                  \tag{4.9}
\]

The tail is (o(W)) by (0.3).  Substitute in (4.5).  \(\square\)

The same rate controls modifications which preserve exactness.  If
(F'\) is obtained from (F) by at most (R) row replacements and is
again exact, then

\[
 \|\mu_q^{F'}-\mu_q^F\|_1\le2nR,
 \qquad O_q(F')\le O_q(F)+nR.                                  \tag{4.10}
\]

Therefore

\[
                         J_H(F')\le J_H(F)+nRS_H.               \tag{4.11}
\]

Thus (4.6) remains sufficient after arbitrary choices of the replacement
rows.  No relation to the product SCD is involved.

More generally, if a leave deletes arbitrary occurrence vectors
\(\delta_q\) rather than whole rows, Lemma 3.1 shows that the exact
size-only sufficient ledger is

\[
 \boxed{
 \sum_{q=1}^H\frac{\|\delta_q\|_1}{c_q}=o(W),}                 \tag{4.12}
\]

together with $J_H(F)=o(W)$, the rank-$m$ leave $o(W)$, and the
existence of a Stage-A word realizing the retained occurrences in length
(W+o(W)).  The logically minimal hypothesis is still the actual target
condition 
\(|\mathcal E_{m,H}|=o(W)\) in Theorem 1.2; (4.12) is a convenient
floor-buffer certificate for it.

## 5. Exact counterexamples to overbroad interfaces

### 5.1 Exactness alone is insufficient

The theorem
`MATH_THEOREM_MSW_23_FIXED_HOLE_FLOOR_20260725.md` proves for the canonical
MSW exact factor, and indeed for every corner of its complete fixed
\((2\ 3)\)-component cube,

\[
 M_1\ge(m-3)\operatorname {Cat}_{m-2}-\frac{2W}{m+2}
       =(1/32-o(1))W.                                          \tag{5.1}
\]

Thus the implication

\[
 \text{exact middle factor}
 \quad\Longrightarrow\quad
 \sum_{q\le H}M_q=o(W)                                        \tag{5.2}
\]

is false even with no leave at all.  Equation (5.1) does not rule out a
different non-rowwise compiler; it decisively rules out using exactness as
the missing central repair hypothesis.

### 5.2 An (o(W)) row leave is vacuous

Every exact factor has

\[
                         B=W/(2m+1)=o(W)                        \tag{5.3}
\]

complete rows.  Hence even deleting all rows is an (o(W))-sized leave
when the unit is “rows.”  It leaves $W$ rank-$m$ targets uncovered.
The correct row scale is relative to (B), and the uniform cardinal
certificate supplied by Theorem 4.1 is (o(B/\sqrt m)).

### 5.3 An (o(W)) owner or occurrence leave needs a profile theorem

For $R$ deleted rows, the rank-$m$ owner leave is

\[
                         \Lambda=nR.                            \tag{5.4}
\]

Although 
\(\Lambda=o(W)\) repairs the middle layer itself, it does not by itself
bound simultaneous losses at the other central depths.  The unconditional
floor-buffer theorem asks for

\[
                         \Lambda\sqrt m=o(W),                   \tag{5.5}
\]

or, more sharply, the actual weighted deletion ledger (4.12) or target
ledger (1.9).  No necessity of (5.5) is claimed: structured leaves can be
larger if their actual depth profiles remain covered.

## 6. Precise implication scope

The following statements are proved.

1. The product-SCD word covers every rank outside (0.4) with exact charge
   (0.1), independently of every Stage-A choice.
2. Concatenation requires no matching endpoints, no separator, and no
   common owner.  Extra crossing intervals are harmless.
3. Any Stage-A word of length (W+o(W)) with (o(W)) actual central
   target holes composes immediately when (H/\sqrt m\to\infty).
4. For an arbitrary exact factor with weighted overload (J_H=o(W)),
   deleting any (o(B/\sqrt m)) complete rows preserves an (o(W))
   central repair ledger uniformly through every (H\le m).
5. If the standard cyclic-row compiler is used, (H=o(m)) is separately
   required for its collar cost.  It is not a product-SCD tail hypothesis.

The following stronger statements are not proved and must not be used.

1. Arbitrary exactness does not imply a small central repair ledger;
   (5.1) is an exact counterexample.
2. A leave of (o(W)) rows, owners, components, or unweighted occurrences
   is not interchangeable with (o(W)) uncovered central targets.
3. The sufficient row rate (o(B/\sqrt m)) is not asserted necessary.
   A larger structured leave is allowed whenever (1.9) or (4.12) is
   verified directly.
4. The product-SCD tail repairs no hole inside (0.4) and supplies no MWB,
   labelled synchronization, or exact-factor completion theorem.

Therefore the uniform compositional boundary is exact:

\[
\boxed{
 \begin{array}{c}
 \text{Stage-A literal length }W+o(W)
 \, +\,
 \text{central target leave }o(W)\\[1mm]
 \, +\,
 H/\sqrt m\to\infty
 \end{array}
 \quad\Longrightarrow\quad
 \nu(2m+1)\le W+o(W),}
\tag{6.1}
\]

and Theorem 4.1 is the uniform exact-factor/leave certificate that can be
inserted in place of the central-target hypothesis.
