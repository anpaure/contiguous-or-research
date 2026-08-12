# A tagged checkpoint returns the beta train without losing its occurrence

**Date:** 2026-08-06  
**Method:** stationary marked-corridor train transport plus the literal
full-matching beta path; no computation or search  
**Status:** independently audited conditional return theorem. It closes the
long-corridor and endpoint-parity parts when the beta conversion is performed
at a fully tagged checkpoint. The authoritative audit is
MATH_AUDIT_ODD_FULL_MATCHING_BETA_AND_TAGGED_RETURN_20260806.md.
Three bounded preparation rows remain explicit in Section 5.

## 1. Tagged-checkpoint hypothesis

Let

\[
 \mathcal G=\{20,01,21\},\qquad H=02.
\]

Assume the odd tape is at the checkpoint after every nonneutral source
extreme has been tagged but before the tags are finalized. Thus every work
block between the fixed collar berth and \(p_1\) lies in \(\mathcal G\).
At the berth retain the double head

\[
                              H\mid H.
\tag{1.1}
\]

Retain also an exterior record which recovers both the source branch
\(a_1\) **and the ordered collar source**, after the old \(p_1\) row is
overwritten. Merely retaining \(H|H\) and the residual signed count is not
enough: those data recover only the collar sum. When the head reaches the
beta site, orient its nearer
block as the scan pair

\[
                         p_2=(v,u)=20
\]

immediately after \(p_1=(g,b)\); the second \(H\) lies later and remains
fixed during the local path. This exact connector-head alignment is a
hypothesis: the current global transport theorem has not yet proved that
the nearer transported head occupies precisely the scan pair \(p_2\).

## 2. Outward transport and local conversion

Regard (1.1) as one length-two active train. If the corridor has even
length, Corollary 4.2 of the stationary-corridor theorem transports it to
the \(p_1\) neighbourhood while replacing every crossed
\(\mathcal G\)-block by its injective stationary mark. If the corridor has
odd length, leave the berth-adjacent block unmarked, cross that one block
by the corrected fixed-berth guarded swap, and apply Corollary 4.2 to the
remaining even-length corridor.

For corridor length zero the train is already local. For corridor length
one, the untouched \(p_1\) row on one side and the named fixed berth record
on the other locate the six-coordinate active window. Choose one simple
fixed-mass train/block interchange path; local mass and the retained branch
record identify its ordered endpoint type. This is the same two-fixed-end
decoder as the corrected one-interior fixed-berth shuttle.

Keep the second \(H\) fixed and apply
MATH_THEOREM_ODD_FULL_MATCHING_TERMINAL_BETA_LOCAL_PATH_20260806.md
to the first \(H\), \(B_1\), and the other coordinate of \(p_1\). The
active train is now

\[
                              E\mid H,
\tag{2.1}
\]

where \(E\in\{00,20,22\}\) is the compensating target block and
\(p_1=c(B_1^*)\). The local theorem intentionally changes \(p_2\) from the returned head to
the compensating target block. The untouched second head locates every
strict local state independently of any repeated work-tape pattern.

There is one endpoint-parity detail. A marked crossing of one
\(\mathcal G\)-block both swaps two even-length blocks and changes
\(Y\) to \(\mu(Y)\). The swap has even token-graph parity, whereas the
mark change has odd parity. The schedule above marks an even number of
blocks: \(s\) when \(s\) is even and \(s-1\) when \(s\) is odd. The one
unmarked train/block swap has even parity because the two block lengths
are four and two. Hence arrival toggles the endpoint of the selected
\(p_1\) row an even number of times and enters the local beta theorem at
its literal source endpoint. No external parity register is needed.

## 3. Immediate marked return

Do not erase any corridor mark. Move (2.1) back across the marked corridor
in reverse order, using the return half of Corollary 4.2.

Every required train/mark interchange lies in a nonextreme mass layer.
Indeed, \(E|H\) has mass \(2,4\), or \(6\), while a stationary mark has
mass \(1,2\), or \(3\); their six-coordinate total is strictly between
zero and twelve. Hence the capacity-two token graph is connected and a
simple local interchange path exists.

During this return the target row \(p_1=c(B_1^*)\) is nonquiet and precedes
the delimiter. All physical work is disjoint from \(p_1\), so its selected
edge supplies the directed lift while preserving its unordered row. The
maximal marked corridor locates the moving train exactly as in the
stationary-corridor decoder.

After (2.1) reaches the fixed berth, erase the stationary marks one at a
time. In the odd-length case, reverse the sole unmarked fixed-berth swap
after the marked return and before declaring the train home. The work
tape is restored literally to the fully tagged checkpoint, the berth
contains \(E|H\), \(p_1\) is its exact target endpoint, and \(p_2\) has
its source value.

Indeed every marked-block/train interchange on the return has even parity:
the block lengths are four and two, so the endpoint change of the weighted
token-position parity is

\[
 2\,\operatorname{mass}(E|H)-4\,\operatorname{mass}(\mu(Y)),
\]

which is even. Erasing the even number of installed marks toggles \(p_1\)
an even number of times. Thus the target endpoint produced by the local
theorem is restored, not merely its unordered row.

## 4. The conditional return theorem

### Theorem 4.1 (tagged-checkpoint beta return)

Under the tagged-checkpoint, persistent ordered-record, and exact
connector-head alignment hypotheses of Section 1,
the concatenation

\[
 H|H\text{ at berth}
 \longrightarrow
 H|H\text{ at }p_1
 \longrightarrow
 E|H\text{ at }p_1
 \longrightarrow
 E|H\text{ at berth}
\]

is a directed occurrence-labelled path in the fixed matching contraction.
It changes only \(B_1\), the selected compensating head block, the temporary
corridor marks, and (twice, when needed) the delimiter clock \(p_2\).
Every other block and every later clock is restored.

#### Proof

The outward and return path banks are supplied by the stationary-corridor
decoder, including the length-two train extension. The local middle path
is the exact forced-matching theorem cited in Section 2. Its second head
and exterior branch record distinguish source, branch, and microstep.
The parity calculation in Sections 2--3 proves that the local theorem is
entered at its literal source endpoint and that the full return restores
its literal target endpoint.

The three phases have disjoint literal signatures: an outward marked
corridor ending in a double head, the fixed second head at \(p_1\), and a
returning marked corridor ending in \(E|H\). At a checkpoint the maximal
marked interval and the fixed berth determine the phase and active
address. Inside a chosen local path, simplicity determines the microstep.
Equality of two global states therefore forces equality of source, phase,
address, and microstep. \(\square\)

## 5. Remaining global assignment

The theorem has closed the local dynamics, changed-train return, and long
endpoint parity. What remains is an exact bounded preparation/scheduling
statement:

1. **Connector-head alignment.** Transport or rethread the nearer \(H\)
   so that it is literally the next scan pair \(p_2=(v,u)=20\).
2. **Order record.** Before beta overwrites the old three-row \(p_1\)
   record, write one named target collar block or a disjoint order record;
   \(H|H\) plus the residual signed count remembers only the collar sum.
3. **Bounded non-\(\mathcal G\) interfaces.** Remove, route around, or pack
   the finitely many residual midpoint/interface blocks which remain outside
   the fully tagged \(\mathcal G\)-corridor.

After those rows, choose the source digit of charge
\(-\epsilon(a_1)\), return its compensating target occurrence, and run the
fixed-berth accumulator on the remaining bounded bank. Global charge
guarantees existence of the opposite digit, but not these three literal
interfaces. Thus the remaining odd gate is bounded preparation, rather
than local beta dynamics or a long parity problem.
