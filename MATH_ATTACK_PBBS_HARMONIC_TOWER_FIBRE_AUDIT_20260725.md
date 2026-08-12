# Audit of the harmonic peak-deletion tower

Date: 2026-07-25

No computation or web search is used in this note.

## 0. Verdict

For a peak-deletion tower

\[
 T_0\xrightarrow{\partial}T_1\xrightarrow{\partial}\cdots,
 \qquad r_j=|T_j|,
\]

the proposed indices are exact:

\[
 \boxed{
 F_j=\binom{r_j+r_{j+2}}{2r_{j+1}},
 \qquad
 y_j=r_j-2r_{j+1}+r_{j+2}.}
 \tag{0.1}
\]

Prescribing the final root slot to be zero retains the exact fraction

\[
 \boxed{
 q_j=rac{2r_{j+1}}{r_j+r_{j+2}}.}
 \tag{0.2}
\]

On the harmonic ranks

\[
 r_j=\frac{R}{j+1},
 \tag{0.3}
\]

one has

\[
 q_j=1-rac1{(j+2)^2},
 \qquad
 \boxed{
 \prod_{j=0}^{L-1}q_j
 =\frac{L+2}{2(L+1)}\longrightarrow\frac12.}
 \tag{0.4}
\]

This is not merely a real-variable saddle.  For every finite \(L\), there
are arbitrarily large integer \(R\) and actual ordered plane trees realizing
the harmonic ranks through level \(L+1\); the final root slot can be zero at
all those levels.  Conditional on a fixed bottom core and this rank profile,
the exact proportion of inverse towers with all these seam slots zero is the
product (0.4).

The implication scope is essential.  This proves that **Pascal fibre factors
alone do not contract through iterated pruning**.  It does not construct a
PBBS return/passage tower with harmonic ranks.  Passage admissibility is a
separate condition on every core orbit.  Consequently (0.4) neither proves
nor disproves RP_A.  It isolates the first possible positive input: a
dynamic theorem must show that adjacent-particle passage cores cannot carry
harmonic-type rank profiles at sufficient Catalan mass.

Remembering the two child returns gives no additional fibre factor.  Once a
reduced core and its passage itinerary are fixed, both children are fixed
before the parent slot vector is chosen; the admissible parent fraction is
still exactly \(q_j\).  The gap-seven family shows at two levels that the two
child traces may overlap so completely that no local \(o(1)\) capacitated
contraction results.  Any two-child gain must therefore be a global
enumeration/clustering theorem for passage cores, not a refinement of the
Pascal slot count.

## 1. Exact fibre indices

Let \(T_{j+1}\) be a nonempty Dyck tree of semilength \(r_{j+1}\).  Its
number of leaves is

\[
 k_{j+1}
 =r_{j+1}-|\partial T_{j+1}|
 =r_{j+1}-r_{j+2}.
 \tag{1.1}
\]

To reconstruct \(T_j\), first attach one mandatory new leaf at every leaf
of \(T_{j+1}\), then distribute the remaining new leaves among the
\(2r_{j+1}+1\) ordered child slots.  The free mass is therefore

\[
\begin{aligned}
 y_j
 &= (r_j-r_{j+1})-k_{j+1}\\
 &=r_j-2r_{j+1}+r_{j+2}.
\end{aligned}
 \tag{1.2}
\]

It must be nonnegative for every realizable tower.  The inverse fibre is the
weak-composition simplex of \(y_j\) into \(2r_{j+1}+1\) slots, and hence

\[
\begin{aligned}
 F_j
 &=\binom{y_j+2r_{j+1}}{2r_{j+1}}\\
 &=\binom{r_j+r_{j+2}}{2r_{j+1}}.
\end{aligned}
 \tag{1.3}
\]

The final root slot is unforced.  Prescribing it to be zero leaves a weak
composition into \(2r_{j+1}\) slots, of size

\[
 K_j(0)=\binom{y_j+2r_{j+1}-1}{2r_{j+1}-1}.
 \tag{1.4}
\]

