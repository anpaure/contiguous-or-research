# Exact rank-eight provider interface for the frozen 306-owner prefix

Date: 2026-09-08.
Status: proved source-relative constraints, one legal exact pin, and bounded remote verification. The specified one-pivot completion is now RULED OUT by the global facet-count argument in Section 9. No extension Q or full universal word is claimed. The local provider statements remain valid necessary conditions, but do not describe a viable one-pivot completion route.

## 1. Fixed source and result

Let P be the materialized 306-owner path

    scratch/badsix_relaxed_306_owner_path.word

and let E be its 308-letter maximal depth-two inverse

    scratch/badsix_relaxed_308_depth2_source.word.

Use zero-based indices. The five rank-eight targets missing from the current global adjacent-intersection palette are

    H={21866,43860,46420,70998,92834}.

Exact ordinary-interval enumeration finds NONE of these targets anywhere in E. This includes both the stable positions 0 through 305 and intervals involving final temporary letters 306 and 307. Upon attachment to a depth-three remainder Q, only those last two existing envelope letters change; later Q letters are new.

A stronger structural statement controls all future caps, rather than only the maximal E:

- 21866 can be installed exactly at A_0 without disturbing any owner window;
- none of H can use the one-pivot exceptional cell [306,308], for any compatible extension Q;
- at most one still-missing target can be supplied by the final suffix;
- no target in H can be the intersection at the P/Q seam; and therefore
- at least THREE of {43860,46420,70998,92834} must appear as adjacent-owner intersections strictly inside Q in any universal completion using this fixed P and this one-pivot schedule.

Each of the five targets has seven explicit remaining rank-nine superowners available in Q. These local provider constraints alone do not prove irreparability. However, the additional global count in Section 9 does prove that this prefix has no universal one-pivot completion. The provider table remains useful if the deadline schedule is changed.

## 2. General exceptional-facet theorem for increasing deadlines

Let W>=2, and let T_0,...,T_(W-1) be distinct sets of the same rank m, realized by a nonempty word A on owner intervals

    I_i=[i,r_i],   r_i=i+h_i,

where the nonnegative integers h_i are nondecreasing. The word has exactly the positions 0,...,r_(W-1); there is no additional unconstrained tail after the final owner deadline. Suppose the last two depths agree, h_(W-2)=h_(W-1). Let J be the number of strict depth increases h_j>h_(j-1), where 1<=j<=W-2. Let D be the rank-(m-1) adjacency palette

    D={T_i intersect T_(i+1): 0<=i<W-1,
                                  |T_i intersect T_(i+1)|=m-1}.

Then A can realize at most J+2 distinct rank-(m-1) targets outside D.

More precisely, each such target must have a witness belonging to one of these nested interval families:

1. initial prefixes [0,b] with b<r_0;
2. for a strict depth increase at j, intervals [j,b] with
   r_(j-1)<b<r_j; or
3. final suffixes [a,r_(W-1)] with a>W-1.

Each family contributes at most one distinct target of a fixed rank, because its intervals are nested and their unions form an inclusion chain.

### Proof

Take a witness [a,b] of rank m-1. It cannot contain an entire owner interval I_i, whose union has rank m.

If b=r_i for some i<W-1, avoidance of I_i requires a>=i+1. The witness is then contained in both I_i and I_(i+1), so its union is contained in T_i intersect T_(i+1). Since the owners are distinct rank-m sets, this intersection has size at most m-1. The witness union must equal it, hence belongs to D.

If b<r_0 and a>=1, the witness is contained in I_0 and I_1, giving the same conclusion. The only other initial possibility is a=0, which gives family 1.

If r_(j-1)<b<r_j, avoidance of I_(j-1) requires a>=j. Since no final jump occurs, j<=W-2. If a>=j+1, the witness lies in I_j and I_(j+1), and belongs to D. Otherwise a=j, giving family 2. A nonempty deadline gap occurs precisely at a strict depth increase.

Finally, if b=r_(W-1), avoidance of the last owner interval requires a>W-1, giving family 3. These cases partition all possible right endpoints. Counting at most one distinct fixed-rank union per nested family proves J+2. QED.

The no-final-jump premise is intentional: an arbitrarily long tail belonging only to the last owner could supply additional incomparable facets. This theorem is a specialized improvement over the general 2d endpoint bound, not a replacement for that bound under arbitrary starts or deadlines.

