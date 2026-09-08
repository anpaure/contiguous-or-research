# Independent audit: private one-occurrence switches do not yet close FSW

**Date:** 2026-08-06  
**Primary file:**
`MATH_THEOREM_PRIVATE_ORDER_ONE_OCCURRENCE_GENERATOR_AND_FSW_REDUCTION_20260806.md`  
**References checked:** the atomic FIFO/doublet theorem, the synchronized
fresh-chain normal form, the raw composite-switch theorem, and the current
joint resolvent Lyapunov note.  No computation is used.

## Verdict

The local owner-tail observation is correct: an adjacent transposition in
one private incoming FIFO order changes exactly one owner set, and the old
and new sets are Johnson adjacent.  The analogous lower deletion-order
statement is correct only for the **set-valued resources of the current
block**; it changes the ordered queue exported to the next block.

The proposed conclusion that these switches close `(FSW)` and the stopped
Johnson transfer does **not** pass.  There are three load-bearing gaps.

1. The projected switch form is a scalar Johnson Dirichlet form
   `alpha <f,L_T f>`.  The quantity to be paid is the whole-word covariance
   `<f,B_T f>`, and the resolvent identity
   `R_T L_T=B_T` is bilinear.  Rescaling the scalar switch measure does not
   turn `<f,L_T f>` into `<f,B_T f>` and does not reproduce the squared
   resolvent Bellman identity.
2. When the unique old or new occurrence is also present in the companion
   macro, the private switch changes the pair/root future coefficient and
   can change the distinguished-root validity.  The statement that every
   such term is already `(ROc)` or `(FE3)` is asserted but not injected with
   the actual coefficients.
3. The endpoint ledger is incomplete.  The terminal-fan estimates cover the
   last-two owner fan, and the marked-cluster estimates cover their stated
   rooted moments, but no occurrence-wise dynamic ledger is given for all
   lower endpoints, initial owner/marked roles, and the lower exported queue
   holonomy.

Therefore the candidate theorem is **FAIL as an FSW/JSEC closure**.  It is a
useful reduction to a possible one-occurrence switching proof, but that proof
still needs a coefficient-faithful bilinear Bellman identity plus the finite
endpoint ledger.

## 1. Exact audit of the private orders

For a fresh lower block,

\[
 S_j=C\cup\{a_{j+1},\ldots,a_d\}
       \cup\{b_1,\ldots,b_j\}.
\]

Swapping adjacent deletion labels `a_q,a_(q+1)` changes only `S_q`; before
that role both labels are present and afterward both are absent.  The two
values differ by one Johnson exchange.  All owner **sets** in the current
block are unchanged because

\[
 T_j=C\cup A\cup\{x_{j+1},\ldots,x_d\}
       \cup\{b_1,\ldots,b_j\}
\]

depends on `A` only as an unordered set.

However the final queue is

\[
                         Q_d=(a_1,\ldots,a_d).
\]

The transposition changes this ordered state.  The synchronized-chain source
explicitly warns that deletion order is owner-invisible locally but changes
the next block's input queue.  Thus a lower private switch is not a closed
chronology involution unless a queue-order holonomy/next-block switch is
included.  The candidate theorem fixes endpoint **sets**, not this endpoint
order.

For owner copy `c`,

\[
 Q_j^c=(x_{j+1}^c,\ldots,x_d^c,a_1,\ldots,a_j),
 \qquad T_j^c=S_j\dot\cup Q_j^c.
\]

Swapping `x_q^c,x_(q+1)^c` changes exactly `T_q^c`; the final queue is still
`(a_1,...,a_d)`.  The private banks of distinct copies are disjoint in the
atomic template.  Hence this owner-tail switch is a genuine one-occurrence
set-valued involution and preserves the terminal queue.  This part passes.

The slot and port data also remain fixed because these private labels are
chosen outside the port pair and the other macro half.  For a pointed marked
owner the coordinate mark is fixed, but the pointed owner changes whenever
its underlying owner role changes; it must therefore be handled by the
anchored, not automatically the unmarked, operator.

## 2. What the orbit double count actually proves

Fix one unmarked resource rank, one owner-tail role, and one macro/track
type.  Over the complete coordinate orbit, the old/new changed pairs are
Johnson edges.  Coordinate symmetry is transitive on directed Johnson
edges, so for a suitable normalization