Taking the ratio of (1.4) and (1.3) gives

\[
 \frac{K_j(0)}{F_j}
 =\frac{2r_{j+1}}{y_j+2r_{j+1}}
 =\frac{2r_{j+1}}{r_j+r_{j+2}},
\]

which is (0.2).

## 2. Harmonic telescoping

Assume (0.3) for \(0\le j\le L+1\).  Then

\[
 y_j
 =\frac{2R}{(j+1)(j+2)(j+3)}>0
 \tag{2.1}
\]

and

\[
\begin{aligned}
 q_j
 &=\frac{2/(j+2)}{1/(j+1)+1/(j+3)}\\
 &=\frac{(j+1)(j+3)}{(j+2)^2}\\
 &=\left(1-\frac1{j+2}\right)
   \left(1+\frac1{j+2}\right).
\end{aligned}
 \tag{2.2}
\]

Therefore

\[
\begin{aligned}
 \prod_{j=0}^{L-1}q_j
 &=\prod_{n=2}^{L+1}\frac{(n-1)(n+1)}{n^2}\\
 &=\left(\prod_{n=2}^{L+1}\frac{n-1}{n}\right)
   \left(\prod_{n=2}^{L+1}\frac{n+1}{n}\right)\\
 &=\frac1{L+1}\cdot\frac{L+2}{2}
 =\frac{L+2}{2(L+1)}.
\end{aligned}
 \tag{2.3}
\]

This verifies both the indices and the proposed limit.

## 3. Exact integer and tree realization

Fix \(L\).  Choose \(R\) to be any sufficiently large multiple of

\[
 \Lambda_L=\operatorname{lcm}(1,2,\ldots,L+2).
 \tag{3.1}
\]

Then all ranks in (0.3), through \(r_{L+1}\), are integers.  Put

\[
 a_j=r_j-r_{j+1}
 =\frac{R}{(j+1)(j+2)}
 \qquad(0\le j\le L).
 \tag{3.2}
\]

This is a nonincreasing positive integer sequence.  Extend it by

\[
 a_{L+1}=a_{L+2}=\cdots=a_{2L+1}=a_L,
 \qquad
 a_j=0\quad(j\ge2L+2).
 \tag{3.3}
\]

There are \(L+1\) copies in (3.3), so

\[
 \sum_{j=L+1}^{2L+1}a_j
 =(L+1)a_L
 =\frac{R}{L+2}=r_{L+1}.
 \tag{3.4}
\]

Thus, after defining

\[
 r_j=\sum_{t\ge j}a_t
 \tag{3.5}
\]

for the extended sequence, the prescribed harmonic values through level
\(L+1\) remain unchanged.

Every nonincreasing finite sequence \(a_0\ge a_1\ge\cdots\ge0\) is a
plane-tree pruning profile.  To see this explicitly, take a root and attach

\[
 a_{ell-1}-a_\ell
 \tag{3.6}
\]

ordered path branches of length exactly \(\ell\), for every \(\ell\ge1\).
Then \(a_j\) is the number of branches of length at least \(j+1\).  After
\(j\) simultaneous leaf-pruning rounds, the number of surviving edges is

\[
 \sum_{t\ge j}a_t=r_j.
\]

This constructs an actual ordered plane tree with the desired ranks.

The branches can be ordered so that one of maximum length is last.  That
branch survives every one of the first \(L+1\) pruning rounds.  Hence no
leaf branch lies after the last surviving root child at any of these
levels, and the final root slot is zero throughout the harmonic segment.

There is also a direct fibre-count realization.  Fix any bottom core
\(T_{L+1}\) having the extended tail profile.  At level \(j\), every core
with the prescribed lower profile has exactly \(F_j\) inverse trees of rank
\(r_j\), and exactly \(K_j(0)=q_jF_j\) of them have zero final slot.  Since
these counts depend only on the three ranks, successive inverse choices
multiply.  Therefore

