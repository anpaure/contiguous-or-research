# Audit of the proposed `nu`-twisted seed target

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The canonical MSW seed followed by arbitrary cyclic row rephasing is
indeed ruled out by the hereditary Catalan phase-capacity obstruction.
The proposed replacement

\[
 \operatorname {OV}(F)=
 \max_{q\le p^{1/4}}\sum_S(\mu_q^F(S)-p)_+=0
\]

is not, however, the exact remaining target.

There are two corrections.

1. The sharp rephasing obstruction is the **orbitwise under-capacity**
   after subtracting the unavoidable duplicate mass `W-N_q`; raw source
   overload above `p` is stronger than necessary.
2. A seed satisfying the orbitwise capacity inequalities may still have
   no common legal phase assignment.  Capacity is a local condition on
   each phase orbit, whereas middle exactness and simultaneous
   lower-rank coverage form a coupled Latin-type system on the row
   phases.

Moreover, a twist whose dependence on an invisible Dyck filling is only
through the `p`-valued hash `nu mod p` cannot eliminate all dangerous
fibres.  Once a Catalan fibre has size greater than `p^2`, pigeonhole
forces a residual fibre of size greater than `p`.  Such a scale occurs at
`r=O(log p)`, well below `p^{1/4}`.

Thus breaking the named MSW fibre is a useful design specification, but
it neither proves `OV=0` nor preserves exact middle ownership by itself.

## 1. The exact orbit-capacity identity

Let `p=2m+1` be prime and let `sigma` be a `p`-cycle on the coordinates.
At depth `q`, let `V_q` be the target layer, `|V_q|=N_q`, and let
`O_q` denote its free `sigma`-orbits.  Every orbit has size `p`.

For an exact seed factor `F`, define

\[
 \mu_q^F(S)=\#\{C\in F:S\text{ is a depth-}q\text{ interval of }C\}
\]

and the orbit mass

\[
 \mathsf M_q^F(O)=\sum_{S\in O}\mu_q^F(S).
\]

Choose arbitrary row exponents `a_C in Z_p` and replace every row `C` by
`sigma^{a_C}C`.  This operation preserves every orbit mass
`mathsf M_q^F(O)`.  The resulting occurrences can cover at most

\[
                         \min\{\mathsf M_q^F(O),p\}
\]

members of `O`.  Consequently its number `H_q(F_a)` of uncovered
depth-`q` targets satisfies

\[
 \begin{aligned}
 H_q(F_a)
 &\ge \sum_{O\in O_q}(p-\mathsf M_q^F(O))_+\\
 &=\sum_{O\in O_q}(\mathsf M_q^F(O)-p)_+-(W-N_q).
 \end{aligned}                                      \tag{1.1}
\]

The second line is an identity: the signed sum of
`mathsf M_q^F(O)-p` is `W-N_q`.  In particular the right side is already
nonnegative; no positive-part symbol is needed in the orbitwise form.

Define the exact capacity floor

\[
 \boxed{
 \operatorname {CapDef}_q(F)
 :=\sum_{O\in O_q}(p-\mathsf M_q^F(O))_+ .}          \tag{1.2}
\]

This is the optimum that would remain even if occurrences could be
placed independently inside every orbit.  Actual row phases can only do
worse.

The source statistic

\[
 K_q(F)=\sum_{S\in V_q}(\mu_q^F(S)-p)_+
\]

gives the valid but weaker lower bound

\[
 H_q(F_a)\ge (K_q(F)-(W-N_q))_+ .                    \tag{1.3}
\]

Thus `K_q=0` is not necessary.  An orbit of mass `p+d` can cover all of
its `p` phases and spend `d` units of the unavoidable duplicate budget.
Only excess beyond the global budget forces a hole.

The smallest local model makes this literal.  For `p=3`, put four source
occurrences at one member of a three-point phase orbit.  Then `K_q=1`, so
raw `OV=0` fails.  Rephase the four rows to phases `0,1,2,0`: all three
targets are covered and the fourth occurrence is precisely the one
unavoidable duplicate (`W-N_q=1`).  Hence positive raw source overload
does not itself force any hole.

## 2. Capacity is not realization

Define the realization slack of a phase vector `a` by

\[
 \operatorname {Real}_q(F,a)
 :=H_q(F_a)-\operatorname {CapDef}_q(F)\ge0.         \tag{2.1}
\]

Even `CapDef_q(F)=0` for every relevant `q` does not imply that one can
make all the slacks small.  For each orbit separately, capacity merely
says there are enough occurrence slots.  A row exponent is shared by all
occurrences of that row and by all depths, while exact middle ownership
requires the shifted middle phases at every middle orbit to be a complete
residue system.  These are simultaneous all-different constraints.

A three-phase toy model already shows the logical gap.  Give three phase
variables `a,b,c in Z_3`.  One locally full orbit requires

\[
                         \{a,b,c\}=Z_3,
\]

and a second requires

\[
                         \{a,b,c+1\}=Z_3.
\]