\[
  \sum_{(C,C')}w(C,C')
      (f(x(C))-f(x(C')))^2
       =\alpha_T\langle f,L_Tf\rangle.
\tag{2.1}
\]

This is correct.  It proves a reversible local generator and nothing more.
The constant `alpha_T` depends on the role/track normalization unless those
weights are explicitly balanced; it cannot simply be rescaled inside the
actual first-kill coefficient.

## 3. Fatal operator substitution

The current resolvent is

\[
 R_T=L_T^\dagger B_T,
\qquad R_TL_T=B_T
\tag{3.1}
\]

on the mean-zero resource layer.  Here `B_T` is the covariance of the full
FIFO side/union word, including all cross-role and cross-track terms.  From
(2.1) one obtains only `<f,L_T f>`.  Equation (3.1) yields

\[
             \langle f,R_TL_Tf\rangle
                 =\langle f,B_Tf\rangle,
\tag{3.2}
\]

not

\[
             \langle f,L_Tf\rangle
                 =\langle f,B_Tf\rangle.
\]

To use (3.2), the switching argument must produce the **bilinear** form with
`R_T` acting on the same predictable vector, or the equivalent squared
identity

\[
 \mathbb E_\tau\langle(I-\tau)f,
       R_T(I-\tau)f\rangle
       =2\alpha\langle f,B_Tf\rangle.
\tag{3.3}
\]

The global-transposition proof obtains (3.3) because every global
transposition is a self-adjoint involution commuting with `R_T`, and its
average is exactly `I-alpha L_T` on the entire resource layer.

The private construction instead evaluates a candidate-dependent
transposition only at its one changed occurrence.  Its local energy is the
point difference in (2.1).  It neither applies `(I-tau)` to the entire
resource vector nor inserts `R_T` into the local form.  Uniformity of the
projected Johnson edge does not restore the missing cross-role covariance.
No candidate-space counterterm whose drift equals (3.2) is defined.

This is not a harmless normalization omission.  A sum of one-role local
Dirichlet forms contains no cross terms between two different FIFO roles,
whereas `B_T` was defined precisely from the squared sum over the complete
side/union word.  Those cross terms are the slow-sector content for which
the resolvent was introduced.

Therefore the sentence “combining (2.1) with `R_TL_T=B_T` gives exact
pristine cancellation” is not established.

## 4. Boundary stopping is locally favorable but not yet a Bellman proof

Suppose a private-switch pair `C,C'` really differs in one host resource
`x -> y`, both candidates are live, and the next accepted edge `G` kills
`C'` but not `C`.  Every common resource misses `G`; hence `G` contains `y`
and not `x`.  At the raw occurrence level the changed set has one member,
so the unhit portion of that **particular** switch is empty.  This useful
fact passes.

It does not by itself close `(FSW)`, because `(FSW)` is the boundary term of
the coefficient-faithful resolvent symmetrization.  The proof must first
replace the global switch decomposition by the private one while preserving
the internal bilinear payment (3.2) and the true first-kill coefficient.  No
such replacement is supplied.

## 5. Composite coefficient exceptions are not audited

Let `E` undergo `x -> y` inside a composite `(Q,E,F)`.  If neither or both
of `x,y` belong to `F`, the cardinalities of `E cap F` and `E union F` are
unchanged.  Away from distinguished-root issues, equal base orbit weights
then give equal future coefficients.  This subcase passes.

If exactly one belongs to `F`, both the intersection and union exponents can
change.  For example, if `x in F` and `y notin F`, the switch loses one
intersection and gains one union element.  The coefficient contains both
the current intersection fugacity and the one-step future union factor; it
is not justified merely by saying that “one exponent” changes.

Moreover, if `x` is a distinguished member of `Q`, replacing it by `y`
while holding `F,Q` fixed can leave `Q` outside `E' cap F`; transporting
`Q` instead need not restore a valid common root.  Such switches must be
excluded and charged as rooted-overlap cases.

It is plausible that these exceptional faces reduce to `(ROc)`/`(FE3)`,
because a companion-common occurrence supplies an anchor.  But the candidate
note gives no termwise map with the actual coefficient, no multiplicity
bound, and no treatment of the distinguished-root case.  The earlier raw
switch theorem explicitly warns that coefficient equality and blocker-hit
terms alone do not prove the stopped residual.  This warning still applies.

## 6. Endpoint ledger audit

Adjacent private switches cover the genuinely interior lower/owner roles
subject to the lower queue-order qualification above.  Constantly many roles
remain on every track, but “constant” is not the same as “priced.”

The existing ledgers prove:

* `(TF1)--(TF3)` for the penultimate/terminal owner fan;
* bounded rooted overlap and first-two-hit moments for stated marked clusters
  of size two or three; and
* a separate slot ledger.

They do not presently identify, occurrence by occurrence, every lower
endpoint, initial owner role, pointed level-one/level-two role, exported
queue state, and composite distinguished-root exception with one of those
rows.  Equation (5.1) of the candidate note is only a scalar Cauchy bound.
It omits the resolvent weight and does not prove a stopped coefficient-
faithful injection.  The assertion that a constant endpoint word cannot
support a slow-sector loss is also insufficient: the resolvent contains the
inverse Johnson gap even for a one-occurrence innovation unless an explicit
switch resistance or service term pays it.

Thus item 3 of the candidate's own audit list remains open, and its
conditional conclusion cannot be upgraded to an unconditional one.

## 7. Smallest proof-safe repair

The private owner-tail switches are still promising.  A valid closure would
need one of the following equivalent additions.

1. **Private-switch Bellman identity.**  Define a candidate-space
   counterterm and prove that its internal private-switch drift is exactly
   `<f,B_T f>` with the actual composite weights, while every stopped
   boundary has the one-hit coefficient and every companion-overlap
   exception injects into `(ROc)`/`(FE3)`.
2. **Coefficient-faithful flow representation.**  Express the full
   whole-word centered collision innovation as a signed flow of private
   one-occurrence Johnson switches, with `R_T` included through the exact
   resistance identity and with total boundary multiplicity bounded by the
   existing rooted ledgers.

In either repair, lower deletion switches must be closed around the exported
queue-order holonomy, and a finite endpoint table must be written.  Until
then, `(FSW)`, `(JBEL)`, and the balanced-doublet rounding theorem remain
open.