\[
 \frac{
 \#\{T_0:\partial^{L+1}T_0=T_{L+1},
          |\partial^jT_0|=r_j,
          z_j=0\ (0\le j<L)\}}
 {
 \#\{T_0:\partial^{L+1}T_0=T_{L+1},
          |\partial^jT_0|=r_j\}}
 =\prod_{j=0}^{L-1}q_j.
 \tag{3.7}
\]

Thus the noncontraction in (0.4) is fully integral and occurs on actual
Dyck trees.

## 4. Quantifiers and implication scope

The construction proves the following precise statement:

> For every \(L\), there are arbitrarily large \(R\), an integral pruning
> profile of top rank \(R\), and a nonempty inverse-tree family such that
> imposing zero final seam slot at each of the first \(L\) levels retains
> the fraction \((L+2)/(2(L+1))\).

Taking \(R\) through multiples of \(\Lambda_L\) and then letting
\(L\to\infty\) gives a sequence with retention tending to \(1/2\).  Since
\(\log\Lambda_L=O(L\log L)\) by the elementary bound
\(\Lambda_L\le(L+2)!\), one may also choose \(L\to\infty\) while
\(L=o(\sqrt R)\), so the tower depth fits inside a fixed Gaussian return
window.  No prime-number asymptotics are needed.

What is **not** proved is that the cores \(T_j\) in this family satisfy the
PBBS predecessor-passage equations at compatible times.  The slot condition
\(z_j=0\) is necessary for a one-prior-selection passage, but it is not
sufficient: one still needs the reduced omitted-particle itinerary to
reselect the distinguished particle and then select its predecessor at the
specified endpoint time.

Consequently the harmonic family refutes only arguments of the form

\[
 \text{many pruning levels}
 \quad+\quad
 \text{one prescribed Pascal slot per level}
 \quad\Longrightarrow\quad o(1)\text{ fibre mass}.
 \tag{4.1}
\]

It does not refute a dynamic theorem asserting that passage-admissible
cores avoid this saddle or have small aggregate Catalan weight.

## 5. The two-child condition

An outer predecessor passage contains two reduced same-label returns:

1. the distinguished particle is reselected before the endpoint; and
2. the predecessor particle has a previous occurrence before its final
   selection.

For a fixed reduced root \(E\), both child intervals and their complete
ordered traces are determined by the reduced PBBS itinerary.  Choosing a
parent inverse tree changes only the slot vector.  Once the required seam
coordinate is fixed, remembering one child, both children, or their whole
ordered union retains the same number

\[
 K_j(z)=inom{y_j-z+2r_{j+1}-1}{2r_{j+1}-1}
 \tag{5.1}
\]

of parent starts.  Thus there is no second independent Pascal factor.

Nor is there a universal edge-volume gain from charging both children.
Their reduced traces can overlap.  In the exact gap-seven fibre, the two
gap-five child traces are translates inside the same short reduced cycle,
and a parent packing over that one two-child pattern has normalized load at
least \(1/18-o(1)\).  Hence no local estimate of the form

\[
 \#\{\text{parent lifts of one two-child pattern}\}
 =o(F_j)
 \tag{5.2}
\]

is valid.

The only possible two-child contraction left is dynamic and aggregate: one
must bound the Catalan/Pascal mass of reduced cores whose PBBS itinerary
realizes both adjacent returns.  Neither the fibre algebra nor outer
edge-disjointness supplies such a bound.

## 6. Exact two-child terminal-block equation

There is nevertheless a sharper exact description of what the second child
requires at the next pruning level.

Let a parent root \(E\) have semilength \(d\), let

\[
 F=\partial E\in\mathcal D_e,
 \qquad p=2e+1,
 \qquad M=2d+1,
\]

and write the recorded particle word as \(w=0F\).  Label its particles by
\(0,1,\ldots,p-1\), with particle \(0\) distinguished.  Let

\[
 q_a=1+\epsilon_a+2n_a,
 \qquad
 \epsilon_a=\mathbf1_{\{w_{a-1}\ne w_a\}},
 \tag{6.1}
\]