## 3. Specialization to the one-pivot K17 schedule

For the proposed completion P,Q, use W=24310, L=306 and

    I_i=[i,i+2] for i<L;
    I_i=[i,i+3] for i>=L.

The missing deadlines are 0,1,308. The theorem gives exactly three possible exceptional facet families:

- initial [0,0] and [0,1];
- the single pivot cell [306,308];
- terminal suffixes ending at physical position 24312.

All other rank-eight witnesses must have their value in the final owner-adjacency palette. This statement applies to every simultaneous common cap that preserves the owner windows, not just to the maximal envelope.

For example, the other apparent cells ending at the pivot, [307,308] and [308,308], lie in Q_0 intersect Q_1. Any rank-eight value there is already its adjacency color. Similarly, terminal cells ending before 24312 lie in the final two owners and cannot create an additional absent adjacency color.

## 4. A legal initial pin

The first owner is

    P_0=21867=21866 union {bit 0}.

The first three maximal source letters are

    E_0=21867, E_1=21803, E_2=21801.

Both E_1 and E_2 contain bit 0. Replacing E_0 by 21866 therefore preserves P_0 on [0,2]. Position 0 belongs to no other owner interval, so every other owner remains unchanged. Direct replay confirms all 306 owner identities.

For a subsequent common-cap compiler, reserve the exact target pin

    A_0=21866

and, for a simple protected witness of the removed bit, require bit 0 in A_1. This is legal since 0 belongs to E_1. Then P_0 is supplied by A_0 union A_1 regardless of any further shrink at position 2. The rest of the compiler must still enforce its other owner and lower-target obligations.

No other member of H is contained in P_0. Hence none can use the initial exceptional family.

## 5. The pivot is impossible for all five targets

The last prefix owner and maximal stable letter at its start are

    P_305=103765,   E_305=5461.

Their exact difference is

    P_305 minus E_305 =98304={bits 15,16}.

In every word subordinate to the proposed owner's envelopes, positions 0 through 305 remain within these same maximal prefix envelopes. The owner P_305 is prescribed on [305,307]. Since neither bit 15 nor bit 16 can occur at position 305, both must occur at positions 306 or 307.

Therefore every target realized on the entire pivot cell [306,308] must contain both bits 15 and 16. Each member of H omits at least one:

| target | missing mandatory pivot bit(s) |
|---:|---|
| 21866 | 15,16 |
| 43860 | 16 |
| 46420 | 16 |
| 70998 | 15 |
| 92834 | 15 |

This excludes the pivot cell for all five masks independently of the chosen Q_0,Q_1,Q_2 and independently of how the lower caps are coordinated. Further shrinking the stable prefix can only create additional required bits in its last two positions; it cannot remove this obstruction.

Also no target in H is contained in P_305. Thus none can equal P_305 intersect Q_0 at the new P/Q adjacency.

## 6. Exact final-suffix possibilities

Assume Q is a Johnson path and its last two owners are V,U. Put

    R=V intersect U, |R|=8.

The last two maximal source letters are R and U, at physical positions 24311 and 24312. Earlier positions of the final suffix lie in R. Consequently at most one rank-eight target outside the adjacency palette can occur in the final exceptional suffix family.

For a prescribed rank-eight target S absent from that palette, the exact endpoint condition is

    S is a facet of U, and S is not R.

Necessity: a final suffix is contained in the last owner interval, so S is a subset of U; S differs from R because it is absent from the adjacency palette.

Sufficiency at a valid maximal source: write U=S union {b}. Since S is not R, the bit b belongs to R. Replace only the final source letter U by S and keep the preceding maximal letters. The penultimate letter R supplies b, so the last owner remains U. No earlier owner uses the final position. Thus the exact one-letter pin A_24312=S preserves every owner.

For later simultaneous capping, retain b at A_24311 as a positive guard and enforce the exact final pin. These two letters then supply the complete last owner. This is a sufficient compatible boundary prescription, conditional on the rest of Q already being a valid source.

For any chosen target S in the table below, the possible last owners U are exactly its seven remaining Q superowners. Its penultimate owner V must be a remaining rank-nine Johnson neighbor of U whose removed coordinate is in S; equivalently,

    V=U minus {y} union {z},
    y in S, z outside U,

