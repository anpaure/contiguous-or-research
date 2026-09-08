# Independent audit: vanishing-singleton socket insurance

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_VANISHING_SINGLETON_SOCKET_INSURANCE_AND_FULL_SMALL_BANK_LIFT_20260805.md`  
**Method:** independent pure-mathematical replay; no computation, search, or
solver  
**Verdict:** **GO after one exact named-overlay correction.**  Sacrificing
old singleton jobs is legitimate because the construction is only a
bookkeeping transport to depth `D+1`; all persistent jobs remain packed.
The donor budget, endpoint clearing, maximum-socket count, residue-piece
bound, and strict `h<r` inequality are correct.  The named corollary now
states the remaining finite Hall hypothesis and does not require a literal
name for a nontransported endpoint socket.

## 1. Socket census and shift check

At old depth `D`, collar chains beginning at owner rank `r` are genuine
old-capacity-`D` occurrences.  Their number is

\[
 H_r=C_r-C_{r-1}={C_r\over r+1}.
\]

The endpoint triangle contributes exactly one exceptional socket of each
capacity `1,...,D`.  These sockets are not assumed to survive the depth
shift.  Old residual chains beginning at rank `t-1` have length one and
vanish when the new bottom becomes `t-1`.  A genuine old collar occurrence
of capacity `c` survives with capacity `c+1`.  These are exactly the socket
types used in the source.

## 2. One-socket insurance check

An injective packing puts at most one piece in a socket `P`.

* If `P` already holds a disposable singleton, nothing is required.
* If `P` is empty, one disposable singleton moves into it and vacates one
  genuine donor socket.
* If `P` holds a persistent piece of length `ell<=c(P)`, subdivide that
  interval piece into `ell` consecutive singleton pieces.  Move those
  pieces to `ell` distinct genuine sockets vacated by disposable singleton
  jobs, and put one displaced disposable singleton into `P`.

Every persistent job retains exactly its old total length and a consecutive
interval fragmentation.  Each donor has capacity at least one.  The
remaining `ell-1` displaced singleton jobs may be left unpacked: their new
residual length is zero.  The modified object need not be a complete old
packing; it is a transport certificate for every job which survives.

This last quantifier is the key point.  No target required at depth `D+1`
is discarded.

## 3. Simultaneous donor budget

Take all donors outside the target socket set and outside previously used
donor sockets.  A target of capacity `c_i` needs at most `c_i` donors.  If
it already contains a disposable singleton, it needs none, while that one
singleton is unavailable outside the target set.  Hence a total stock of
`sum_i c_i` integral disposable jobs is sufficient even when some of that
stock initially lies in target sockets.

For `h` maximum sockets and the `D` endpoint sockets, the crude donor
budget is exactly

\[
 hD+\sum_{c=1}^D c
 =hD+{D(D+1)\over2}.
\]

At most `D` disposable jobs can belong to the at-most-`D` fractional-job
family.  Thus hypothesis (0.6) supplies the claimed integral donor stock.
All donors are genuine collar sockets because the complete target set,
including every endpoint socket, is excluded from donor selection.

## 4. Extreme-point rounding and endpoint clearing

The configuration-LP basic-support theorem leaves at most `D` jobs with
more than one positive configuration.  Every other job has one integral
configuration, and type capacities inject all its pieces into distinct old
occurrences.  Jobs in the exceptional family are not installed at this
stage, so they cannot obstruct the insurance operation.

After simultaneously insuring the selected maximum sockets and every
endpoint socket:

* every persistent integral job remains packed;
* any persistent piece formerly on an endpoint has moved to a genuine
  donor occurrence;
* the endpoint sockets contain only jobs which vanish;
* the selected maximum occurrences contain only jobs which vanish.

Therefore terminal-cell deletion transports every installed persistent
job through the shift, uses no endpoint socket, and leaves all selected
maximum occurrences genuinely free with new capacity `D+1`.

Subdividing a piece during insurance causes no chronology problem.  Keep
the new singleton pieces consecutive in that job's ordered fragmentation;
terminal deletion then shortens or removes only its final piece exactly as
in the cited transport lemma.

## 5. Residue count and the strict `h<r` inequality

There are at most `D` uninstalled job descendants, each of new length at
most `t-2`.  Maximum-capacity new sockets split each into at most

\[
 \left\lceil{t-2\over D+1}\right\rceil
\]

pieces, for a total of at most

\[
 h=D\left\lceil{t-2\over D+1}\right\rceil.
\]

If the ceiling is positive, write

\[
 x={r-D-2\over D+1}.
\]

For every real `x`, `ceil(x)<x+1`; here

\[
 x+1={r-1\over D+1}.
\]

Consequently

\[
 h<D{r-1\over D+1}<r.
\]

The zero-ceiling case is immediate.  This proves the strict range needed
by the protected-start theorem, not merely an `O(r)` estimate.

## 6. Asymptotic hypotheses

At coefficient-one depth, `D=Theta(sqrt(r))` and `t=Theta(r)`, so `h=O(r)`.
Both

\[
 H_r={W\over r+1}
 \quad\text{and}\quad
 H_{t-1}=Theta(W/\sqrt r)
\]

are exponential in `r`, whereas `hD+D(D+1)/2` is polynomial.  Therefore
(0.5)--(0.6) hold for every sufficiently large `r`.

## 7. Named-overlay correction and replay

The named small-bank theorem also requires, with new bottom `b=t-1`,

\[
 b\ge1,
 \qquad h\le H_b,
 \qquad \binom{b+2}2\ge h.

The first follows from `t>=2`; the second follows from (0.6); the third is
now stated explicitly in Corollary 3.1 as

\[
 \binom{t+1}2\ge h.

\]

It holds automatically in the eventual regime because its left side is
`Theta(r^2)` and `h=O(r)`.

There is no need, and generally no supplied named-containment interface,
for assigning a literal old singleton value to an endpoint-triangle
socket.  Endpoint insurance is anonymous bookkeeping: its occupant has no
new residual descendant, and the socket itself is not transported.  The
named theorem needs only the explicit exclusion of endpoint sockets from
the surviving bulk.  The source was corrected accordingly.

For the maximum sockets, Theorem 5.1 co-chooses the old singleton values,
their containing rank-`r` starts, and the identical surviving physical
occurrences.  The named corollary correctly remains conditional on choosing
the bulk interval lift/Rado attachment compatibly on the complementary
starts.  It does not infer that compatibility from anonymous insurance.

## 8. Scope verdict

The theorem closes a real gap: the extreme-point rounding residue now uses
fewer than `r` actual maximum-capacity occurrences, so the entire residue
falls inside the proved small-start reserve.  Insurance of the endpoint
triangle avoids the extra at-most-`D` discarded persistent jobs from the
earlier argument.

It does **not** prove the old fractional configuration inequalities, the
named bulk Rado gate, upper/residence chronology, topology, or a word at
`B(2r)+1`.  With these exclusions and the corrected named-overlay wording,
the independent audit verdict is GO.
