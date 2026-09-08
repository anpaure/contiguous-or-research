# Self-audit: vanishing-singleton socket insurance

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_VANISHING_SINGLETON_SOCKET_INSURANCE_AND_FULL_SMALL_BANK_LIFT_20260805.md`  
**Method:** independent line-by-line reconstruction from the three declared
dependencies; no computation, search, or solver  
**Verdict:** **GO** for the anonymous theorem.  The named corollary is
correctly conditional on a bulk lift avoiding both the prescribed
rank-`r` starts and every endpoint-triangle socket.

## 1. Extreme-point scope

The configuration LP has one equality per individual job and `D` socket
tail inequalities.  An extreme point therefore has at most `D` individual
jobs with more than one positive configuration, not merely `D` job types.
Every other job has one integer Ferrers configuration.  The aggregate tail
inequalities inject all pieces of those configurations into distinct
actual sockets.  This is exactly the input used by the insurance theorem.

## 2. Legitimacy of sacrificing old singleton jobs

An old residual chain beginning at rank `t-1` has length one.  When the
bottom changes from `t` to `t-1`, that residual chain is empty; its named
rank-`t-1` target belongs to the new collar instead.  Therefore the proof
may leave any number of those old jobs unpacked while constructing the new
depth-`D+1` packing.  It never uses the altered bookkeeping as a claimed
depth-`D` solution.

If a target socket contains a piece of length `ell`, replacing it by
`ell` unit subpieces preserves the same surviving job and uses `ell`
distinct sockets vacated by disposable jobs.  Every donor socket has old
capacity at least one and is a genuine collar occurrence, so all unit
pieces transport through the shift.  The construction preserves the
interval order by replacing one consecutive piece by its consecutive unit
subpieces.

## 3. Simultaneous donor count

Let the target sockets have capacities `c_i`.  If `s` of them already hold
disposable jobs, those `s` jobs are unavailable as donors but those same
targets require no repair.  The remaining donor demand is at most
`sum_i c_i-s`, while the available integral disposable jobs outside the
target set number at least `H_(t-1)-D-s`.  Thus the single inequality

\[
 H_{t-1}-D\ge\sum_i c_i
\]

is sufficient.  For `h` maximum sockets and the complete endpoint triangle
the right side is exactly

\[
 hD+{D(D+1)\over2}.
\]

Donors are chosen outside every endpoint socket, so no transported unit
piece relies on an unproved boundary lift.

## 4. Freed-bank size

Every unresolved descendant has length at most `t-2` and a freed maximum
socket has new capacity `D+1`.  At most `D` unresolved jobs therefore need
at most

\[
 h=D\left\lceil{t-2\over D+1}\right\rceil
\]

pieces.  With `t=r-D`, positivity of the ceiling gives

\[
 \left\lceil{r-D-2\over D+1}\right\rceil
 <{r-1\over D+1},
\]

and hence `h<r`.  There are `H_r=W/(r+1)` genuine maximum occurrences,
so the bank exists eventually.  The donor requirement is `O(r^(3/2))`,
whereas `H_(t-1)=Theta(W/sqrt(r))`; all displayed finite inequalities hold
eventually.

## 5. Named boundary

The named start-matroid theorem handles every family of fewer than `r`
requested rank-`r` starts and co-chooses the old singleton/new exceptional
use of the same occurrence.  It does not itself reroute an arbitrary named
bulk away from those starts.  The corollary therefore explicitly assumes
the complementary bulk Rado lift.  It also assumes that the bulk avoids the
endpoint triangle; without that clause, assigning disposable singletons to
the endpoints could displace named chunks with no proved containing
replacement.  With both exclusions stated, the overlay is exact.

## 6. Scope

No fractional all-price inequality, arbitrary-bulk Rado cut, carrier
serialization, upper deck, residence, topology, or safe opening is inferred.
The theorem closes only the size and physical occurrence form of the
rounding residue.