so that the exceptional bit b=U minus S stays in V. The chosen V must also obey the final chronology's residence, nonrepetition, and upper-coverage conditions. No claim of a compatible full Q follows from this local condition.

## 7. Explicit remaining providers and forced Q adjacencies

Each target S has exactly two superowners in P: the endpoints of its original cut block. The other seven are available in Q:

| S | its seven remaining rank-nine superowners |
|---:|---|
| 21866 | 21870,21882,21994,22378,23914,30058,87402 |
| 43860 | 43861,43868,43892,43988,44884,47956,60244 |
| 46420 | 46421,46428,46452,46548,46932,48468,62804 |
| 70998 | 70999,71006,71030,71126,71510,73046,87382 |
| 92834 | 92835,92842,92898,93090,93858,96930,125602 |

Any two distinct owners in one row intersect exactly in S. Hence each row supplies 21 unordered candidate Johnson edges with color S. These are actual vertices remaining for Q, not an abstract color count.

Now consider the four targets other than 21866. They cannot use the initial exceptional family, cannot use the pivot, and cannot occur at the P/Q adjacency. The final suffix can supply at most one of them. Every other one must therefore be an adjacency color strictly inside Q. This proves the necessary condition

    at least three of 43860,46420,70998,92834
    occur as adjacent intersections inside Q.

A convenient sufficient planning interface is to choose one of these four targets for the final pin and reserve a provider edge from each of the other three rows. Alternatively recreate all four as Q adjacency colors. This only identifies the needed local objects; their chronological placement, residence and upper-witness compatibility remain unresolved.

## 8. Exact bounded verification

The following verifier was executed only on h100:

    scratch/audit_k17_pbbs_prefix_rank8_provider_interface_20260908.py

It exhaustively checked ordinary interval unions of the fixed 308-letter source for the five specified masks; classified stable versus boundary-dependent witnesses; enumerated the nine rank-nine superowners of each mask and separated the two in P from the seven remaining; checked the pivot and P/Q-seam exclusions; installed the initial pin and replayed all 306 owner windows.

The retained result is

    scratch/k17_pbbs_prefix_rank8_provider_interface_20260908.json.

Terminal result:

    PASS: exact five-target absence, seven remaining superowners each,
    pivot exclusion, and legal initial pin.

No extension search, random experiment, or new port bank was run. The general exceptional-facet theorem and the pin/obstruction proofs above are independent of this finite check.

### Provider-versus-witness qualification

A reserved Q edge with intersection S supplies the needed owner-level color. A later arbitrary common cap must still retain a literal interval witness of S; reproducing its two owner rows alone does not force their overlap to have union equal to their intersection. For a legal maximal flat Q envelope, the canonical flag identity supplies the natural overlap witness, but that positive lower obligation must remain in the common-cap compiler. Thus the provider-edge interface is necessary and is a concrete input to the compiler; it is not by itself a completed lower-target construction.

## 9. Decisive global obstruction to the one-pivot completion

The preceding local interface misses a global capacity condition. The fixed prefix already has three non-Johnson owner adjacencies. For any complete linear chronology through all W=24310 rank-nine owners, let b be its number of non-Johnson steps and e the repeated-color excess among its Johnson steps. Its number of distinct rank-eight adjacent-intersection colors is exactly

    W-1-b-e.

Since there are W rank-eight targets, a universal word must supply at least

    1+b+e

rank-eight targets outside this adjacency palette. The one-pivot theorem in Sections 2-3 permits at most three. Hence every universal one-pivot completion must satisfy b+e<=2.

The frozen prefix has b>=3 already, so no Q can satisfy this condition. Therefore:

    There is no universal 24313-letter completion of this fixed prefix
    using the depth-two / depth-three one-pivot schedule.

This conclusion is independent of Q's ordering, upper coverage, the common-cap method, and the apparent seven-provider supply for each current hole. It is a source/schedule obstruction, not a lower bound on unrestricted nu(17).

A separate broader analysis and the exact prefix repeat check are recorded in

    scratch/K17_PBBS_PREFIX_ONE_PIVOT_NOGO_AND_CONSECUTIVE_START_BUDGET_20260908.md.