Each constraint separately has exactly its three available units and is
satisfiable, so its scalar capacity defect is zero.  They cannot hold
simultaneously: under the first constraint `c+1` is one of the other two
residues and therefore duplicates `a` or `b` in the second.  The wreath
system has more structure, but no scalar capacity statistic supplies that
missing global compatibility.

Accordingly a seed-only condition cannot complete the row-power route.
One must prove both small capacity floor and a legal common realization.

## 3. A `p`-valued twist cannot remove all Catalan fibres

The following elementary lemma tests the proposed binary-value twist.

### Lemma 3.1 (finite-hash residual fibre)

Suppose a blind family `B` of `d` fillings gives the same relevant window
before twisting.  Suppose that, after twisting, the resulting window
depends on the filling only through a hash `h:B->[L]`.  Then some twisted
window has multiplicity at least `ceil(d/L)`, and the total raw overload
above phase capacity `p` among the at most `L` images is at least

\[
                         (d-Lp)_+.                   \tag{3.1}
\]

#### Proof

If the hash fibres have sizes `d_1,...,d_s`, `s<=L`, then
`sum d_i=d`.  Hence `max d_i>=ceil(d/L)`, and

\[
 \sum_i(d_i-p)_+\ge \sum_i(d_i-p)=d-sp\ge d-Lp.
\]

Taking the positive part proves the claim.  \(\square\)

For the proposed hash

\[
                         \nu(x)=\sum_i x_i2^i\pmod p,
\]

we have `L=p`.  A primitive Dyck block of semilength `r` has
`d=Cat_r` fillings.  Since

\[
 \operatorname {Cat}_r\sim \frac{4^r}{\sqrt\pi r^{3/2}},
\]

one may take, for example,

\[
 r=\left\lceil\log_2p+2\log_2\log p\right\rceil .   \tag{3.2}
\]

Then `r=O(log p)=o(p^{1/4})` and `Cat_r/p^2 -> infinity`.  Lemma 3.1
therefore leaves a fibre of size greater than `p` whenever the twisted
window sees the filling only through `nu mod p`.

This does not rule out a genuinely global word-dependent construction.
It rules out the inference

\[
 \text{`nu separates replacements while }4^r<p\text{'}
 \quad\Longrightarrow\quad
 \text{`no dangerous fibres for all }r\le p^{1/4}\text{'}.
\]

The dangerous phase-capacity range begins precisely after the injective
hash range ends.  A viable twist must retain more than a `p`-valued
summary of the filling, or alter the window by a mechanism not determined
only by that summary.

## 4. Exact middle ownership is a separate bijection

Let `D_{2m}` be the Dyck words indexing the proposed rows.  For a twisted
family `pi_x`, exact middle ownership is exactly the assertion that

\[
 \Phi_m:D_{2m}\times Z_p\longrightarrow { [p]\choose m},
 \qquad
 \Phi_m(x,j)=I_{\pi_x}(j,m),                         \tag{4.1}
\]

is a bijection.

Local separation of subtree replacements supplies no implication toward
(4.1).  In particular, changing the MSW interleaving according to a word
label can create a repeated middle set in two rows and a missing middle
set elsewhere.  The middle bijection must be proved globally, not inferred
from the injectivity of the label on one replacement family.

If a second row-power phase vector `a_x` is then applied, legality is the
separate bijection

\[
 (x,j)\longmapsto \sigma^{a_x}I_{\pi_x}(j,m).        \tag{4.2}
\]

## 5. The corrected single construction target

Within the row-power architecture, the exact target is a pair `(F,a)`,
not a seed satisfying raw `OV=0`.

For every fixed `A>0`, construct a Dyck-indexed exact seed `F=F_{A,m}`
and one exponent vector `a=a_{A,m}` such that

\[
 \boxed{
 \begin{aligned}
 &\text{the seed middle map (4.1) is bijective},\\
 &\text{the lifted middle map (4.2) is bijective},\\
 &\sum_{q\le A\sqrt m}\operatorname {CapDef}_q(F)=o_A(W),\\
 &\sum_{q\le A\sqrt m}\operatorname {Real}_q(F,a)=o_A(W).
 \end{aligned}}                                      \tag{5.1}
\]

The last two lines are equivalent to

\[
                         \sum_{q\le A\sqrt m}H_q(F_a)=o_A(W),
\]

but they separate the seed obstruction from the common-phase realization
problem.  Together with the already audited factor-blind product-SCD tail
and fixed-window diagonalization, (5.1) yields the constant-one theorem.

For canonical MSW, the third line fails by the hereditary Catalan
plateau.  A global twist can attack that line.  It must still prove the
first, second, and fourth lines; neither the hash nor the disappearance of
one named fibre supplies them automatically.

## 6. Status

The useful conclusion of the proposed redirect is therefore narrower but
still concrete:

* canonical MSW plus cyclic row powers is closed;
* a new globally word-sensitive seed remains open;
* `nu mod p` by itself has insufficient range beyond
  `r approximately log_2 p`;
* the correct seed statistic is baseline-corrected orbit capacity, not
  raw `OV=0`;
* the common legal phase realization remains an independent gate.

This is one sharply formulated construction program, but not one solved
seed criterion.