be the clockwise physical gap from particle \(a-1\) to particle \(a\).
At the seam, \(\epsilon_0=0\).  Normalize the initial physical omitted
coordinate of \(E\) to be zero, so the initial position of particle \(0\)
is \(-1\pmod M\).

Run the PBBS on \(0F\).  Let \(\kappa_t\) be its selected particle and

\[
 C_a(t)=\#\{0\le u<t:\kappa_u=a\}.
 \tag{6.2}
\]

For \(j\ne0\), put

\[
 Q_j=\sum_{a=1}^{j}q_a,
 \qquad
 \mathcal B(j)=\{j+1,j+2,\ldots,p-1,0\},
 \qquad b(j)=p-j.
 \tag{6.3}
\]

The physical omitted coordinate of \(E\) at time \(t\), when
\(j=\kappa_t\), is

\[
 \lambda_t(E)\equiv Q_j+C_j(t)\pmod M.
 \tag{6.4}
\]

Consequently, whenever \(t<M\),

\[
 \boxed{
 \lambda_t(E)=-1
 \quad\Longleftrightarrow\quad
 \sum_{a\in\mathcal B(j)}q_a=C_j(t)+1.}
 \tag{6.5}
\]

Indeed, the left side says \(Q_j+C_j(t)=M-1\); a second wrap is impossible
because \(C_j(t)<M\).  Since \(M-Q_j\) is the gap sum in (6.5), the two
forms are equivalent.

Now suppose \(E\) is itself a predecessor passage: its initial physical
label returns at time \(h\), and its physical predecessor label occurs at
time \(g>h\).  The return theorem gives

\[
 \kappa_h=p-1,
 \qquad
 C_{p-1}(h)=q_0=1+2n_0.
 \tag{6.6}
\]

At time \(g\), let \(j=\kappa_g\).  Equation (6.5) gives

\[
 \sum_{a\in\mathcal B(j)}n_a
 =s,
 \qquad
 s=\frac{C_j(g)+1-b(j)-sum_{a\in\mathcal B(j)}\epsilon_a}{2}.
 \tag{6.7}
\]

Thus the two children impose one seam coordinate and one terminal-block
sum.

### Lemma 6.1 (the terminal block contains a second slot)

In a genuine passage one has

\[
 \boxed{b(j)\ge2.}
 \tag{6.8}
\]

#### Proof

If \(b(j)=1\), then \(j=p-1\) and (6.5) reads

\[
 q_0=C_{p-1}(g)+1.
\]

But particle \(p-1\) is selected at time \(h<g\), so

\[
 C_{p-1}(g)\ge C_{p-1}(h)+1=q_0+1
\]

by (6.6), a contradiction.  \(\square\)

For fixed \(F,h,g\), put

\[
 z=\frac{C_{p-1}(h)-1}{2}.
\]

If the free slot mass is \(y=d-2e+|\partial F|\), then the exact number of
parent slot vectors satisfying both children is

\[
 \boxed{
 K^{(2)}=
 \binom{s-z+b-2}{b-2}
 \binom{y-s+p-b-1}{p-b-1},}
 \tag{6.9}
\]

with the usual convention that an inadmissible binomial is zero.  The first
factor distributes \(s-z\) among the other \(b-1\) terminal-block slots;
the second distributes \(y-s\) among the \(p-b\) outside slots.

For the gap-seven core over \(F=10\), one has \(p=3\), \(j=1\),
\(b=2\), and \(s=z=0\).  Formula (6.9) fixes both terminal slots and leaves
all free mass in the one outside slot, recovering the unique core
\((10)^{d-2}1100\) at every rank \(d\).

Lemma 6.1 proves that two-child dynamics does impose more than the seam
coordinate when the passage cores themselves are recursively enumerated.
It still does not give a uniform contraction: on harmonic profiles the free
mass per slot is summable, and fixing any bounded number of zero slots per
level can retain a positive limiting product.  A proof of RP_A would need a
dynamic reason that the block sizes or prescribed masses in (6.7) grow often
enough, or an aggregate bound on the cores for which they do not.
